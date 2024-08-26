my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)

# create another list
second_list = [50, 60, 70]
#Extend my_list with another list
my_list.extend(second_list)

#Remove the last element from my_list.
del my_list[len(my_list)-1] # or my_list.pop()

#Sort my_list in ascending order.
my_list.sort()

#Find and print the index of the value 30 in my_list.
print(my_list.index(30))
