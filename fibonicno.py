import math

def isPerfectSquare(number):
    doubt = int(math.sqrt(number))
    return doubt*doubt == number



def check_Fibonacci(number):
    if isPerfectSquare(5*(number * number) +4) or isPerfectSquare(5*(number * number) - 4):
       return True
    else:
      return False

num = int(input("Please enter a number to check if the Number is Fibonacci:"))
if check_Fibonacci(num):
    print("Yes")
else:
    print("No")