from audioop import reverse


a_list = [] #spcae is not required in py, but here = to delimit if = belongs to vatiable name or the latter
print(type(a_list))

a_list = [0,13,95,34,56,12]
print(a_list[0]) #0 is the first 1
print(a_list[3])
print(a_list[-1]) #-1 is the last number
print(a_list[0:3]) #0:3 is first number to the previous number before number 3
print(a_list[-3:-1]) #the third number from the bottom to the previous number before the last one
print(a_list[-3:]) #the third number from the bottom to the last one
print(a_list[3::-1]) 
print(a_list[::-1]) #reverse the list

a_list.reverse() 
print(a_list)

a_list.sort()
print(sorted(a_list))
print(a_list)

a_list.append(7) #add single value to the list
print(a_list)
a_list.append([342,234]) #added [342,234] to the list, not recommend

a_list.extend([53,27])
print(a_list) #adding multiple value to the list

a_list.pop()
print(a_list) #remove the last value you added previously to the list

a_list.remove(95)
print(a_list)

del a_list[3] #delete the third element
print(a_list)

a_list=a_list[0:3] #remove all but the first 3 elements 
print(a_list)

a_list.insert(2,3)
print(a_list)

#finding the details for an interger list
a_list=[3,5,7,10,1,6]
for second_num in a_list [1::2]:
    print(second_num)

second_num=a_list[1::2]
first_num=a_list[::2]
deltas=[]
for i in range(0,len(second_num)):
    deltas.append(second_num[i]-first_num[i-1])
print(deltas)
