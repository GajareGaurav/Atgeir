D = {'a': 10, 'b': 37, 'c': 22, 'd': 33}
entered_number = int(input("Enter a number: "))

filtered_dict = {key: value for key, value in D.items() if value <= entered_number}

print("Filtered dictionary:")
print(filtered_dict)
