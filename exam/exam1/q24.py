# 25)Write a Python script that takes a person's age as input and prints whether they are a child (0-12), a teenager (13-19), an adult (20-64), or a senior (65+).

def get_age():
    age=int(input("your  enter  age :"))
    if age <= 12:
        print("you are child")

    elif age>=13 and age <=19:
        print("you are a teenager")

    elif age>=20 and age <=64:
        print("you are an adult")


    else :
        print("you are senior")
get_age()