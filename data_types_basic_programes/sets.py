# my_set = {1, 2, 3, 4, 5, 6}
# print(my_set)
# o/p {1, 2, 3, 4, 5, 6}
print("* "*50)

# adding the elements in set
# my_set.add(7)
# print(my_set)
# o/p {1, 2, 3, 4, 5, 6, 7}
print("* "*50)

# other methods in set
# union
# intersection
# difference
# symmetric difference
# clear
my_set_1 = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}
# print(my_set_1.union(my_set_2), "-------", my_set_1|my_set_2)     # union operation can be done
# o/p {1, 2, 3, 4, 5, 6}
# print(my_set_1.intersection(my_set_2), "-----", my_set_1 & my_set_2)  # intersection using int
# o/p {3, 4} ----- {3, 4}
# print(my_set_1.difference(my_set_2), "------", my_set_1 - my_set_2)   # perform the difference
# o/p  {1, 2} ------ {1, 2}
# print(my_set_1.symmetric_difference(my_set_2), "----", my_set_1 ^ my_set_2)     # perform symmetric difference
# o/p {1, 2, 5, 6} ---- {1, 2, 5, 6}
# print(my_set_1.clear())     # empty the set
# o/p None
print("* "*50)

# operators with sets
superset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 == s2)   # if symmetric
# o/p False
print(s1 != s2)   # if not symmetric
# o/p True
print(s1 <= superset)   # if s1 is subset of super set
# o/p True
print(s1 < superset)    # s1 is a proper set of superset
# o/p True
print(s1 >= s2)   # if s2 is subset of s1
# o/p False
print(s1 > s2)   # if s2 is a proper subset of s1
# o/p False



