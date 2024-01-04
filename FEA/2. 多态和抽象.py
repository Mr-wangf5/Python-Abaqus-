# TODO 多态
"""多态就是为不同的数据类型提供接口的能力， 这里的接口指函数或方法"""
import math


class Rectangle():
    def __init__(self, width, length):
        self.width =width
        self.length =length

    def calculate_perimeter(self):
        return self.width *2 +self.length*2

class Square():
    def __init__(self, s1):
        self.s1 =s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(25, 30)
a_square = Square(20)

shape_list = [a_rectangle, a_square]
for iShape in shape_list:
    d = iShape.calculate_perimeter()
    print(d)

# TODO 抽象
"""抽象（Abstraction）指在事物的诸多特征中，保留解决问题所需的部分特征这一过程"""

class ElemBeam2D:
    def __init__(self, id, I, mat, node1, node2, LoadType, val1, val2):
        self.id = id
        self.I = I
        self.mat = mat
        self.node1 = node1
        self.node2 = node2
        self.LoadType = LoadType         # 分布荷载类型 1-均布荷载
        self.val1 = val1          # node1 荷载值
        self.val2 = val2          # node 2 荷载值

    def elemLength(self):
        dx = self.node2.coord_X- self.node1.coord_X
        return math.sqrt(dx * dx)

    def elemEquforce(self):
        pass

    def findForceVector(self, FF):
        equf = self.elemEquforce()
        ets = self.elemToStruct()

        for k in range(len(ets)):
            if ets[k] != 0:
                index = ets[k]
                FF[index-1] = FF[index-1] + equf[k]

        return FF

    def AssembleStiffnessMatrix(self, KK):
        pass

    def ElementDisp(self, delta):
        pass

    def ElemStress(self, delta):
        equf = self.elemEquforce()
        eld = self.ElementDisp(delta)
        ek = self.elemStifinessMatrix()
        fl = np.dot(ek, eld)
        fl = fl - equf
        return fl

    def PlotData(self, delta):
        l = self.elemLength()
        x = np.arange(0, l+0.01, 0.05)
        EI = self.mat.E * self.I
        l2 = l **2
        l3 = l **3
        l4 = l **4

        q = self.val1
        invA = np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])

