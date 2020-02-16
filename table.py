from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def func_s(x):
	S_pod = [5,8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11]
	return S_pod[(S_pod.index(x) + 1) % 16]

wb = Workbook()
dest_filename = 'new_wb.xlsx'
ws1 = wb.active

for i in range(16):
	row_temp = []
	for j in range(16):
		counter = 0
		for itera in range(16):
			if(func_s(itera ^ i) == func_s(itera) ^ j):
				counter+=1
		if counter > 0:
			print(i, j,',',bin(i).count("1") + bin(j).count("1"), ',', counter / 16)
		row_temp.append(counter)
	ws1.append(row_temp)		

wb.save(filename = dest_filename)