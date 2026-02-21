import datetime
import pytz 	# -used for timezones

#aware and naive datetime objects. 
#aware datetimes take into account timezones, naive datetimes do not.


'''Date'''
bday = datetime.date(2005, 10, 15)		#only integers, no zfill
	#.date(year, month, day). all arguments required
print(f'birthday is {bday}')

tday = datetime.date.today()
print(f'today is {tday}')

# print(tday.weekday(), tday.isoweekday())

#weekday: monday - 0, sunday - 6
#isoweekday: monday - 1, sunday - 7


'''Timedelta'''
# td = datetime.timedelta(days=7)
	#arguments can be days, seconds, months etc
# print(tday + td) 	#timedelta adds no. of days (7) to 'tday'

#date + date = timedelta
#date +/- timedelta = date

n_bday = datetime.date(tday.year, bday.month, bday.day)
days_to_bday = n_bday - tday
print(f'{days_to_bday.days} days till my birthday')
	#subtracted a date from a date, producing a timedelta
	#.year returns year attribute of a datetime. same for .month and.day
	#note using .year, .month, .day and related methods returns integer value

# print(days_to_bday.total_seconds())
	#converts days to seconds


'''Time'''
t = datetime.time(6, 45, 0, 0) 		#only integers, no zfill
	#.time(hours, minutes, seconds, microseconds, tzinfo)
	#arguments not required, default 0

print(f'time: {t}')


'''Datetime - suggested to just always use this'''
dt = datetime.datetime(2000,1,1,6,45,0,0) 		#only integers, no zfill
	#.datetime(year, month, day, hours, minutes, sec, microsec, tzinfo)
	#year, month, and day arguments required

print(f'datetime: {dt}')
	#more methods can be passed through datetime object
	#date, time, as well as hour, year etc 
	#friendly interaction with timedeltas as well


'''Timezones -- aware datetime objects'''
dt_timezone = datetime.datetime.now(tz=pytz.UTC)
	#timezone argument passed, with pytz module
print(dt_timezone)

dt_local = dt_timezone.astimezone(pytz.timezone('Asia/Singapore'))
	#.astimezone() is used to change timezones. 
	#refer to zoneinfo under pytz package folder to find timezone
print(dt_local)

#only datetime objects can have .astimezone passed through it

# print(dt_local.isoformat())
	#separates time from date with T


'''Conversion of string to datetime'''
date_str = 'October 15, 2005'
date_dt = datetime.datetime.strptime(date_str, '%B %d, %Y')
	#.strptime() inteprets a string, format must be provided
	#.strftime converts datetime to a string, format must be provided
print(date_dt)




'''
FORMAT CODE LIST
The table below shows all the codes that you can pass to the strftime() method.

Directive	Meaning	Example
%a	Abbreviated weekday name.	Sun, Mon, ...
%A	Full weekday name.	Sunday, Monday, ...
%w	Weekday as a decimal number.	0, 1, ..., 6
%d	Day of the month as a zero-padded decimal.	01, 02, ..., 31
%-d	Day of the month as a decimal number.	1, 2, ..., 30
%b	Abbreviated month name.	Jan, Feb, ..., Dec
%B	Full month name.	January, February, ...
%m	Month as a zero-padded decimal number.	01, 02, ..., 12
%-m	Month as a decimal number.	1, 2, ..., 12
%y	Year without century as a zero-padded decimal number.	00, 01, ..., 99
%-y	Year without century as a decimal number.	0, 1, ..., 99
%Y	Year with century as a decimal number.	2013, 2019 etc.
%H	Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23
%-H	Hour (24-hour clock) as a decimal number.	0, 1, ..., 23
%I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12
%-I	Hour (12-hour clock) as a decimal number.	1, 2, ... 12
%p	Locale’s AM or PM.	AM, PM
%M	Minute as a zero-padded decimal number.	00, 01, ..., 59
%-M	Minute as a decimal number.	0, 1, ..., 59
%S	Second as a zero-padded decimal number.	00, 01, ..., 59
%-S	Second as a decimal number.	0, 1, ..., 59
%f	Microsecond as a decimal number, zero-padded on the left.	000000 - 999999
%z	UTC offset in the form +HHMM or -HHMM.	 
%Z	Time zone name.	 
%j	Day of the year as a zero-padded decimal number.	001, 002, ..., 366
%-j	Day of the year as a decimal number.	1, 2, ..., 366
%U	Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.	00, 01, ..., 53
%W	Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.	00, 01, ..., 53
%c	Locale’s appropriate date and time representation.	Mon Sep 30 07:06:05 2013
%x	Locale’s appropriate date representation.	09/30/13
%X	Locale’s appropriate time representation.	07:06:05
%%	A literal '%' character.	%
'''