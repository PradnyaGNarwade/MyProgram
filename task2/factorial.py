# 5. Write a recursive function factorial(n) to calculate the factorial of a number.

def factorial(n):
   if (n==1):
       return n
   else:
       #the fac_recursion() function is recursively called to calculate the factorial of x
       return n * factorial(n-1)
 
#Enter the number
n = int(input("Enter the number : "))
print("The factorial of the above number is", factorial(n))

'''
Output:-
 Enter the number : 5
The factorial of the above number is 120

'''
