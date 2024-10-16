# 14) Write a Python function sum_of_digits(n) that calculates the sum of digits of an integer. Test it with the number 123.

def sum_of_digits(*n):
    total=0
    for num in n:
        total+=num
    return total
    
result=sum_of_digits(1,2,3)
print(f"the total result is {result}")