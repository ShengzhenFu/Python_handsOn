import xml.dom.minidom
import sys
import glob
import os
import xlwt
from datetime import datetime

def traversalDir_XMLFile(path):
    # check if file exists
    if (os.path.exists(path)):
        f = glob.glob(path + '\\*.xml')

        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                             num_format_str='#,##0.00')
        style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

        wb = xlwt.Workbook()
        ws = wb.add_sheet('A Test Sheet')
        i = 1
        ws.write(0, 0, 'AutoHold xml file', style0)
        ws.write(0, 1, 'Lot ID', style0)
        ws.write(0, 2, 'DataStatus', style0)
        ws.write(0, 3, 'LotDecision',style0)
        ws.write(0, 4, 'ErrorMessage', style0)
        ws.write(0, 5, 'OTWF process Timestamp', style0)

        for file in f :
            #print(file)
            # open xml file
            dom = xml.dom.minidom.parse(file)
            # get element
            root = dom.documentElement
            #get attribute key
            childs = root.getElementsByTagName('LotStatus')
            for child in childs:
                if(child.nodeType == 1):

                        ws.write(i,0,file)
                        ws.write(i,1,child.getAttribute("Lot"))
                        ws.write(i,2,child.getAttribute("DataStatus"))
                        ws.write(i,3,child.getAttribute("LotDecision"))
                        ws.write(i,4,child.getAttribute("ErrorMessage"))
                        ws.write(i,5,child.getAttribute("Timestamp"))
                        i+=1
                        wb.save('test.xls')
traversalDir_XMLFile('F:\\O+\\customers\\NXP\ATTJ\\quarantine_report_20Nov_To_1Dec')
