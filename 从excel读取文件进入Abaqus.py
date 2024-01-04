# 从excel 读取文件进入Abaqus
import numpy as np
import xlrd
from abaqus import *
from abaqusConstants import *
from caeModules import *
import os
import numpy as np
import math
import matplotlib.pyplot as plt
from visualization import *
from odbAccess import *
import xlwt

session.journalOptions.setValues(replayGeometry=INDEX, recoverGeometry=INDEX)
session.journalOptions.setValues(recoverGeometry=COORDINATE, replayGeometry=COORDINATE)
Mdb()

# 读入txt数据
myModel = mdb.Model(name='sphere')
b = np.loadtxt('coordinates.txt', delimiter=',', dtype=np.float32)

for i in range(len(b)):
    mySketch = myModel.ConstrainedSketch(name='sphereProfile', sheetSize=0.2)
    mySketch.ArcByCenterEnds(center=(b[i][0], b[i][1]), direction = CLOCKWISE, point1 =(b[i][0], b[i][1]+b[i][3]), point2 =(b[i][0], b[i][1]-b[i][3]) )
    mySketch.Line(point1 =(b[i][0], b[i][1]+b[i][3]), point2 =(b[i][0], b[i][1]-b[i][3]) )
    myConstructionLine = mySketch.ConstructionLine(point1 =(b[i][0], b[i][1]+b[i][3]), point2=(b[i][0], b[i][1]-b[i][3]) )
    myBeam = myModel.Part(name='sphere'+str(i), dimensionality=THREE_D, type=DEFORMABLE_BODY)
    myPart = myBeam.BaseSolidRevolve(angle=360.0, flipRevolveDirection=OFF, sketch=mySketch)
    myModel.rootAssembly.DatumCsysByTwoLines(CARTESIAN)
    myModel.rootAssembly.Instance(dependent=ON, name='sphere'+str(i), part=myBeam)
    myModel.rootAssembly.translate(instanceList=('sphere'+str(i),), vector = (0.0, 0.0, b[i][2]))

data = xlrd.open_workbook('coordinates.xls')
# data.sheet_names()
# 通过名称选择表单
table = data.sheet_names('')

table = data.sheets()[0]
# 获得表格的行数和列数
nrows = table.nrows
ncols = table.ncols
data_list = []
data_list.extend(table.row_values(0))

