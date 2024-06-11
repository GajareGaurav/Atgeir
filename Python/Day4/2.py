Org_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_dict_asc = dict(sorted(Org_dict.items(), key=lambda item: item[1]))
print("Ascending Order:", sorted_dict_asc)

sorted_dict_des = dict(sorted(Org_dict.items(), key=lambda item: item[1],reverse=True))
print("descending Order:", sorted_dict_des)
