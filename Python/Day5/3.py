start=int(input("enter starting number: "))
end = int(input("enter ending number: "))
user_input = list(range(start , end +1))

gvn_num= int(input("Enter number: "))

def if_in_lst(user_input, gvn_num):
    if gvn_num in user_input:
        print("number in list")
    else:
        print("number not in list")    

if_in_lst(user_input, gvn_num)