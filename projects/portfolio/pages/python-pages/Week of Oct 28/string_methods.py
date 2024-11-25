my_string = "The quick brown fox jumps over the lazy dog"

# 'The quick brown fox jumps over the lazy dog'
my_string = my_string.capitalize()
print(my_string)

# '****************The quick brown fox jumps over the lazy dog****************'
my_string = my_string.center(100, '*')
print(my_string)

found = my_string.find("fox")  # 44
print(found)

print(my_string.isalnum())  # False

# '****************the quick brown fox jumps over the lazy dog****************'
print(my_string.lower())

# '****************THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG****************'
print(my_string.upper())

# ['****************The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog****************']
out = my_string.split()
