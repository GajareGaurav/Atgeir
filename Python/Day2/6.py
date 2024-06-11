name=input("enter name: ")
first_name,last_name = name.split()

rev_name=first_name[::-1] + " "+ last_name[::-1]
print(rev_name)