# 10. Write a program that checks if a year is a leap year.
#(Hint: A year is a leap year if it is divisible by 4 but not by 100, except when it is also divisible by 400)

# Python program to check if year is a leap year or not

year =int(input("Enter the Year:-"))



# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))

'''
Output:-
Enter the Year:-2000
2000 is a leap year

Enter the Year:-2025
2025 is not a leap year

'''
