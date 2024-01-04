##四点弯混凝土梁计算案例 @B站-土木老鸽
##知识点1：自定义材料库（def函数）
##知识点2：加载方式设置（==）
##知识点3：箍筋集合（元组）
##知识点4：切分实体简写（遍历列表）
##知识点5：关键词（master-slave；main-secondary）
from abaqus import *
from abaqusConstants import *
from caeModules import *
import time
import winsound
##知识点1：自定义材料库（def函数）
##定义材料库
def Mat():
    m.Material(name='Con')
    m.materials['Con'].Density(table=((2.39e-09,),))
    m.materials['Con'].Elastic(table=((31500.0, 0.28),))
    m.materials['Con'].ConcreteDamagedPlasticity(table=((38.0, 0.1, 1.16, 0.66667, 0.0001),))
    m.materials['Con'].concreteDamagedPlasticity.ConcreteCompressionHardening(table=(
        (14.06658, 0.0), (15.25467, 1.66e-05), (16.43459, 3.75e-05), (17.61097, 6.38e-05), (18.7982, 9.77e-05), (19.96877, 0.00014139),
        (21.15063, 0.00020197), (22.32383, 0.00029464), (23.4, 0.00055743), (22.2216, 0.00094511), (21.05047, 0.00116754), (19.86845, 0.00137563),
        (18.68694, 0.00158249), (17.51396, 0.00179412), (16.34338, 0.00201706), (15.17237, 0.00225716), (13.99457, 0.0025221), (12.8179, 0.00281811),
        (11.63847, 0.00315681), (10.45743, 0.0035532), (9.2818, 0.00402691), (8.10653, 0.00461422), (6.93325, 0.00537186), (5.76182, 0.0064034),
        (4.5897, 0.00792109), (3.41745, 0.01042338), (2.2453, 0.01544885), (1.07514, 0.03120224), (0.23397, 0.13929908)))
    m.materials['Con'].concreteDamagedPlasticity.ConcreteTensionStiffening(table=(
        (1.7607, 0.0), (1.87103, 1.58e-06), (1.98229, 3.73e-06), (2.09239, 7.01e-06), (2.2, 1.76e-05), (2.08921, 4.74e-05), (1.9791, 6.48e-05),
        (1.86797, 8.12e-05), (1.75689, 9.74e-05), (1.64661, 0.000114), (1.53665, 0.000132), (1.42646, 0.00015), (1.31573, 0.000171),
        (1.2051, 0.000194),
        (1.09422, 0.00022), (0.98318, 0.000251), (0.87265, 0.000287), (0.76215, 0.000332), (0.65184, 0.000389), (0.54171, 0.000468),
        (0.43151, 0.000582),
        (0.3213, 0.000771), (0.2111, 0.00115), (0.10108, 0.002335), (0.022, 0.010462)))
    m.materials['Con'].concreteDamagedPlasticity.ConcreteCompressionDamage(table=(
        (0.0, 0.0), (0.003603, 1.66e-05), (0.012989, 3.75e-05), (0.027085, 6.38e-05), (0.045758, 9.77e-05), (0.068872, 0.000141),
        (0.098425, 0.000202),
        (0.138675, 0.000293), (0.232219, 0.000557), (0.337302, 0.000945), (0.388789, 0.001168), (0.433252, 0.001376), (0.474258, 0.001582),
        (0.513102, 0.001794), (0.550776, 0.002017), (0.587813, 0.002257), (0.624681, 0.002522), (0.661301, 0.002818), (0.697891, 0.003157),
        (0.73445, 0.003553), (0.77073, 0.004027), (0.806784, 0.004614), (0.84236, 0.005372), (0.877128, 0.006403)))
    m.materials['Con'].concreteDamagedPlasticity.ConcreteTensionDamage(table=(
        (0.0, 0.0), (0.00216, 1.58e-06), (0.008595, 3.73e-06), (0.020578, 7.01e-06), (0.059398, 1.76e-05), (0.167314, 4.74e-05), (0.22871, 6.48e-05),
        (0.283731, 8.12e-05), (0.335412, 9.74e-05), (0.384849, 0.000114), (0.433042, 0.000132), (0.480528, 0.00015), (0.527813, 0.000171),
        (0.574731, 0.000194), (0.621514, 0.00022), (0.66812, 0.000251), (0.714206, 0.000287), (0.759815, 0.000332), (0.8046, 0.000389),
        (0.848172, 0.000468), (0.889889, 0.000582)))
    m.HomogeneousSolidSection(name='Section-Con', material='Con', thickness=None)
    m.Material(name='HRB400')
    m.materials['HRB400'].Density(table=((7.9e-9,),))
    m.materials['HRB400'].Elastic(table=((210000.0, 0.3),))
    m.materials['HRB400'].Plastic(table=(
        (475.0, 0.0), (500.0, 0.01423), (518.4, 0.03773), (571.6, 0.06123), (609.6, 0.08473), (632.4, 0.10823), (640.0, 0.13173), (638.84, 0.14093),
        (635.34, 0.15013), (629.52, 0.15933), (621.36, 0.16853), (610.88, 0.17773)))
    m.Material(name='Gang')
    m.materials['Gang'].Density(table=((7.8e-9,),))
    m.materials['Gang'].Elastic(table=((198000.0, 0.28),))
    m.HomogeneousSolidSection(name='Section-Gang', material='Gang', thickness=None)

