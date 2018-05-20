# -*- coding: UTF-8 -*-
import time
from datetime import timedelta,date
import collections


todayWeek = date.today().strftime('%w') # 今天是周几  0:周末 1:周一 ... 6:周六

friday = None

def get_day_of_day(n=0):
	if(not friday is None):
		today = friday
	else:
		today = date.today()

	if(n<0):
		n = abs(n)
		return today-timedelta(days=n)
	else:
		return today+timedelta(days=n)


if(int(todayWeek)>=5 or todayWeek == '0'):
	# 周末或周五周6️六
	if todayWeek == '5':
		friday = date.today()
	elif todayWeek == '0':
		friday = get_day_of_day(-2)
	else:
		friday = get_day_of_day(-1)
	todayWeek = '5'
else:
	print '请在周末或周五使用'
	exit(1)

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

thisWeek[friday.strftime('%Y-%m-%d')] = todayWeek #今天

addWeek(afterOffset)
addWeek(beforeOffet)
#获取这一周的时间和星期


nextWeek = collections.OrderedDict()

def addNextTime():
	for i in range(5):
		time = get_day_of_day(afterOffset+3+i)
		nextWeek[time.strftime('%Y-%m-%d')] = time.strftime('%w')

addNextTime()

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
	'month':str(friday.month)
}

def splitDay(day):
	daySet = day.split('-')
	return '%s年%s月%s日' % (daySet[0],daySet[1],daySet[2])

timeList['thisWeekStr'] = '%s-%s' % (splitDay(weekOrderSet[0]),splitDay(weekOrderSet[-1]))


WeekMapSet = {
	'Mon':'一',
	'Tues':'二',
	'Wed':'三',
	'Thur':'四',
	'Fri':'五'
}


def getWeekMap(weekSet):
	midSet = {}
	for day in weekSet:
		m = {'1':'Mon','2':'Tues','3':'Wed','4':'Thur','5':'Fri'}[weekSet[day]]
		midSet[m] = '星期'+WeekMapSet[m]
		midSet[m+'Date'] = day
	return midSet


timeList['thisWeek'] = getWeekMap(thisWeek)
timeList['nextWeek'] = getWeekMap(nextWeek)


def outTime():
	return timeList
