def is_palindrome(x):
    cleaned_string = ''.join(c.lower() for c in x if c.isalnum())
    return cleaned_string == cleaned_string[::-1]

user_input = input("Enter string: ")
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
