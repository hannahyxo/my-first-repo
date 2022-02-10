a_list= [3, 4, 5]
b_list=a_list 
b_list[0]=7 #changing the first number into 7
b_list.sort()
print(a_list)
print(id(a_list), id(b_list))

c_list=a_list.copy()
c_list[0]=12
print(a_list)
print(c_list)

