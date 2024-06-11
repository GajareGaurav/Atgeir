s = input("Enter a string: ")
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
result_upper = ""
result_lower = ""
for char in s:
    if char in uppercase:
        result_upper += lowercase[uppercase.index(char)]
        result_lower += char
    elif char in lowercase:
        result_upper += char
        result_lower += uppercase[lowercase.index(char)]
    else:
        result_upper += char
        result_lower += char

print("Uppercase: ", result_upper)
print("Lowercase: ", result_lower)
