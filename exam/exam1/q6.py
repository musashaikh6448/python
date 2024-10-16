# 6)Write a Python script to reverse a given string.



def reverse(string):
    return string[::-1]


string = input("Enter a string: ")
reversed_string = reverse(string)
print(f"The reversed string is: {reversed_string}")
