# TODO 荷载类

class Beam2DLoad:
    def __init__(self, id, LoadType, q1, q2):
        self.id = id
        self.LoadType = LoadType        # 分布荷载类型， 1-均布荷载， 2-线性分布荷载
        self.q1 =q1       # node 1 荷载值
        self.q2 =q2       # node 2 荷载值，若是均布荷载，q1、q2相等

load1 = Beam2DLoad(1, 1, -20, -20)
# 一个荷载对象，多个单元共有

class ElemBean2D:
    def __init__(self, id, sec, mat, node1, node2, disLoad):
        self.id = id
        self.sec = sec
        self.mat = mat
        self.node1 = node1       # node 1 荷载值
        self.node2 = node2       # node 2 荷载值，若是均布荷载，q1、q2相等
        self.disLoad = disLoad

elem1 = ElemBean2D(1, sec1, mat1, nd1, nd2, load1)
elem2 = ElemBean2D(1, sec1, mat1, nd2, nd3, load1)