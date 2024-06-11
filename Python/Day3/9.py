test_list = [(25, 6), (34, 7), (214, 235), (12, 45), (78,), (111, 22), [356, 729]]

result = [x for x in test_list if isinstance(x, tuple) and any(100 <= i < 1000 for i in x)]

print(result)
