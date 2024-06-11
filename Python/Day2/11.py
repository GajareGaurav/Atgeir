def rearrange_number(num):
    num_str = str(num)
    length = len(num_str)
    result = ""

    i = 0
    j = length - 1

    while i < j:
        result += num_str[i]
        result += num_str[j]
        i += 1
        j -= 1

    if i == j:
        result += num_str[i]

    return result


numbers = [12345, 90213, 123456]

for num in numbers:
    print(rearrange_number(num))
