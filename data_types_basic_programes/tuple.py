my_tuple = ()

tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = ("raviteja", "avinash", "ramya")
tuple_3 = (1, 2, 3, ["avinash", "raviteja"])
print(tuple_1[0])
# o/p 1
print(tuple_2[:])
# o/p ('raviteja', 'avinash', 'ramya')
print(tuple_3[3][1])
# o/p raviteja
print("* "*50)

# tuple methods
# count
# index
print(tuple_3.count(2))
# o/p  1
print(tuple_3.index(["avinash", "raviteja"]))
# o/p  3

