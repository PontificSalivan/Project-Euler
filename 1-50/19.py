from datetime import date 

count=0
year = date(1901,1,1).year
month = date(1901,1,1).month
while year <= date(2000,12,31).year and month <= date(2000,12,31).month:
    print(str(year)+'  '+str(month))
    if date(year,month,1).isoweekday() == 7:
        count += 1
    if month == 12:
        month=1
        year += 1
    else:
        month += 1
print(count)
    
