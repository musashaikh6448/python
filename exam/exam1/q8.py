# 8)Create a Python function count_vowels(s) that counts the number of vowels in a given string. Test it with the string "Hello World".


def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


string = input("give some msg : ")
vowel = count_vowels(string)
print(f"The number of vowels in '{string}' is: {vowel}")
