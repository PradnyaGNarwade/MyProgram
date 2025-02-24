#6. Use a lambda function with filter( ) to get all even numbers from a list: [1, 2, 3, 4, 5, 6, 7, 8].

mylist=[1, 2, 3, 4, 5, 6, 7, 8]
even_list=list(filter(lambda x:(x%2==0),mylist))
print("mylist=[1, 2, 3, 4, 5, 6, 7, 8]")
print("even number list are:- ",even_list)

'''
Output:-
        mylist=[1, 2, 3, 4, 5, 6, 7, 8]
        even number list are:-  [2, 4, 6, 8]
'''
