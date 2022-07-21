
my_dict = {"first": "raviteja", "second": "avinash"}
print(my_dict)
# o/p {'first': 'raviteja', 'second': 'avinash'}
print(my_dict["first"])  # get values by key
# o/p raviteja
print(my_dict.get("second"))
# o/p avinash
print("* "*50)

# adding and changing elements in the dictionary
my_dict["second"] = "ramya"  # change the value  of key
print(my_dict)
# o/p {'first': 'raviteja', 'second': 'ramya'}
my_dict["third"] = "sowjanya"   # add new key,value pair
print(my_dict)
# o/p {'first': 'raviteja', 'second': 'ramya', 'third': 'sowjanya'}
print("* "*50)

# deleting elements from the dictionary
a = my_dict.pop("third")    # remove the key and return value
print("dict:",my_dict)
# o/p dict: {'first': 'raviteja', 'second': 'ramya'}
b = my_dict.popitem()   # remove a key value pair at random ad return them as a tuple
print("\n key , value pair :", b)
print("dict:",my_dict)
# o/p  key , value pair : ('second', 'ramya')
#      dict: {'first': 'raviteja'}
my_dict.clear()     # used to clear all values in the dictionary
print(my_dict)
# o/p {}
# and we can use del keyword to delete the values too
print("* "*50)

# functions
# key
# value
# item
# get
my_dict_1 = {"first": "raviteja", "second": "avinash"}
print(my_dict_1.keys())
# o/p dict_keys(['first', 'second'])
print(my_dict_1.values())
# o/p dict_values(['raviteja', 'avinash'])
print(my_dict_1.items())
# o/p dict_items([('first', 'raviteja'), ('second', 'avinash')])
print(my_dict_1.get("first"))
# o/p raviteja







