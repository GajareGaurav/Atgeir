user_input=str(input("Enter string"))

def cases(user_input):
    upper_count = sum(1 for c in user_input if c.isupper())
    lower_count = sum(1 for c in user_input if c.islower())
    return upper_count, lower_count

upper_count, lower_count =cases(user_input)

print("No. of upper case Characters: ",upper_count )
print("No. of Lower case Characters: ",lower_count)