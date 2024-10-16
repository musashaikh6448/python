# 16)Write a Python script that takes a number as input and prints whether the number is positive, negative, or zero.

def check(n):
    if n > 0:
        print("The number is positive.")
    elif n < 0:
        print("The number is negative.")
    else:
         print("The number is zero.")

check(0)