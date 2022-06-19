# Author Gourish mokashi
# 19/06/2022

# About sets

S = set()
s = {2, 5}
# here we can write set() or {x, y} as set data type
# NOTE: If you write {"a": "b"} then its dict not set
print(type(s))
print(type(S))

s2 = [1, 2, 3, 4]
s3 = set(s2)
# here we can give reference to other variables
print(s3)

s3.add(5)
s3.add(5)
s3.add(6)
# By using .add() function we can add integer or string in sets
s3.remove(6)
# Here by using .remove() function we can remove any integer or string from sets
print(s3)

s4 = s3.union({1, 2, 7})
# By using .union function we can observe whether the following integer or string is present ii the particular set.

print(s3, s4)
# we can print sets in combine to

s5 = s3.intersection({1, 2, 3, 4, 5, 6, 7})
print(s3, s5)
# here by using .intersection() function we and compare or observe the same integers or string

s6 = {8, 9, 6}
print(s3.isdisjoint(s6))
# we can use .isdisjoint() function to check whether the following integer is present in the particular set,
# if it returns false then it is present if return true then not present
