import numpy as np
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
from tkinter import *


session.journalOptions.setValues(replayGeometry=INDEX, recoverGeometry=INDEX)
session.journalOptions.setValues(recoverGeometry=COORDINATE, replayGeometry=COORDINATE)

Modelname = 'TestModel'
Partname = 'Part-1'
Instancename = 'Part-1-1'
Workdirectory = "F:\\temp\substructure\\TestModel"
Jobname = "TestModel"
os.chdir(r"" + Workdirectory)
ElemNumExtra = 1                  # 需要提取的节点编号

Modelname, Instancename, odbname = getInputs(
    fields=(('Modelname', Modelname), ('Instancename', Instancename), ('odbname', Workdirectory + '\\'+Jobname+'.odb')),
    Label="Enter information",
    dialogTitle="Get information.")


odb = openOdb(path=odbname)

# 提取所有节点的编号以及xyz坐标
eqs = 0.000000001
node = mdb.models[Modelname].rootAssembly.instances[Instancename].nodes
NodeNum = np.zeros(len(node), 4)
denode = 0
for i in range(len(node)):
    x = node[i].coordinates[0]
    y = node[i].coordinates[1]
    z = node[i].coordinates[2]
    NodeNum[denode][0] = node[i].label
    NodeNum[denode][1] = x
    NodeNum[denode][2] = y
    NodeNum[denode][3] = z
    denode = denode +1

# 提出所有单元以及该单元所有节点的编号
element = mdb.models[Modelname].rootAssembly.instances[Instancename].elements

ElemNum = []
for i in range(len(element)):
    ENum = [i]
    for j in element[i].connectivity:
        x = node[j].coordinates[0]
        y = node[j].coordinates[1]
        z = node[j].coordinates[2]
    if len(ENum) == 9:
        ElemNum.append(ENum)

for i in range(len(ElemNum)):
    for j in range(9):
        ElemNum[i][j] = ElemNum[i][j] +1

GetInfo = np.zeros((1000, 40))
Maxframs = 200          # 最大帧数
Numframes = len(odb.steps['Step-1'].frames)          # 该荷载步的帧数
DispNodeNum = np.zeros((len(node), Maxframs, 4))     # 用来储存单元节点的位移

MaxX = np.zeros((len(node), Maxframs, 1))         # 储存所有节点x位移的最大值，并记录在第几帧
MaxY = np.zeros((len(node), Maxframs, 2))         # 储存所有节点y位移的最大值，并记录在第几帧
MaxZ = np.zeros((len(node), Maxframs, 3))         # 储存所有节点z位移的最大值，并记录在第几帧
MaxXValue = 0.0
MaxYValue = 0.0
MaxZValue = 0.0

# 输出每个节点所有帧数的位移最大值
for kf in range(len(node)):
    # 提取所有变形后节点的编号及xyz坐标
    for i in element[ElemNumExtra -1].connectivity:
        DispNodeNum[i][kf][0] = NodeNum[i][0]
        DispNodeNum[i][kf][1] = odb.steps['Step-1'].frames[kf].fieldoutputs['u'].getSubset(position=NODAL).values[int(NodeNum[i][0]-1)].data[0]
        DispNodeNum[i][kf][2] = odb.steps['Step-1'].frames[kf].fieldoutputs['u'].getSubset(position=NODAL).values[int(NodeNum[i][0]-1)].data[1]
        DispNodeNum[i][kf][3] = odb.steps['Step-1'].frames[kf].fieldoutputs['u'].getSubset(position=NODAL).values[int(NodeNum[i][0]-1)].data[2]
        if kf == 0:
            MaxXValue = DispNodeNum[i][kf][1]
        else:
            if MaxXValue <= DispNodeNum[i][kf][1]:
                MaxXValue = DispNodeNum[i][kf][1]
            if MaxYValue <= DispNodeNum[i][kf][2]:
                MaxXValue = DispNodeNum[i][kf][2]
            if MaxZValue <= DispNodeNum[i][kf][3]:
                MaxXValue = DispNodeNum[i][kf][3]


