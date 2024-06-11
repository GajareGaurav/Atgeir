d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'x': 400, 'y': 500, 'z': 600}

# Copy d1 to d3
# d3 = d1.copy()

# Concatenate d2 into d3
d1.update(d2)

print("Concatenated dictionary:")
print(d1)
