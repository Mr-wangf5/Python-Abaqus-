# python后处理提取变形前后单位体积及对应编号
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

session.journalOptions.setValues(replayGeometry=INDEX,recoverGeometry=INSIDE)
session.journalOptions.setValues(recoverGeometry=COORDINATE, replayGeometry=COORDINATE)

Modelname = 'TestModel'
Partname = 'Part-1'
Instancename = 'Part-1-1'
Workdirectory = "F:\\temp\substructure\\TestModel"
Jobname = "TestModel"
os.chdir(r"" + Workdirectory)
ElemNumExtra = 1                  # 需要提取的节点编号

Modelname, Instancename, odbname=getInputs(
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
    denode = denode + 1

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

GetInfo = np.zeros(len(element), 2)
Maxframs = 200          # 最大帧数
Numframes = len(odb.steps['Step-1'].frames)          # 该荷载步的帧数
DispNodeNum = np.zeros((Maxframs, len(element),  2))

# odb.rootAssembly.instances[Instancename].elementSets['WHOLE']

ModelVol = 0.0
for i in range(len(odb.steps['Step-1'].frame[0].fieldOutputs['EVOL'].values)):
    ModelVol = ModelVol + odb.steps['Step-1'].frame[i].fieldOutputs['EVOL'].data        # data 为体积

