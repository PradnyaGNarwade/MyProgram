#7. Write a while loop to print the first 5 multiples of 3.
n=1
table=3

while(n<=5):
   result=n*table
   print(f"{table}*{n}={result}")
   n+=1
   
'''Output:
         3*1=3
         3*2=6
         3*3=9
         3*4=12
         3*5=15'''
