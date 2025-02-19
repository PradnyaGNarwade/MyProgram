#write a program that print the grade based on score input using if-else statement(A for 90-100,B for 80-89) in python

print("Enter Marks Obtained in 5 Subjects: ")
total1=int(input("Enter Marks Obtained in 1 Subjects: "))
total2 =int(input("Enter Marks Obtained in 1 Subjects: "))
total3 = int(input("Enter Marks Obtained in 1 Subjects: "))
total4 = int(input("Enter Marks Obtained in 1 Subjects: "))
total5 = int(input("Enter Marks Obtained in 1 Subjects: "))
 
tot = total1 + total2 + total3 + total4 + total4
avg = tot / 5
print(avg) 
if avg >= 90 and avg <= 100:
    print("Your Grade is A")
elif avg >= 80 and avg < 90:
    print("Your Grade is B")
else:
    print("Your Grade is C")
