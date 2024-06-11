x = [[1, 2, 3], [10, [4, 6, 7]], 8]
y = []

def flatten_list(l):
    for item in l:
        if isinstance(item, list):
            flatten_list(item)
        else:
            y.append(item)

flatten_list(x)
print("Flattened list:", y)
