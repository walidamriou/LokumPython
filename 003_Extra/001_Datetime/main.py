"""
 ******************************************************************** 

  LokumPython
  To Learn Python Programming Language with small programs examples
  Project Website: LokumPython.walidamriou.com
  Github: https://github.com/walidamriou/LokumPython

  Copyright CC 2020 Walid Amriou
  This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
   
  Last update: July 2020

 ******************************************************************** 
"""

import datetime

# Current Date and Time
current_date_time = datetime.datetime.now()
print(current_date_time)
print(current_date_time.year)
print(current_date_time.month)
print(current_date_time.day)
print(current_date_time.hour)
print(current_date_time.minute)
print(current_date_time.second)
print(current_date_time.strftime("%A")) # Convert date objects into readable strings

# Creating Date Objects
custom_date = datetime.datetime(2020, 7, 14)
print(custom_date_time)

"""
Note: the format codes use with strftime()
%a	Weekday, short version	(Wed)	
%A	Weekday, full version	(Wednesday)	
%w	Weekday as a number 0-6, 0 is Sunday	(3)	
%d	Day of month 01-31	(31)
%b	Month name, short version	(Dec)	
%B	Month name, full version	(December)	
%m	Month as a number 01-12	(12)	
%y	Year, short version, without century	(18)	
%Y	Year, full version	(2018)	
%H	Hour 00-23	(17)	
%I	Hour 00-12	(05)	
%p	AM/PM	(PM)	
%M	Minute 00-59	(41)	
%S	Second 00-59	(08)	
%f	Microsecond 000000-999999	(548513)	
%z	UTC offset	(+0100)	
%Z	Timezone	(CST)	
%j	Day number of year 001-366	(365)	
%U	Week number of year, Sunday as the first day of week, 00-53	(52)
%W	Week number of year, Monday as the first day of week, 00-53	(52)	
%c	Local version of date and time	(Mon Dec 31 17:41:00 2018)	
%x	Local version of date	(12/31/18)	
%X	Local version of time	(17:41:00)	
%%	A % character	(%)
"""