# 8.Create a loop that prints all numbers from 1 to 20 but skips multiples of 5.

i=0
print("1 to 20 Number without multiples of 5:-\n")
while i < 20:
   i += 1
   if i%5==0: #using if condition ,we can skip the multiples of 5 until 20
     continue
   print(i)

'''
Output:-
1 to 20 Number without multiples of 5:-

1
2
3
4
6
7
8
9
11
12
13
14
16
17
18
19
'''
