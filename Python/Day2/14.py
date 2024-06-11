def swap_with_third_variable(a, b):
    c = a
    a = b
    b = c
    return a, b

def swap_without_third_variable(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

choice = int(input("Enter choice (1 for with third variable, 2 for without third variable): "))


if choice == 1:
    a, b = swap_with_third_variable(a, b)
    print("After swapping (with third variable):")
elif choice == 2:
    a, b = swap_without_third_variable(a, b)
    print("After swapping (without third variable):")
else:
    print("Invalid choice. Please enter 1 or 2.")

print("a =", a)
print("b =", b)
