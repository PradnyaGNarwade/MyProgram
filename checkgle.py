# 8. Write a program to compare two numbers and print whether the first is greater, smaller, or equal to the second using relational operators

first=int(input("Enter the first number:-"))
second=int(input("Enter the second number:-"))

if first > second:
    print("First number is greater than second")
elif first < second:
    print("First number is less than second")
else:
    print("Both are equal")
    
