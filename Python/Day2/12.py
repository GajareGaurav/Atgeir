def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

num = int(input("Enter an integer: "))


if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")