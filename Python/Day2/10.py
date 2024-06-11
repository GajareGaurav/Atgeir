def rem_third(lst):
    index=2
    op=[]

    while len(lst) > 0:
        if index < len(lst):
            op.append(lst.pop(index))
            index += 2  # Move to the next third element
        else:
            break
    
    return op

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

removed_elements = rem_third(numbers)
print("Removed elements:", removed_elements)
