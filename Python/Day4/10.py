D = {'a': 10, 'b': 37, 'c': 22, 'd': 33, 'e': 45, 'f': 9, 'g': 88, 'h': 63, 'i': 98, 'j': 12}
inp_3 = input("Enter 3 keys: ").split(",")

val = [D[key] for key in inp_3]

max_val = max(val)

max_key = inp_3[val.index(max_val)]

print(f"The highest keys {inp_3} is {max_key} and its value is {max_val}")
