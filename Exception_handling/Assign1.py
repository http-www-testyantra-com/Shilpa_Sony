#5 scenarios handling exceptions:
import xlrd
import xlwt
from selenium import webdriver
#index error exception

def test_Excel():
    wb = xlwt.Workbook()
    sh = wb.add_sheet("Test case1")
    sh.write(0,0,"Username")
    wb.save("Workbook.xls")

def test_Read():
    try:
        wo =xlrd.open_workbook("Workbook.xls")
        s = wo.sheet_by_name("Test case1")
        text = s.cell_value(0,1)
        print(text)
    except IndexError(Exception) as e:
        print(e)
        print("Exception handled")

def test_Operate():
    test_Operate()
    print("this is test operate method")

if __name__ == '__main__':
    test_Excel()