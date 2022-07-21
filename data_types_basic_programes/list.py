
# adding elements to the list
list_1 = [1, 2, 5, 4, "avinash", "raviteja"]
print(list_1)
# o/p [1, 2, 5, 4, 7, 8, 'avinash', 'raviteja']
print("* "*50)

# accessing the elements of the list
print(list_1[:])  # accessing the all elements
# o/p [1, 2, 5, 4, 'avinash', 'raviteja']
print(list_1[3])  # accessing the 3 rd element
# o/p  4
print(list_1[0:4])  # accessing the elements from 1 to 3 , it is index 0 to 3
# o/p [1, 2, 5, 4]
print(list_1[::-1])  # accessing the elements in the reverse order
# o/p ['raviteja', 'avinash', 4, 5, 2, 1]
print(list_1[0:5:2])  # accessing from index 0 to 4 and jumping 2 elements instead of 1
# o/p [1, 5, 'avinash']
print(list_1[5][3])  # accessing the particular elements of the list
# o/p i
print("* "*50)

# add data into the list
# append
# extend
# insert
list_1.append([55, 12])
print(list_1)  # add passed parameters as a single element
# o/p [1, 2, 5, 4, 'avinash', 'raviteja', [55, 12]]
list_1.extend([55, 12])  # extending list by adding all the elements one by one
print(list_1)
# o/p [1, 2, 5, 4, 'avinash', 'raviteja', [55, 12], 55, 12]
list_1.insert(1, "ramya")  # insert passed parameters inplace of index and extend list
print(list_1)
# o/p [1, 'ramya', 2, 5, 4, 'avinash', 'raviteja', [55, 12], 55, 12]
print("* "*50)

# deleting the data into the list
del list_1[5]   # deleting using delete keyword
print(list_1)
# o/p [1, 'ramya', 2, 5, 4, 'raviteja', [55, 12], 55, 12]
list_1.remove("ramya")  # remove the passed element in present list
print(list_1)
# o/p [1, 2, 5, 4, 'raviteja', [55, 12], 55, 12]
list_1.pop(5)   # deleted element can be retrived
print(list_1)
# o/p [1, 2, 5, 4, 'raviteja', 55, 12]
list_1.clear()
print(list_1)
# o/p []
print("* "*50)

# functions in list
# len
# index
# count
# sorted
# reverse
# max
# min
# copy
list_2 = [4, 22, 58, 30, 5, 6, 7, 8, 9, 9]
list_3 = [33, 44]
print(len(list_2))  # find the length of the list
# o/p 10
print(list_2.index(4))  # find the index of the element
# o/p 0
print(list_2.count(5))  # find the count of element in the list
# o/p 1
print(sorted(list_2))   # sort the element in the list
# o/p [4, 5, 6, 7, 8, 9, 9, 22, 30, 58]
print(max(list_2))  # find the max number
# o/p 58
print(min(list_2))  # find the min number
# o/p 4
new_list = list_2.copy()    # copy the elements of list to the new list
print(new_list)
print("* "*50)


