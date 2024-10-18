# def add(a,b):                                     #def is a keyword of function
#     print(a+b)

# add(10,20)

# def sub(x,y):
#     return x-y        
# print(sub(20,10)) 

# s1=sub(10,2)
# print(s1)  

########################################
#global scope
# x=4
# y=6
# def show():
#     print(x)
#     print(y)

# show()
# print(x)
# print(y)

#n number of argument # rest parameter
# def mul(*a):
#     result=1
#     for x in a:
#         result=result*x
#     print(f"the mul is {result}")

# mul(2,3)
# mul(2,3,4)
# mul(2,3)


# def person(**b):
#     print(b)

# person(name="shaikh")



def fizz_buzz(x):
    
    if x % 3==0 and x%5 ==0 :
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz") 
    elif  x % 5 == 0:
        print("buzz")
    else:
        print(f"the given number {x} is not for dividation")
   
    

fizz_buzz(2)