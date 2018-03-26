# -*- coding: UTF-8 -*-
import time
from datetime import timedelta,date
import os
import collections
import platform 
_version = platform.python_version()


try:
	import openpyxl
except:
	try:
		if(int(_version[:1])<3):
			os.system("pip install openpyxl")
		else:
			os.system("pip3 install openpyxl")

		import openpyxl
	except:
		print '请先安装pip,或手动安装openpyxl'
		exit(1)

from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import NamedStyle, Font, Border, Side

import copy
def get_day_of_day(n=0):
    if(n<0):
        n = abs(n)
        return date.today()-timedelta(days=n)
    else:
        return date.today()+timedelta(days=n)

todayWeek = date.today().strftime('%w')

thisWeek = {}

def addWeek(offset):
	o = offset > 0 if 1 else -1;
	for i in range(abs(offset)):
		time = get_day_of_day(i+o)
		thisWeek[time.strftime('%Y-%m-%d')] = time.strftime('%w')


afterOffset = 5 - int(todayWeek) 
beforeOffet = 1 - int(todayWeek) 

thisWeek[date.today().strftime('%Y-%m-%d')] = todayWeek #今天
addWeek(afterOffset)
addWeek(beforeOffet)
#获取这一周的时间和星期

nextWeek = collections.OrderedDict()

def addNextTime():
	for i in range(5):
		time = get_day_of_day(afterOffset+3+i)
		nextWeek[time.strftime('%Y-%m-%d')] = time.strftime('%w')

addNextTime()

# print nextWeek

def date_compare(item1, item2):
    t1 = time.mktime(time.strptime(item1, '%Y-%m-%d'))
    t2 = time.mktime(time.strptime(item2, '%Y-%m-%d'))
    if t1 < t2:
        return -1
    elif t1 > t2:
        return 1
    else:
        return 0

weekOrderSet = sorted(thisWeek.keys(), date_compare)

# print weekOrderSet
# print thisWeek


question = collections.OrderedDict()
question['name'] = ''
question['companyName'] = ''
question['position'] = ''

if os.path.exists('./setting.txt'):
	f = open('./setting.txt', 'r')
	for line in f.readlines():
		item = line.strip().split(':')
		if(item[0] in question):
			question[item[0]] = item[1];
	f.close()

print question

questionMap = {
	'name':'请输入你的名字:',
	'companyName':'请输入你的公司名:',
	'position':'请输入你的职位:'
}
def set():
	for i in question:
		ans = raw_input(questionMap[i])
		question[i] = ans


def save():
	with open("./setting.txt","w") as fs:
		for i in question:
			fs.write("%s:%s\n" % (i,question[i]))

def checkSet():
	for i in question:
		if(question[i].strip() == ''):
			return 'error'


def readFile():
	wb = load_workbook('./template.xlsx')
	oldSheet = wb['Sheet1']
	oldSheet.title = 'template'
	# wb.create_sheet('fork',0)
	# newSheet = wb['fork']
	# print newSheet

	
	wb.save('output/gg.xlsx')

def run():
	firstSelect = raw_input('请选择要做的事(s:设置, g:开始生成周报):')
	if(firstSelect == 's'):
		set()
		print '设置完毕'
		save()
		return run()
	elif(firstSelect == 'g'):
		if(checkSet() == 'error'):
			print '请先设置个人信息'
			return run() # TODO 后续优化 只需输入未填写的信息
		else:
			print '模板读取中.. 请确认当前文件夹下有 template.xlsx 文件'
			readFile()
			# p = list() 
			# for row in range(sheet.nrows):
			# 	for col in range(sheet.ncols):
			# 		try:
			# 			if(sheet.cell(row,col).value.strip() == ''):
			# 				print 'null'
			# 			else:
			# 				print sheet.cell(row,col).value
			# 		except:
			# 			print 'number'
			# 			print sheet.cell(row,col).value
			# for row in range(sheet.nrows):  
   #          	# row_data = []
			# 	for col in range(sheet.ncols):  
			# 		cel = sheet.cell(row, col)  
			# 		val = cel.value 
			# 		print '键:'+str(cel)+'值:'+str(val)

	else:
		print '请重新选择'
		return run()

run()