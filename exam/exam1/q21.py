# 21) find the unicode values of A,Z,l,m,n,@,#


characters = ['A', 'Z', 'l', 'm', 'n', '@', '#']
unicode_values = {char: ord(char) for char in characters}
for char, unicode_value in unicode_values.items():
    print(f"Unicode value of '{char}' is: {unicode_value}")
