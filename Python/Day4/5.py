x = {'mango', 'apple'}
y = {'mango', 'orange'}
z = {'mango'}

# using comparision operator

print(x <= y)
print(x < z)

print(y <=x )
print(y < z)

print(z < x)
print(z < y)


# using issubset

def is_subset(set1, set2):
    return set1.issubset(set2)

# Check if x is a subset of y
print("Is x a subset of y?", is_subset(x, y))

# Check if y is a subset of x
print("Is y a subset of x?", is_subset(y, x))

# Check if y is a subset of z
print("Is y a subset of z?", is_subset(y, z))

# Check if z is a subset of y
print("Is z a subset of y?", is_subset(z, y))

# Check if z is a subset of x
print("Is z a subset of x?", is_subset(z, x))



























