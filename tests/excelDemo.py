import openpyxl

book = openpyxl.load_workbook("/Users/ntalesha/Desktop/TESTING.xlsx")
sheet = book.active
cell = sheet.cell(row=1,column=2)
print(cell.value)
