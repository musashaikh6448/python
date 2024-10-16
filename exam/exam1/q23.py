# 24)Write a Python script that takes a month number (1 to 12) as input and prints the corresponding month name. If the number is outside this range, print "Invalid month".


month = int(input("Enter a month number (1 to 12) "))

if month == 1:
    print("The month of the year is: january")
elif month == 2:
    print("The month of the year is: febuary")
elif month == 3:
    print("The month of the year is: march")
elif month == 4:
    print("The month of the year is: april")
elif month == 5:
    print("The month of the year is: may")
elif month == 6:
    print("The month of the year is: june")
elif month == 7:
    print("The month of the year is: july")
elif month == 8:
    print("The month of the year is: august")
elif month == 9:
    print("The month of the year is: septembar")
elif month == 10:
    print("The month of the year is: octobar")
elif month == 11:
    print("The month of the year is: November")
elif month == 12:
    print("The month of the year is: December")
else:
    print("Invalid input")