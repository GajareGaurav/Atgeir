limit = int(input("Enter the limit: "))

def sum_of_multiples(limit):
    total = 0
    for num in range(limit):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total

def sum_of_common_multiples(limit):
    total = 0
    for num in range(limit):
        if num % 3 == 0 and num % 5 == 0:
            total += num
    return total

sum_of_multiples_result = sum_of_multiples(limit)
sum_of_common_multiples_result = sum_of_common_multiples(limit)

print(f"Sum of multiples of 3 and 5 up to {limit}: {sum_of_multiples_result}")
print(f"Sum of common multiples of 3 and 5 up to {limit}: {sum_of_common_multiples_result}")