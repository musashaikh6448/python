# 19. Write a Python script that takes three numbers as input and prints the largest of the three numbers.


def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest = find_largest(number1, number2, number3)
print(f"The largest  numbers is: {largest}")