##开始建模
m = mdb.Model(name='Model-CB')
session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)
##几何量（以下可以更改）
##砼梁
Wc = 150  ##砼梁宽
Hc = 300  ##砼梁高
Lb = 2500  ##砼梁长
##垫块
Hd = 60  ##垫块厚度
##配筋参数
As = 50.24  ##箍筋面积
Al = 113.04  ##压筋面积
Aw = 200.96  ##拉筋面积
Wbh = 30  ##箍筋网宽度方向保护层厚度
Hbh = 30  ##箍筋网高度方向保护层厚度
Lbh = 30  ##纵筋在长度方向保护层厚度
Lst = 60  ##箍筋间距
Htw = 35  ##二层拉筋距底层高度
##网格大小
Me = 50
##荷载加载（N）
Lol = 100000
Lor = 100000
##位移加载（mm
Lll = 13
Llr = 13
##知识点2：加载方式设置（==）
##判断加载方式   0-位移；1-力；2-循环
Jz = 0
##用于计算的CPU线程（2020版线程数-更高版本核心数 注意：性能核心数）
Nc = 32
##用于计算的GPU数量
Ng = 0
##几何运算（以下不需更改）
Ws = Wc - 2 * Wbh  ##箍筋网宽度
Hs = Hc - 2 * Hbh  ##箍筋网高度
Ls = Lb - 2 * Lbh  ##纵筋的长度
Ns = (Ls // Lst) + 1  ##实际箍筋个数取整
Br = (Ls - Lst * (Ns - 1)) / 2  ##避让距离
##砼梁建模
Partb = m.ConstrainedSketch(name='ConBeam-skech', sheetSize=3000.0)
xyCoords = ((0, 0), (Wc / 2, 0), (Wc / 2, Hc), (-Wc / 2, Hc), (-Wc / 2, 0), (0, 0))
for i in range(len(xyCoords) - 1):
    Partb.Line(point1=xyCoords[i], point2=xyCoords[i + 1])

Partbeam = m.Part(name='Part-beam', dimensionality=THREE_D, type=DEFORMABLE_BODY)
Partbeam.BaseSolidExtrude(sketch=Partb, depth=Lb)
##支座处刚性快
SP = m.ConstrainedSketch(name='SteelPlate-skech', sheetSize=200.0)
xyCoords = ((0, 0), (Wc / 2, 0), (Wc / 2, -Hd), (-Wc / 2, -Hd), (-Wc / 2, 0), (0, 0))
for i in range(len(xyCoords) - 1):
    SP.Line(point1=xyCoords[i], point2=xyCoords[i + 1])

SteelPlate = m.Part(name='SteelPlate', dimensionality=THREE_D, type=DEFORMABLE_BODY)
SteelPlate.BaseSolidExtrude(sketch=SP, depth=Wc)
##箍筋建模
St = m.ConstrainedSketch(name='Stirr-skech', sheetSize=3000.0)
xyCoords = ((0, Hbh), (Ws / 2, Hbh), (Ws / 2, Hbh + Hs), (-Ws / 2, Hbh + Hs), (-Ws / 2, Hbh), (0, Hbh))
for i in range(len(xyCoords) - 1):
    St.Line(point1=xyCoords[i], point2=xyCoords[i + 1])

Stirr = m.Part(name='Part-gj', dimensionality=THREE_D, type=DEFORMABLE_BODY)
Stirr.BaseWire(sketch=St)
##纵筋建模
Lo = m.ConstrainedSketch(name='LongStiffener-skech', sheetSize=3000.0)
Lo.Line(point1=(0, 0), point2=(0, Ls))
LongStiffener = m.Part(name='Part-zj', dimensionality=THREE_D, type=DEFORMABLE_BODY)
LongStiffener.BaseWire(sketch=Lo)
##############################################################################
##装配
a = m.rootAssembly
##布置砼梁
part0101 = a.Instance(name='Part-beam', part=Partbeam, dependent=ON)
##布置箍筋
BuzhiGujinx = []
for i in range(0, Ns):
    p = a.Instance(name='gujinx-00{}'.format(i), part=Stirr, dependent=ON)
    BuzhiGujinx.append(p)

for i, item in enumerate(BuzhiGujinx):
    item.translate(vector=(0, 0, Lbh + Br + i * Lst))

##知识点3：箍筋集合（元组）
##布尔箍筋
jihejin = [a.instances['gujinx-000'], a.instances['gujinx-001']]
for i in range(2, Ns):
    jihejin.append(a.instances['gujinx-00{}'.format(i)])

jihejin = tuple(jihejin)
a.InstanceFromBooleanMerge(name='Part-St', instances=jihejin)



##压筋
part0201 = a.Instance(name='yajin-01', part=LongStiffener, dependent=ON)
part0202 = a.Instance(name='yajin-02', part=LongStiffener, dependent=ON)
part0201.translate(vector=(Ws / 2, Hbh + Hs, Lbh))
part0202.translate(vector=(-Ws / 2, Hbh + Hs, Lbh))
a.rotate(instanceList=('yajin-01',), axisPoint=(Ws / 2, Hbh + Hs, Lbh), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.rotate(instanceList=('yajin-02',), axisPoint=(-Ws / 2, Hbh + Hs, Lbh), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
##布尔压筋
a.InstanceFromBooleanMerge(name='Part-zj-c', instances=(a.instances['yajin-01'], a.instances['yajin-02'],), originalInstances=SUPPRESS,
                           domain=GEOMETRY)
##拉筋
part0301 = a.Instance(name='lajin-01', part=LongStiffener, dependent=ON)
part0302 = a.Instance(name='lajin-02', part=LongStiffener, dependent=ON)
part0303 = a.Instance(name='lajin-03', part=LongStiffener, dependent=ON)
part0304 = a.Instance(name='lajin-04', part=LongStiffener, dependent=ON)
part0305 = a.Instance(name='lajin-05', part=LongStiffener, dependent=ON)
part0306 = a.Instance(name='lajin-06', part=LongStiffener, dependent=ON)
part0301.translate(vector=(Ws / 2, Hbh, Lbh))
part0302.translate(vector=(-Ws / 2, Hbh, Lbh))
part0303.translate(vector=(Ws / 2, Hbh + Htw, Lbh))
part0304.translate(vector=(-Ws / 2, Hbh + Htw, Lbh))
part0305.translate(vector=(0, Hbh, Lbh))
part0306.translate(vector=(0, Hbh + Htw, Lbh))
a.rotate(instanceList=('lajin-01',), axisPoint=(Ws / 2, Hbh, Lbh), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.rotate(instanceList=('lajin-02',), axisPoint=(-Ws / 2, Hbh, Lbh), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.rotate(instanceList=('lajin-03',), axisPoint=(Ws / 2, Hbh + Htw, Lbh), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.rotate(instanceList=('lajin-04',), axisPoint=(-Ws / 2, Hbh + Htw, Lbh), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.rotate(instanceList=('lajin-05',), axisPoint=(0, Hbh, Lbh), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.rotate(instanceList=('lajin-06',), axisPoint=(0, Hbh + Htw, Lbh), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
##布尔拉筋
a.InstanceFromBooleanMerge(name='Part-zj-t', instances=(
    a.instances['lajin-01'], a.instances['lajin-02'], a.instances['lajin-03'], a.instances['lajin-04'], a.instances['lajin-05'],
    a.instances['lajin-06'],), originalInstances=SUPPRESS, domain=GEOMETRY)
a.InstanceFromBooleanMerge(name='Part-Rnet', instances=(a.instances['Part-St-1'], a.instances['Part-zj-t-1'], a.instances['Part-zj-c-1'],),
                           originalInstances=SUPPRESS, domain=GEOMETRY)
##布置刚性快下
part0401 = a.Instance(name='SteelPlate-01', part=SteelPlate, dependent=ON)
part0402 = a.Instance(name='SteelPlate-02', part=SteelPlate, dependent=ON)
part0401.translate(vector=(0, 0, 0))
part0402.translate(vector=(0, 0, Lb - Wc))
##布置刚性快上
part0501 = a.Instance(name='SteelPlate-03', part=SteelPlate, dependent=ON)
part0502 = a.Instance(name='SteelPlate-04', part=SteelPlate, dependent=ON)
part0501.translate(vector=(0, Hc + Hd, Lb / 2 - Hc - Hc / 2))
part0502.translate(vector=(0, Hc + Hd, Lb / 2 + Hc))
###########################
##知识点4：切分实体简写（遍历列表）
a = m.rootAssembly
p = m.parts['Part-beam']
fenge = [Wc, Lb - Wc, Lb / 2 - Hc - Hc / 2, Lb / 2 - Hc, Lb / 2 + Hc + Hc / 2, Lb / 2 + Hc]
for i in fenge:
    myPlane1 = p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=int(i))
    myID1 = myPlane1.id
    c = p.cells[:]
    d = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d[myID1], cells=c)

##知识点1：自定义材料库（def函数）
Mat()

##桁架属性
m.TrussSection(name='Part-St', material='HRB400', area=As)
m.TrussSection(name='Part-zj-c', material='HRB400', area=Al)
m.TrussSection(name='Part-zj-t', material='HRB400', area=Aw)
########################################################################################################################################
p = m.parts['Part-beam']
c = p.cells
cells = c.findAt(((0, Hc / 2, 1),), ((0, Hc / 2, Wc + 1),), ((0, Hc / 2, Lb / 3),), ((0, Hc / 2, Lb / 2),),
                 ((0, Hc / 2, 2 * Lb / 3),), ((0, Hc / 2, Lb - 1 - Wc),), ((0, Hc / 2, Lb - 1),))
region = p.Set(cells=cells, name='Part-beam')
p.SectionAssignment(region=region, sectionName='Section-Con', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

p = m.parts['SteelPlate']
c = p.cells
cells = c.findAt(((0, -Hd, Wc / 2),), )
region = p.Set(cells=cells, name='SteelPlate')
p.SectionAssignment(region=region, sectionName='Section-Gang', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
                    thicknessAssignment=FROM_SECTION)
########################################################################################################################################
p = m.parts['Part-Rnet']
xunzhaoGujin = []
for i in range(0, Ns):
    e = p.edges
    e01 = e.findAt(((Ws / 4, Hbh, Lbh + Br + i * Lst),))
    e02 = e.findAt(((-Ws / 4, Hbh, Lbh + Br + i * Lst),))
    e03 = e.findAt(((Ws / 2, Hbh + 1, Lbh + Br + i * Lst),))
    e04 = e.findAt(((-Ws / 2, Hbh + 1, Lbh + Br + i * Lst),))
    e05 = e.findAt(((Ws / 2, Hs - 1, Lbh + Br + i * Lst),))
    e06 = e.findAt(((-Ws / 2, Hs - 1, Lbh + Br + i * Lst),))
    e07 = e.findAt(((0, Hbh + Hs, Lbh + Br + i * Lst),))
    xunzhaoGujin.append(e01 + e02 + e03 + e04 + e05 + e06 + e07)

all_edgeg = xunzhaoGujin[0]
for i in xunzhaoGujin[1:]:
    all_edgeg += i

p.Set(edges=all_edgeg, name='xunzhaoGujin')
xunzhaozongjiny = []
for i in range(0, Ns):
    e = p.edges
    e01 = e.findAt(((Ws / 2, Hbh + Hs, Lbh + Br - 1 + i * Lst),))
    e02 = e.findAt(((-Ws / 2, Hbh + Hs, Lbh + Br - 1 + i * Lst),))
    e03 = e.findAt(((Ws / 2, Hbh + Hs, Lbh + Ls - 1),))
    e04 = e.findAt(((-Ws / 2, Hbh + Hs, Lbh + Ls - 1),))
    xunzhaozongjiny.append(e01 + e02 + e03 + e04)

all_edgeg = xunzhaozongjiny[0]
for i in xunzhaozongjiny[1:]:
    all_edgeg += i

p.Set(edges=all_edgeg, name='xunzhaozongjiny')
xunzhaozongjinl = []
for i in range(0, Ns):
    e = p.edges
    e01 = e.findAt(((Ws / 2, Hbh, Lbh + Br - 1 + i * Lst),))
    e02 = e.findAt(((-Ws / 2, Hbh, Lbh + Br - 1 + i * Lst),))
    e03 = e.findAt(((Ws / 2, Hbh + Htw, Lbh + Br - 1 + i * Lst),))
    e04 = e.findAt(((-Ws / 2, Hbh + Htw, Lbh + Br - 1 + i * Lst),))
    e05 = e.findAt(((0, Hbh, Lbh + Br - 1 + i * Lst),))
    e06 = e.findAt(((0, Hbh + Htw, Lbh + Br),))
    e07 = e.findAt(((Ws / 2, Hbh, Lbh + Ls - 1),))
    e08 = e.findAt(((-Ws / 2, Hbh, Lbh + Ls - 1),))
    e09 = e.findAt(((Ws / 2, Hbh + Htw, Lbh + Ls - 1),))
    e10 = e.findAt(((-Ws / 2, Hbh + Htw, Lbh + Ls - 1),))
    e11 = e.findAt(((0, Hbh, Lbh + Ls - 1),))
    xunzhaozongjinl.append(e01 + e02 + e03 + e04 + e05 + e06 + e07 + e08 + e09 + e10 + e11)

all_edgeg = xunzhaozongjinl[0]
for i in xunzhaozongjinl[1:]:
    all_edgeg += i

p.Set(edges=all_edgeg, name='xunzhaozongjinl')
xunzhaojin = []
for i in range(0, Ns):
    e = p.edges
    e01 = e.findAt(((Ws / 4, Hbh, Lbh + Br + i * Lst),))
    e02 = e.findAt(((-Ws / 4, Hbh, Lbh + Br + i * Lst),))
    e03 = e.findAt(((Ws / 2, Hbh + 1, Lbh + Br + i * Lst),))
    e04 = e.findAt(((-Ws / 2, Hbh + 1, Lbh + Br + i * Lst),))
    e05 = e.findAt(((Ws / 2, Hs - 1, Lbh + Br + i * Lst),))
    e06 = e.findAt(((-Ws / 2, Hs - 1, Lbh + Br + i * Lst),))
    e07 = e.findAt(((0, Hbh + Hs, Lbh + Br + i * Lst),))
    e08 = e.findAt(((Ws / 2, Hbh + Hs, Lbh + Br - 1 + i * Lst),))
    e09 = e.findAt(((-Ws / 2, Hbh + Hs, Lbh + Br - 1 + i * Lst),))
    e10 = e.findAt(((Ws / 2, Hbh + Hs, Lbh + Ls - 1),))
    e11 = e.findAt(((-Ws / 2, Hbh + Hs, Lbh + Ls - 1),))
    e12 = e.findAt(((Ws / 2, Hbh, Lbh + Br - 1 + i * Lst),))
    e13 = e.findAt(((-Ws / 2, Hbh, Lbh + Br - 1 + i * Lst),))
    e14 = e.findAt(((Ws / 2, Hbh + Htw, Lbh + Br - 1 + i * Lst),))
    e15 = e.findAt(((-Ws / 2, Hbh + Htw, Lbh + Br - 1 + i * Lst),))
    e16 = e.findAt(((0, Hbh, Lbh + Br - 1 + i * Lst),))
    e17 = e.findAt(((0, Hbh + Htw, Lbh + Br),))
    e18 = e.findAt(((Ws / 2, Hbh, Lbh + Ls - 1),))
    e19 = e.findAt(((-Ws / 2, Hbh, Lbh + Ls - 1),))
    e20 = e.findAt(((Ws / 2, Hbh + Htw, Lbh + Ls - 1),))
    e21 = e.findAt(((-Ws / 2, Hbh + Htw, Lbh + Ls - 1),))
    e22 = e.findAt(((0, Hbh, Lbh + Ls - 1),))
    xunzhaojin.append(
        e01 + e02 + e03 + e04 + e05 + e06 + e07 + e08 + e09 + e10 + e11 + e12 + e13 + e14 + e15 + e16 + e17 + e18 + e19 + e20 + e21 + e22)

all_edgeg = xunzhaojin[0]
for i in xunzhaojin[1:]:
    all_edgeg += i

p.Set(edges=all_edgeg, name='xunzhaojin')
region = p.sets['xunzhaoGujin']
p.SectionAssignment(region=region, sectionName='Part-St', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
region = p.sets['xunzhaozongjiny']
p.SectionAssignment(region=region, sectionName='Part-zj-c', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
region = p.sets['xunzhaozongjinl']
p.SectionAssignment(region=region, sectionName='Part-zj-t', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
##########################################################################################################################
m.StaticStep(name='Step-1', previous='Initial', maxNumInc=10000, initialInc=0.01, minInc=1e-08)
############################################################################################
s1 = a.instances['SteelPlate-02'].faces
side1Faces1 = s1.findAt(((0, 0.0, Lb - Wc + Wc / 2),), )
a.Surface(side1Faces=side1Faces1, name='Surf-BC-1-G')
s1 = a.instances['SteelPlate-01'].faces
side1Faces1 = s1.findAt(((0, 0.0, Wc / 2),), )
a.Surface(side1Faces=side1Faces1, name='Surf-BC-2-G')
s1 = a.instances['SteelPlate-03'].faces
side1Faces1 = s1.findAt(((0, Hc, Lb / 2 - Hc - Hc / 2 + Wc / 2),), )
a.Surface(side1Faces=side1Faces1, name='Surf-BC-3-G')
s1 = a.instances['SteelPlate-04'].faces
side1Faces1 = s1.findAt(((0, Hc, Lb / 2 + Hc + Wc / 2),), )
a.Surface(side1Faces=side1Faces1, name='Surf-BC-4-G')
s1 = a.instances['Part-beam'].faces
side1Faces1 = s1.findAt(((0, 0.0, Lb - Wc + Wc / 2),))
a.Surface(side1Faces=side1Faces1, name='Surf-BC-1-C')
side1Faces1 = s1.findAt(((0, 0.0, Wc / 2),))
a.Surface(side1Faces=side1Faces1, name='Surf-BC-2-C')
side1Faces1 = s1.findAt(((0, Hc, Lb / 2 - Hc - Hc / 2 + Wc / 2),))
a.Surface(side1Faces=side1Faces1, name='Surf-BC-3-C')
side1Faces1 = s1.findAt(((0, Hc, Lb / 2 + Hc + Wc / 2),))
a.Surface(side1Faces=side1Faces1, name='Surf-BC-4-C')
##知识点5：关键词（master-slave；main-secondary）
a = m.rootAssembly
region1 = a.surfaces['Surf-BC-1-C']
region2 = a.surfaces['Surf-BC-1-G']
m.Tie(name='Constraint-1', master=region1, slave=region2, positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1 = a.surfaces['Surf-BC-2-C']
region2 = a.surfaces['Surf-BC-2-G']
m.Tie(name='Constraint-2', master=region1, slave=region2, positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1 = a.surfaces['Surf-BC-3-C']
region2 = a.surfaces['Surf-BC-3-G']
m.Tie(name='Constraint-3', master=region1, slave=region2, positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1 = a.surfaces['Surf-BC-4-C']
region2 = a.surfaces['Surf-BC-4-G']
m.Tie(name='Constraint-4', master=region1, slave=region2, positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
##########################################################################################################################################
a = m.rootAssembly
region1 = a.instances['Part-Rnet-1'].sets['xunzhaojin']
region2 = a.instances['Part-beam'].sets['Part-beam']
m.EmbeddedRegion(name='Constraint-5', embeddedRegion=region1, hostRegion=region2, weightFactorTolerance=1e-06, absoluteTolerance=0.0,
                 fractionalTolerance=0.05, toleranceMethod=BOTH)
##########################################################################################################################################
a = m.rootAssembly
r1 = a.ReferencePoint(point=(0.0, Hc + Hd, Lb / 2 - Hc - Hc / 2 + Wc / 2))
r2 = a.ReferencePoint(point=(0.0, Hc + Hd, Lb / 2 + Hc + Wc / 2))
r3 = a.ReferencePoint(point=(0.0, -Hd, Wc / 2))
r4 = a.ReferencePoint(point=(0.0, -Hd, Lb - Wc + Wc / 2))
myID1 = r1.id
myID2 = r2.id
myID3 = r3.id
myID4 = r4.id
r1 = a.referencePoints
refPoints1 = (r1[myID1],)
region1 = a.Set(referencePoints=refPoints1, name='m_Set-1')
s1 = a.instances['SteelPlate-03'].faces
side1Faces1 = s1.findAt(((0, Hc + Hd, Lb / 2 - Hc - Hc / 2 + Wc / 2),), )
region2 = a.Surface(side1Faces=side1Faces1, name='s_Surf-9')
m.Coupling(name='Constraint-6', controlPoint=region1, surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, localCsys=None, u1=ON,
           u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
refPoints1 = (r1[myID2],)
region1 = a.Set(referencePoints=refPoints1, name='m_Set-2')
s1 = a.instances['SteelPlate-04'].faces
side1Faces1 = s1.findAt(((0, Hc + Hd, Lb / 2 + Hc + Wc / 2),), )
region2 = a.Surface(side1Faces=side1Faces1, name='s_Surf-10')
m.Coupling(name='Constraint-7', controlPoint=region1, surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, localCsys=None, u1=ON,
           u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
r1 = a.referencePoints
refPoints1 = (r1[myID3],)
region1 = a.Set(referencePoints=refPoints1, name='m_Set-3')
s1 = a.instances['SteelPlate-01'].faces
side1Faces1 = s1.findAt(((0, -Hd, Wc / 2),), )
region2 = a.Surface(side1Faces=side1Faces1, name='s_Surf-11')
m.Coupling(name='Constraint-8', controlPoint=region1, surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, localCsys=None, u1=ON,
           u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
r1 = a.referencePoints
refPoints1 = (r1[myID4],)
region1 = a.Set(referencePoints=refPoints1, name='m_Set-4')
s1 = a.instances['SteelPlate-02'].faces
side1Faces1 = s1.findAt(((0, -Hd, Lb - Wc + Wc / 2),), )
region2 = a.Surface(side1Faces=side1Faces1, name='s_Surf-12')
m.Coupling(name='Constraint-9', controlPoint=region1, surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, localCsys=None, u1=ON,
           u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
############################################################################################
# 约束
a = m.rootAssembly
r1 = a.referencePoints
refPoints1 = (r1[myID3],)
region = a.Set(referencePoints=refPoints1, name='m_Set-3')
m.DisplacementBC(name='BC-1', createStepName='Initial', region=region, u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=SET, ur3=SET, amplitude=UNSET,
                 distributionType=UNIFORM, fieldName='', localCsys=None)
r1 = a.referencePoints
refPoints1 = (r1[myID4],)
region = a.Set(referencePoints=refPoints1, name='m_Set-4')
m.DisplacementBC(name='BC-2', createStepName='Initial', region=region, u1=SET, u2=SET, u3=UNSET, ur1=UNSET, ur2=SET, ur3=SET, amplitude=UNSET,
                 distributionType=UNIFORM, fieldName='', localCsys=None)
##########################################################################################################################################
##知识点2：加载方式设置（==）
##位移加载
if Jz == 0:
    a = m.rootAssembly
    r1 = a.referencePoints
    refPoints1 = (r1[myID1],)
    region = a.Set(referencePoints=refPoints1, name='m_Set-1')
    m.DisplacementBC(name='BC-3', createStepName='Step-1', region=region, u1=UNSET, u2=-Lll, u3=UNSET, ur1=UNSET, ur2=UNSET,
                     ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
    r1 = a.referencePoints
    refPoints1 = (r1[myID2],)
    region = a.Set(referencePoints=refPoints1, name='m_Set-2')
    m.DisplacementBC(name='BC-4', createStepName='Step-1', region=region, u1=UNSET, u2=-Llr, u3=UNSET, ur1=UNSET, ur2=UNSET,
                     ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)

##力加载
if Jz == 1:
    a = m.rootAssembly
    region = a.sets['m_Set-1']
    m.ConcentratedForce(name='Load-1',
                        createStepName='Step-1', region=region, cf2=-int(Lol),
                        distributionType=UNIFORM, field='', localCsys=None)
    region = a.sets['m_Set-2']
    m.ConcentratedForce(name='Load-2',
                        createStepName='Step-1', region=region, cf2=-int(Lor),
                        distributionType=UNIFORM, field='', localCsys=None)

############################################################################################################################################
# 网格
p = m.parts['Part-beam']
p.seedPart(size=Me, deviationFactor=0.1, minSizeFactor=0.1)
p.generateMesh()

elemType1 = mesh.ElemType(elemCode=T3D2, elemLibrary=STANDARD)
p = m.parts['Part-Rnet']
e = p.edges
xunzhaojin = []
for i in range(0, Ns):
    e = p.edges
    e01 = e.findAt(((Ws / 4, Hbh, Lbh + Br + i * Lst),))
    e02 = e.findAt(((-Ws / 4, Hbh, Lbh + Br + i * Lst),))
    e03 = e.findAt(((Ws / 2, Hbh + 1, Lbh + Br + i * Lst),))
    e04 = e.findAt(((-Ws / 2, Hbh + 1, Lbh + Br + i * Lst),))
    e05 = e.findAt(((Ws / 2, Hs - 1, Lbh + Br + i * Lst),))
    e06 = e.findAt(((-Ws / 2, Hs - 1, Lbh + Br + i * Lst),))
    e07 = e.findAt(((0, Hbh + Hs, Lbh + Br + i * Lst),))
    e08 = e.findAt(((Ws / 2, Hbh + Hs, Lbh + Br - 1 + i * Lst),))
    e09 = e.findAt(((-Ws / 2, Hbh + Hs, Lbh + Br - 1 + i * Lst),))
    e10 = e.findAt(((Ws / 2, Hbh + Hs, Lbh + Ls - 1),))
    e11 = e.findAt(((-Ws / 2, Hbh + Hs, Lbh + Ls - 1),))
    e12 = e.findAt(((Ws / 2, Hbh, Lbh + Br - 1 + i * Lst),))
    e13 = e.findAt(((-Ws / 2, Hbh, Lbh + Br - 1 + i * Lst),))
    e14 = e.findAt(((Ws / 2, Hbh + Htw, Lbh + Br - 1 + i * Lst),))
    e15 = e.findAt(((-Ws / 2, Hbh + Htw, Lbh + Br - 1 + i * Lst),))
    e16 = e.findAt(((0, Hbh, Lbh + Br - 1 + i * Lst),))
    e17 = e.findAt(((0, Hbh + Htw, Lbh + Br),))
    e18 = e.findAt(((Ws / 2, Hbh, Lbh + Ls - 1),))
    e19 = e.findAt(((-Ws / 2, Hbh, Lbh + Ls - 1),))
    e20 = e.findAt(((Ws / 2, Hbh + Htw, Lbh + Ls - 1),))
    e21 = e.findAt(((-Ws / 2, Hbh + Htw, Lbh + Ls - 1),))
    e22 = e.findAt(((0, Hbh, Lbh + Ls - 1),))
    xunzhaojin.append(
        e01 + e02 + e03 + e04 + e05 + e06 + e07 + e08 + e09 + e10 + e11 + e12 + e13 + e14 + e15 + e16 + e17 + e18 + e19 + e20 + e21 + e22)

all_edgeg = xunzhaojin[0]
for i in xunzhaojin[1:]:
    all_edgeg += i

pickedRegions = (all_edgeg,)
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,))
p.seedPart(size=Me, deviationFactor=0.1, minSizeFactor=0.1)
p.generateMesh()

p = m.parts['SteelPlate']
p.seedPart(size=Me, deviationFactor=0.1, minSizeFactor=0.1)
p.generateMesh()
############################################################################################################################################
# 定义输出场
m.fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 'CDISP', 'DAMAGEC', 'DAMAGET'),
                                              timeInterval=0.01)
regionDef = m.rootAssembly.sets['m_Set-1']
m.FieldOutputRequest(name='F-Output-2', createStepName='Step-1', variables=('RT',), timeInterval=0.01, region=regionDef, sectionPoints=DEFAULT,
                     rebar=EXCLUDE)
############################################################################################################################################
# 提交工作
Time_sta_run = time.time()
mdb.Job(name='Job-Cb', model='Model-CB', description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF,
        contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', resultsFormat=ODB, multiprocessingMode=THREADS, numCpus=Nc, numDomains=Nc,
        numGPUs=Ng)
mdb.jobs['Job-Cb'].submit(consistencyChecking=OFF)
mdb.jobs['Job-Cb'].waitForCompletion()
########################################################################################################################
Time_end_run = time.time()  # 记录结束时间
Time_Run = (Time_end_run - Time_sta_run)  # 计算的时间差为程序的执行时间，单位为秒
print('Run(min)=', Time_Run)  # 打印计算时间
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)  # 发出声音
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))