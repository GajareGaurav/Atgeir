def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numbers = (1, 2, 30, 4, 5, 67, 7, 8, 9)

even = sum(1 for num in numbers if num % 2 == 0)
odd = sum(1 for num in numbers if num % 2 != 0)
aprime = sum(1 for num in numbers if prime(num))

print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")
print(f"Number of prime numbers: {aprime}")
