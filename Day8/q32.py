#Calculate the number of days between two dates

from datetime import date

print("Enter the starting date(yy/mm/dd)")
f_y = int(input())
f_m = int(input())
f_d = int(input())

print("Enter the starting date(yy/mm/dd)")
l_y = int(input())
l_m = int(input())
l_d = int(input())

f_date = date(f_y,f_m,f_d)
l_date = date(l_y,l_m,l_d)

delta = l_date - f_date

print("The number of days between thr dates is: ",delta)
