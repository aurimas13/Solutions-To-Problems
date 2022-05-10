import calendar

my_date = list(map(str, input().split()))
my_date_day =int(my_date[0], 10)
my_date_month = int(my_date[1], 10)
my_date_year = int(my_date[2])

if calendar.weekday(my_date_year, my_date_day, my_date_month) == 0:
    print('MONDAY')
elif calendar.weekday(my_date_year, my_date_day, my_date_month) == 1:
    print('TUESDAY')
elif calendar.weekday(my_date_year, my_date_day, my_date_month) == 2:
    print('WEDNESDAY')
elif calendar.weekday(my_date_year, my_date_day, my_date_month) == 3:
    print('THURSDAY')
elif calendar.weekday(my_date_year, my_date_day, my_date_month) == 4:
    print('FRIDAY')
elif calendar.weekday(my_date_year, my_date_day, my_date_month) == 5:
    print('SATURDAY')
else:
    print ('SUNDAY')