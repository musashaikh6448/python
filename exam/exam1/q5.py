# 5)Write a Python script to find the length of a given string without using the built-in len() function.

def string_length(string):
    count = 0
    for lenght in string:
        count +=1
    print(count)

string_length("shaikh")
