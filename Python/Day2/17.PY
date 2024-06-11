string = str(input("Enter a string: "))

digits = sum(char.isdigit() for char in string)
alphabets = sum(char.isalpha() for char in string)
special_characters = sum(not char.isalnum() and not char.isspace() for char in string)
white_spaces = sum(char.isspace() for char in string)
lines = string.count('\n') + 1

print("Total Digits:", digits)
print("Total Alphabets:", alphabets)
print("Special Characters:", special_characters)
print("White Spaces:", white_spaces)
print("Number of Lines:", lines)
