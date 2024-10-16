# 10)Create a Python function multiply_elements(lst) that multiplies all elements of a list together. Test it with the list [2, 3, 4].

def multiply_elements(*lst):
    result=1
    for x in lst:
        result=result*x
    print(f"the mul is {result}")


multiply_elements(2,3,4)
        