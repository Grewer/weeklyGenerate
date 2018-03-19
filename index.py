# -*- coding: UTF-8 -*-
import time
from datetime import timedelta,date
import os
import collections

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


# name = raw_input('请输入用户名：')
# 第一次需要输入,后续读取文件


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
   	# read
else:
	f = open('./setting.txt', 'wr')
	print 'daixie'
	# touch

print question

firstSelect = raw_input('请选择要做的事(s:设置, g:开始生成周报):')
questionMap = {
	'name':'请输入你的名字:',
	'companyName':'请输入你的公司名:',
	'position':'请输入你的职位:'
}

if(firstSelect == 's'):
	print '设置'
	for i in question:
		ans = raw_input(questionMap[i])
		question[i] = ans
	print '已设置完毕'
	
else:
	print '生成'


