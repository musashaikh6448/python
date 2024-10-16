# 15) Write a Python function sum_of_arguments(n) that calculates the sum of arguments. Test it with the number 10,20,30,40

def sum_of_arguments(*n):
    total=0
    for num in n:
        total+=num
    return total
    
result=sum_of_arguments(10,20,30,40)
print(f"the total result is {result}")