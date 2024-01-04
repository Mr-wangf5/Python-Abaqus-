# TODO 节点类
"""
结构标识：指节点、单元编号、确定坐标系以及约束等。也叫前处理
"""
import numpy as np

"""
节点类
节点有编号，自由度，坐标，节点类等。
"""
class NodeBeam2D:
    def __init__(self, id, coord_X, RY, Rtheta, fy, ftheta):
        self.id = id
        self.coord_X = coord_X
        self.RY = RY
        self.Rtheta = Rtheta
        self.fy = fy
        self.ftheta = ftheta

    # 计算总自由度
    def findGdof(self, gdof):
        if self.RY == 1:
            gdof = gdof + 1
            self.RY = gdof
        if self.Rtheta == 1:
            gdof = gdof + 1
            self.Rtheta = gdof

    # 节点力组装到整体节点向量中
    def findLoadVector(self, FF1):
        if self.RY !=0:
            FF1[self.RY-1] = FF1[self.RY-1] + self.RY
        if self.Rtheta != 0:
            FF1[self.Rtheta -1] = FF1[self.Rtheta-1] + self.ftheta

        return FF1

nd1 = NodeBeam2D(1, 0, 0, 0, 0, 0)
nd2 = NodeBeam2D(2, 4, 0, 1, 0, 0)
nd3 = NodeBeam2D(3, 6, 0, 1, 0, 0)
nd4 = NodeBeam2D(4, 10, 0, 1, 0, -1)
listNode = [nd1, nd2, nd3, nd4]

gdof = 0
for iNode in listNode:
    gdof = iNode.findGdof(gdof)

F = np.zeros((gdof))     # 初始化
for iNode in listNode:
    gdof = iNode.findLoadVector(F)

print(F)
