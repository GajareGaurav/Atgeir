import random

input_list = input("Enter a list of words separated by spaces: ").split()

random.shuffle(input_list)

print("Shuffled list:", input_list)
