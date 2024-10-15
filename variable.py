#case sensetive
# A=10
# a=10

# print(a)                 #10   o/p
# print(A)                #10      o/p

# assigning one value to multiple variables
# x=y=z=10                   # 10,10,10    o/p

# assign multiple variable in one line
# p,q,r="orange","banana","cherry"             
         #p=orange   ,  q=banana ,    r=cherry


# print(f"{x}  \n{y}  {z}")          #\n use for new line
# print(f"{p}  {q}  {r}")


# name="shaikh"     #string
# num=10            #intiger  / int
# num1=10.5         #float


# # type function is used to find data types
# print(type(name))
# print(type(num))
# print(type(num1))

# n1=str(4)    #it convert number into string
# n2=int(4)     # it work as +parse int
# n3=float(5)    #it work as float

# print(type(n1))
# print(type(n2))
# print(type(n3))


# print(f"{n1}  \n{n2}   \n{n3}")


# num1= int(input('enter your first number'))
# num2= int(input('enter your second number'))
# # arthmetic operator
# print(f"the addition of {num1}  and  {num2}  is   {num1 + num2}")
# print(f"the substraction of {num1}  and  {num2}  is   {num1 - num2}")
# print(f"the multiplication of {num1}  and  {num2}  is   {num1 * num2}")
# print(f"the division of {num1}  and  {num2}  is   {num1 / num2}")
# print(f"the reminder of {num1}  and  {num2}  is   {num1 % num2}")


#assigment opt

# x=3
# x+=3
# x-=3
# x*=3
# x/=3


#comparison opt
# x=30
# y=35
# print(	x == y)
# print(	x != y)
# print(	x > y)
# print(	x < y)
# print(x >= y)
# print(x <=y)

#logical opt

# x=5
# print(x < 5 and  x < 10)

# print(x < 5 or x < 10)

# print(x < 5 or x < 10)

#array 

list=["apple", "banana","mango","xyz","cherry"]
# print(list)
# print(list[0])
# print(list[1])
# print(list[2])
 
# print(list[-2])    #it gives last elemant of array  / list 

# print(len(list))   #it givesd last elelment of list / array 

# print(list[1:3])     # start with 1 index  but not selelct 2 vslue what we give him 
# print(list[1:])

# print(type(list))
# print(list[:4])

if "apple" in list:
   print("yes")