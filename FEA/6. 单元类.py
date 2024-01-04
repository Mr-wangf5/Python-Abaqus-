# TODO 单元类
"""对于一个平面梁单元，其特征有编号、材料类型、截面类型、两个节点的信息、单元长度、
单元刚度矩阵、等效节点力、单元刚度矩阵集成到整体刚度矩阵、杆端力等等"""
import math


class ElemBeam2D:
    def __init__(self, id, sec, mat, node1, node2, distributeLoad):
        self.id = id
        self.sec = sec
        self.mat = mat
        self.node1 = node1
        self.node2 = node2

    # 单元长度，两个节点的坐标之差
    def elemLength(self):
        dx = self.node2.coord_X - self.node1.coord_X
        return math.sqrt(dx * dx)

    # 单元刚度矩阵
    def elemStifinessMatrix(self):
        I = self.sec.getI()
        EI = self.mat.E * I
        L = self.elemLength()

        L3 = L ** 3
        L2 = L * L
        a = 12 * EI/L3
        b = 6*EI/L2
        c = 4*EI/L
        d = 2*EI/L

        ek = np.arry([[a, b, -a, b],
                      [b, c, -b, d],
                      [-a, -b, a, -b],
                      [b, a, -b, c]])
        return ek
    # 单元向整体转换的标识
    def eleToStruct(self):
        elToStr = np.zreos((4), dtype = int)
        elToStr[0] = self.node1.RY
        elToStr[1] = self.node1.Rtheta
        elToStr[2] = self.node2.RY
        elToStr[3] = self.node2.Rtheta
        return elToStr

    # 单元等效节点力，公式假定q1,q2与坐标轴方向一致
    def elemEquForce(self):
        equf = np.zreos((4))
        L = self.elemLength()
        L2 = L*L
        q1 = self.distributeLoad.q1
        q2= self.distributeLoad.q2
        LoadType = self.distributeLoad.LoadType

        if LoadType ==1:           # 分布荷载类型， 1-均布荷载
            equf[0] = 0.5 * q1 *L
            equf[1] = q1 * L2 /12
            equf[2] = 0.5*q1*L
            equf[3] = -q1 * L2/12

        if LoadType ==2:           # 分布荷载类型， 1-线性分布荷载
            equf[0] = 1/20*(7*q1 + 3*q2)*L
            equf[1] = 1/60*(3*q1 + 2*q2)*L2
            equf[2] = 1/20*(3*q1 + 7*q2)*L
            equf[3] = -1/60*(2*q1 + 3*q2)*L2

        return equf

    # 单元等效节点力集成到整体力向量
    def findForceVector(self, FF):
        equf = self.elemEquForce()
        ets = self.eleToStruct()

        for k in range(len(ets)):
            if ets[k] !=0:
                index = ets[k]
                FF[index-1] = FF[index-1] + equf[k]
        return FF

    # 单元刚度矩阵集成到整体刚度矩阵
    def AssembleStiffinessMatrix(self, KK):
        ets = self.eleToStruct()
        ek = self.elemStifinessMatrix()
        for m in range(len(ets)):
            for n in range(len(ets)):
                if (ets[m] !=0) and (ets[n] !=0):
                    M = ets[m]-1
                    N = ets[n] -1
                    KK[M][N] = KK[M][N]+ek[m][n]
        return KK


    # 单元位移
    def ElementDsip(self, dalta):
        elemDisp = np.zreos(4)
        ets = self.eleToStruct()
        for j in range(4):
            if ets[j] !=0:
                M = ets[j]-1
                elemDisp[j] = delta[M]
        return elemDisp

    # 单元杆端力
    def ElemStress(self, delta):
        equf = self.elemEquForce()
        eld = self.ElementDsip()
        ek = self.elemStifinessMatrix()
        fl = np.dot(ek, eld)
        fl =fl-equf
        return fl







