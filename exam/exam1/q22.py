# 22)Write a Python script that takes an integer between 1 and 7 as input and prints the corresponding day of the week (1 for Monday, 2 for Tuesday, etc.). If the number is outside this range, print "Invalid input".

day = int(input("Enter an integer between 1 and 7: "))

if day == 1:
    print("The day of the week is: sunday")
elif day == 2:
    print("The day of the week is: monday")
elif day == 3:
    print("The day of the week is: tuesday")
elif day == 4:
    print("The day of the week is: wednesday")
elif day == 5:
    print("The day of the week is: thursday")
elif day == 6:
    print("The day of the week is: friday")
elif day == 7:
    print("The day of the week is: saturday")
else:
    print("Invalid input")