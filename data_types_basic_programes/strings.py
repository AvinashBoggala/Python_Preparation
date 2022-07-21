string_1 = "i love my india"
string_2 = " iam an indian"
# string slicing
# print(string_1[:])  # print all
# o/p i love my india
# print(string_1[2:6])   # print from index 2 until index and skip 10
# o/p love
# print(string_1[0:10:1])    # print from o to 9 and skip the 1 element
# o/p i love my
# print(string_1[::-1])      # reverse the string
# o/p  aidni ym evol i
# print(string_1[-16:-1])
# o/p i love my indi

# functions
# len
# count
# lower
# upper
# find
# partition
# split
# replace
print(len(string_1))    # return length
# o/p 15
print(string_1.count(" "))   # returns length of string
# o/p 3
print(string_1.lower())   # convert to lower case
# o/p i love my india
print(string_1.upper())  # convert to upper case
# o/p I LOVE MY INDIA
print(string_1.find("o"))  # returns the element of the string
# o/p 3
print(string_1.partition("love"))   # breaks the string into tuple for the element passed
# o/p  ('i ', 'love', ' my india')
print(string_1.split(" "))    # split the string for the parameters passed
# o/p ['i', 'love', 'my', 'india']
print(string_1.replace("india", "name"))    # replace the string with new passed parameter
# o/p i love my name
