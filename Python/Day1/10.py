a = int(input("first number: "))
b = int(input("second number: "))

print("Before: a =", a, ", b =", b)

a = a + b
b = a - b
a = a - b

print("After: a =", a, ", b =", b)
