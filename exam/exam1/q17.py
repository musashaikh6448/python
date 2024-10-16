# 17)Write a Python script that takes a grade (0 to 100) as input and prints the corresponding letter grade based on the following scale:

# 90 and above: A
# 80 to 89: B
# 70 to 79: C
# 60 to 69: D
# Below 60: F


def grade():
    find=int(input("give the your percentage number to find grade. "))
    if find >= 90:
        print("A")
    elif find>=80 and find <=89:
        print("B")
    elif find>=70 and find <=79:
        print("C")
    elif find>=60 and find <=69:
        print("D")
    else :
        print("F")
grade()