#TODO 封装

"""面向对象语言通过重用现有的模块或函数来帮助程序员降低程序的复杂性。面向对象的概念设计语言是基于类的"""
import math


class Point2D:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x = dx + self.x
        self.y = dy + self.y
        print(f'移动后的坐标：')
        print('({0}, {1})'.format(self.x, self.y))

p1 = Point2D ((0, 0), 1, 0)          # 还可以定义很多point 2D对象，P2, P3
p1.move(0, 1)

"""类包含属性（Attribute）和方法（Method)，
将他们写在一起叫做封装，第二层是指隐藏属性与方法。 P1.move(0,1)直接通过接口调用"""

"""
Python 内置类型（也称为类）有str、int、float、bool、list、tupple或dict等。 
自定义的类和上述类型地位平等 
"""

class Element2D:
    def __init__(self, id, node1, node2):
        self.id =id           # id 是int类型
        self.node1 = node1         # node1 是自定义Point2D类型
        self.node2 = node2

    def Length(self):
        dx = self.node2.x - self.node1.x
        dy = self.node1.y - self.node2.y
        return math.sqrt(dx**2 + dy **2)

nd1 = Point2D(1, 3., 0.)
nd2 = Point2D(2, 5., 2.)

elem1 = Element2D(1, nd1, nd2)
l = elem1.Length()
print(l)

#TODO 继承

# 创建一个3D类， 可以从Point2D继承，二者有逻辑关联
class Point3D(Point2D):
    def __init__(self, id, x, y, z):
        super().__init__(id, x, y)         # super 方法用于继承
        self.z = z

    def Move(self, dx, dy, dz):         # 覆盖掉基类方法
        self.x = dx + self.x
        self.y = dy + self.y
        self.z = dz + self.z
        print(f'移动后的坐标：')
        print('({0}, {1}, {2})'.format(self.x, self.y, self.z))

        # Point 2D叫做父类或基类， Point3D叫做子类或派生类


class Element3D(Element2D):
    def __init__(self, id, node1, node2):
        super().__init__(id, node1, node2)
        # node1 是自定义的Point3D类型

    def Length(self):
        dx = self.node2.x - self.node1.x
        dy = self.node1.y - self.node2.y
        dz = self.node1.z - self.node2.z
        return math.sqrt(dx**2 + dy **2 + dz**2)

nd1 = Point3D((1, 0), 3., 0., 0.)
nd2 = Point3D((2, 0), 5., 2., 0.)

elem1 = Element3D(1, nd1, nd2)
l = elem1.Length()
print(l)

"""Element 3D若不定义Length方法，则会继承基类Element 2D的Length方法，若重新定义，则覆盖掉基类方法 """
# example
class Point2D:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def getID(self):
        return self.id

class Point3D(Point2D):
    def __init__(self, id, x, y, z):
        super.__init__(id, x, y)
        self.z = z

nd1 = Point3D((0.0), 3, 0, 0)
id = nd1.getID()
print(id)

# point3D对象继承了基类getID方法




# 部分继承基类
class Shape():
    def output(self):
        print("I AM A SHAPE")

class Square(Shape):
    def output(self):
        super().output()
        print("Specially, I am a square")

square = Square()
square.output()

