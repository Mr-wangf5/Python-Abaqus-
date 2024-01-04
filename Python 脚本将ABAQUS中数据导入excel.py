from abaqus import *
from abaqusConstants import *
from visualization import *
from odbAccess import *
import xlwt
odb = openOdb(path='ODBName' +'.ODB')
wbkName = 'xxx'             # 创建表格文件名
wbk = xlwt.Workbook()       # 创建空表格
sheet = wbk.add_sheet('sheet1')         # 创建sheet1
myAssembly = odb.rootAssembly
frameRepository = odb.steps['Step-1'].frames
RefPointSet = myAssembly.nodeSets['RF1']
for i in range(len(frameRepository)):
    # 提取参考点RF1在Y方向支反力
    RForce = frameRepository[i].fieldOutputs['RF']
    RefPointRForce = RForce.getSubset(region=RefPointSet)
    RForceValues = RefPointRForce.values
    RF_2 = RForceValues[0].data[1]

    # 提取参考点RF1的位移量
    displacement = frameRepository[i].fieldOutputs['U']
    RefPointDisp = displacement.getSubset(region=RefPointSet)
    DispValues = RefPointDisp.values
    Disp = DispValues[0].data[1]

    # 将结果写入相应的行和列
    sheet.write(i, 0, round(Disp, 3))
    sheet.write(i, 1, round(RF_2, 2))

wbk.save(wbkName+'.xls')          # 保存结果
