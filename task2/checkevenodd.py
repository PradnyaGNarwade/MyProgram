def isEven(n):

    # n&1 is 1, then odd, else even
    if (n & 1) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
  n=int(input("Enter the number to check even-odd:-"))
  if isEven(n):
      print("true")
  else:
      print("false")

'''Output:
Enter the number to check even-odd:-4
true
OR
Enter the number to check even-odd:-3
false

'''
