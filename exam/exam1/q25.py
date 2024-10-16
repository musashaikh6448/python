
# 26)Write a Python script that checks if a given number is divisible by both 3 and 5. Print "Divisible by both" if true, otherwise print "Not divisible by both".
  

def number():
    num = int(input("Enter a number: "))
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible By Both")
    else:
        print("Not Divisible By Both")

number()