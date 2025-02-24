#4.Define a function sum_numbers(a, b=10) that takes two numbers and returns their sum. If the second number is not provided, it should default to 10.

def sum_numbers(a, b=10):
    print("The sum of",a,"And",b)
    sum=a+b
    return sum
    
result=sum_numbers(a=9)
print(result) #Here,we can not pass the value of b,hence b have a default value 

result2=sum_numbers(a=4,b=9)
print(result2)#Here,both value is pass

'''
Output:-

The sum of 9 And 10
19
The sum of 4 And 9
13


'''
