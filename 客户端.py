# ---------客户端代码-----------
import numpy as np

mat1 = Material(4)
mat2 = Material(1)
mat3 = Material(2)

nd1 = NodeBeam2D((1, 0), 0, 0, 0, 0)
nd2 = NodeBeam2D((2, 4), 0, 1, 0, 0)
nd3 = NodeBeam2D((3, 6), 0, 1, 0, 0)
nd4 = NodeBeam2D((4, 10), 0, 1, 0, 0)

listNode = [nd1, nd2, nd3, nd4]

# 截面对象
sec = SectionRectangle(1, 12, 1)

# 分布荷载对象，多个单元并存
load1= Beam2DLoad(1, 1, -6, -6)
load2 = Beam2DLoad(2, 1, 0, 0)

# 单元对象
elem1 = ElemBeam2D(1, sec, mat1, nd1, nd2, load2)
elem2 = ElemBeam2D(2, sec, mat2, nd2, nd3, load2)
elem3 = ElemBeam2D(3, sec, mat3, nd3, nd4, load1)

listElem = [elem1, elem2, elem3]

gdof = 0
for iNode in listNode:
    gdof = iNode.findGdof(gdof)

# 整体节点力向量
F = np.zeros((gdof))
KK = np.zeros((gdof, gdof))

for iElem in listElem:
    ek = iElem.elemStifinessMatrix()
    equf = iElem.elemEquForce()
    F = iElem.findForceVector(F)
    KK = iElem.AssembleStifinessMatrix(KK)
    print(KK)

    # 进一步封装
class FEModel:
    def __init__(self, listNode, listElement):
        self.listNode = listNode
        self.listElement = listElement
        self.gdof = 0
        for iNode in self.listNode:
            self.gdof = iNode.findGdof(self.gdof)

    def getForceVector(self):
        FF = np.zeros(self.gdof)
        FF1 = np.zeros(self.gdof)
        for iNode in self.listElement:
            FF1 = iNode.findLoadVector(FF1)

        for iElem in self.listElement:
            FF = iElem.findForceVector(FF)

        FF =FF +FF1
        return FF

    def getStructStifinessMatrix(self):
        KK = np.zeros(self.gdof, self.gdof)
        for iElem in self.listElement:
            KK = iElem.AssembleStifinessMatrix(KK)
        return KK

# 简化了客户端代码
listNode = [nd1, nd2, nd3, nd4]
listElem = [elem1, elem2, elem3]

# 实例化一个结构对象
fm = ModStruct.FEModel(listNode, listElem)
ff = fm.getForceVector()
KK = fm.getStructStifinessMatrix()