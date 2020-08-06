import xlrd
import openpyxl
# li1表示需要被修改的表格，li2表示模板表格
li1=[]
li2=[]
def get_data(file,li_all,sheet):
    book = xlrd.open_workbook(file)
    sheet = book.sheets()[sheet]
    # 按行读取文件>>nrows
    for j in range(sheet.nrows):
        li=sheet.row_values(j)
        # print(li)
        li_all.append(li)
get_data(r'C:\Users\槐老板\Desktop\假数据.xlsx',li1,0)
get_data(r'C:\Users\槐老板\Desktop\假数据.xlsx',li2,1)
# print(li2)
# print(li1)
for i in range(1,len(li2)):#模板层循环，range函数区间左闭右开，如果只有一个参数，默认从0开始。
    for j in range(1,len(li1)):#修改数据层循环
            if li2[i][3]==li1[j][0]:#如果模板的参数在被修改数据表格里面
                file = openpyxl.load_workbook(r'C:\Users\槐老板\Desktop\假数据.xlsx')
                # 打开表格1
                sheet=file.worksheets[0]
                # 修改表格1的数据
                # 注意这里的J是列表的索引，从0开始，而修改xlsx表格索引从1开始，所以需要加1
                sheet.cell(j+1,3,li2[i][4])
                # 保存数据
                file.save(r'C:\Users\槐老板\Desktop\假数据.xlsx')

