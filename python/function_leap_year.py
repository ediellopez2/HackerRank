## You are given the year, and you have to write a function
## to check if the year is leap or not.

## In the Gregorian calendar three criteria must be taken
## into account to identify leap years:

## The year can be evenly divided by 4, is a leap year, unless:
##      The year can be evenly divided by 100, it is NOT a leap year, unless:
##          The year is also evenly divisible by 400. Then it is a leap year.

## This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
## while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.


def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


# year = int(input())
# print(is_leap(year))


print("1832: ", is_leap(1832))
print("1980: ", is_leap(1980))
print("2000: ", is_leap(2000))
print("2020: ", is_leap(2020))
print("2400: ", is_leap(2400))


print("1990: ", is_leap(1990))


