# 21) find the unicode values of A,Z,l,m,n,@,#

# List of characters
characters = ['A', 'Z', 'l', 'm', 'n', '@', '#']

# Finding Unicode values
unicode_values = {char: ord(char) for char in characters}

# Displaying the result
print(unicode_values)
