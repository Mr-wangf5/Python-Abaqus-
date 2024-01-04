import xlrd
import xlwt
from pymysql import *

# data = xlrd.open_workbook('data1.xlsx')   # filename 路径+表名称
# print(data.sheet_loaded(0))               # 判断当前工作表是否加载
# data.unload_sheet(0)                      # 卸载第一个工作表
# print(data.sheets())                        # 输出所有工作表
# print(data.sheets()[0])                     # 通过索引获取对应工作表
# print(data.sheet_by_index(0))              # 通过索引0获取对应工作表
# print(data.sheet_by_name('Sheet1'))         # 通过sheetname获取对应工作表
# print(data.sheet_names())                   # 获取所有sheetname
# print(data.nsheets)                         # 返回excel中工作表数量

# 操作excel行
# sheet = data.sheet_by_index(0)         # 获取第一个工作表
# print(sheet.nrows)         # 获取当前excel工作表下的有效行数
# print(sheet.row(0))        # 该行单元格对象组成的列表
# print(sheet.row_types(0))   # 获取指定行单元格对象的数据类型
# print(sheet.row(0)[2].value)      # 获取1行3单元格的value
# print(sheet.row_values(1))      # 获取指定行单元格的value
# print(sheet.row_len(1))      # 获取行单元格的长度

# 操作excel列
# sheet = data.sheet_by_index(0)
# print(sheet.ncols)           # 获取当前excel工作表下的有效列数
# print(sheet.col(0))        # 该列单元格对象组成的列表
# print(sheet.col(0)[2].value)      # 获取3行1列单元格的value
# print(sheet.col_values(1))      # 获取指定列单元格的value
# print(sheet.col_types(0))   # 获取指定列单元格对象的数据类型
# print(sheet.col_len(0))      # 获取列单元格的长度

# 操作excel单元格
# sheet = data.sheet_by_index(0)
# print(sheet.cell(1, 2))           # 获取2行3列单元格value
# print(sheet.cell_types(1, 2))      # 获取2行3列单元格数据类型
# print(sheet.cell(1, 2).ctype)
# print(sheet.cell(1, 2).value)           # 获取2行3列单元格value
# print(sheet.cell_value(1, 2))



# 写入excel单元格
titlestyle = xlwt.XFStyle()    # 初始化样式
titlefont = xlwt.Font()
titlefont.name='宋体'
titlefont.bold = True     # 加粗
titlefont.height = 11*20   # 字号
titlefont.colour_index = 0x08       # 设置字体颜色
titlestyle.font = titlefont

# 单元格边框
borders = xlwt.Borders
borders.right=xlwt.Borders.DASHED
borders.bottom=xlwt.Borders.DOTTED
titlestyle.borders = borders

# 背景颜色
datastyle = xlwt.XFStyle()
bgcolor = xlwt.Pattern()
bgcolor.pattern=xlwt.Pattern.SOLID_PATTERN
bgcolor.pattern_fore_colour = 22        # 背景颜色灰色
datastyle.pattern=bgcolor

# 单元格对齐方式
cellalign = xlwt.Alignment()        # 实例化
cellalign.horz = 0x02
cellalign.wrap = 0x01
titlestyle.alignment = cellalign


# 创建工作簿
wb = xlwt.Workbook()
# 创建工作表
ws = wb.add_sheet('CNY')
# 在工作表填充数据
ws.write_merge(0, 1, 0, 5, '2019年货币兑换表', titlestyle)
# 写入货币数据
data = (('1', '2', '3'), (1, 2, 3), (4, 2, 3))
for i, item in enumerate(data):      # enumerate 用于将data组合为索引, i,j为索引
    for j, val in enumerate(item):
        if j ==0:
            ws.write(i+2, j, val, datastyle)
        else:
            ws.write(i+2, j, val)

# 创建第二个工作表
wsimage = wb.add_sheet('image')
# 写入图片
wsimage.insert_bitmap('2017.gif', 0, 0)

# 保存
wb.save('2019-CNY.xls')

# Excel导入试题到数据库操作布置
# 通过xlrd 模块读取Excel数据
data = xlrd.open_workbook('data2.xlsx')
sheet =data.sheet_by_index(0)   # 获取工作表
# 通过pymysql模块连接数据库
questionList = []    # 构建试题列表

# 试题类
class Question:
    pass
for i in range(sheet.nrows):
    if i >1:
        obj = Question()  # 构建试题对象
        obj.subject = sheet.cell(i, 1).value    # 题目
        obj.QuestionType = sheet.cell(i, 2).value      # 题型
        obj.optionA = sheet.cell(i, 3).value
        obj.optionB = sheet.cell(i, 4).value
        obj.optionC = sheet.cell(i, 5).value
        obj.optionD = sheet.cell(i, 6).value
        obj.score = sheet.cell(i, 7).value    # 分值
        obj.answer = sheet.cell(i, 8).value      # 正确答案
        questionList.append(obj)

print(questionList)

# 导入操作
# 1.链接到数据库
db = dbhelper('127.0.0.1', 3306, 'root', '123456', 'test')

# 插入语句

sql = 'insert into qusetion(subject, QuestionType, optionA, optionB, optionC, optionD, score, answer) VALUES (%s, %s, %s, %s, %s, %s)
val = []      # 空列表来存储元组数据
for item in questionList:
    val.append(item.subject, item.QuestionType, item.optionA, item.optionB, item.optionC, item.optionD, item.score, item.answer)

db.executemanydata(sql, val)
# 组装数据、执行插入操作

# 关闭数据库连接