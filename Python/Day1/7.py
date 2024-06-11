first_no=int(input("plz print first number: "))
second_no=int(input("plz print second number: "))
third_no=int(input("plz print third number: "))

def sum_or_3(first_no,second_no,third_no):
    total= first_no+second_no+third_no
    if first_no==second_no==third_no:
        return 3*total
    else:
        return total
    
output=sum_or_3(first_no, second_no, third_no)
print("output: ",output )

