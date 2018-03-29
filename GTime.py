# -*- coding: UTF-8 -*-
import time
from datetime import timedelta,date
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
	for i in range(abs(offset)):
		if offset >0:
			o = 1
		else:
			o = -1
			i = -i
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

print 'nextWeek:',nextWeek
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


timeList = {
	'month':str(date.today().month)
}

def splitDay(day):
	daySet = day.split('-')
	return '%s年%s月%s日' % (daySet[0],daySet[1],daySet[2])

timeList['thisWeekStr'] = '%s-%s' % (splitDay(weekOrderSet[0]),splitDay(weekOrderSet[-1]))


for index,day in enumerate(weekOrderSet):
	m = {0:'Mon',1:'Tues',2:'Wed',3:'Thur',4:'Fri'}[index]

	print m
	
# 待优化 成一个函数 可以删除排序


timeList['thisWeek'] = {'test':1}


print 'timeList:',timeList

def outTime():
	print 'time.py outTime func'
	return timeList
