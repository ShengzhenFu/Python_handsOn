import xlwt
from datetime import datetime

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
i = 0
j = 0
for i in range(0,3):
    ws.write(i, j, 1)
    j+=1
    ws.write(i,j,2)
    j+=1
    ws.write(i,j,3)
    i+=1
    j = 0

#ws.write(0, 0, 1234.56, style0)
#ws.write(1, 0, datetime.now(), style1)
#ws.write(2, 0, 1)
#ws.write(2, 1, 1)
#ws.write(2, 2, xlwt.Formula("A3+B3"))
wb.save('example.xls')