data = [[1, 3, 5, 7, 9, 10], [2, 4, 6, 8]]
data[0].pop(5)
data[0].extend(data[1])
print(data[0])