# TODO 几何截面类
""" 杆系结构的截面是一个重要的特征，截面面积，惯性矩等参数参与有限元计算"""

# 矩形截面类
class SectionRectangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def getArea(self):    # 计算截面积
        return self.b * self.h

    def getI(self):     # 计算截面惯性矩
        return 1/12 * self.b * self.h ** 3


# 圆截面类
class SectionCircle:
    def __init__(self, r):
        self.r = r

    def getArea(self):
        return 3.1415926 * self.r ** 2

    def getI(self):         # 圆形截面惯性矩
        return 0.25 * 3.14 * self.r ** 4

sec = SectionRectangle(1, 2)
sec.getArea()


# TODO 材料类
"""材料类用于对材料特性的描述，如弹性模量，密度，线膨胀系数等等。对于非线性分析，还需要材料本构关系"""

# 基本的材料类， 仅有弹性模量
class Material:
    def __init__(self, E):
        self.E = E

mat = Material(2E11)

# 包括密度，线膨胀系数
class Material1:
    def __init__(self, E, rho, alpha):   # rho、alpha 密度，线膨胀系数
        self.E = E
        self.rho = rho
        self.alpha = alpha

# ---------------用于平面应力-------------------
class MatPlane1:
    def __init__(self, E, nu, t):   # nu 泊松比 t 厚度
        self.E = E
        self.nu = nu
        self.t = t

    def matrix_D(self):          # 弹性刚度矩阵
        E = self.E
        nu = self.nu

        tmp = E / (1. - nu**2)
        D = nu.array([[1, nu, 0],
                     [nu, 1, 0],
                     [0, 0, 0.5*(1-nu)]])

        D = tmp * D
        return D
