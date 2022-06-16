# Author Gourish Mokashi
#16/6/2022

# All About listing
# Listing in strings
Grocery = ["salt", "Sugar", "Washing powder", "tomatoes"]
print(Grocery)
print(len(Grocery))
print(min(Grocery))
print(max(Grocery))

# listing in integers
Numbers = [2, 3, 54, 45, 58]
print(Numbers)
# Slicing in lists
print(Numbers[0:5])
print(Numbers[::2])

# Functions for listing
Numbers.append(44)
Numbers.append(43)
Numbers.append(35)
print(Numbers)
# here append means add the number to end of list

Numbers.insert(2, 12)
print(Numbers)
# here Insert means add a number in particular index place

Numbers.pop(2)
print(Numbers)
# here Pop means deleting number of particular index.
# (last index is default in it)

Numbers[1] = 4
print(Numbers)
# here this function just replace the number with the following index

# Some similar function from Strings
print(len(Numbers))
print(max(Numbers))
print(min(Numbers))

# Arranging in order

# In Ascending order
Numbers.sort()
print(Numbers)

# In Descending order
Numbers.reverse()
print(Numbers)

# Mutable- which can be changed
# Immutable- which cannot be changed

# the list which uses [] Square bracket that are mutable
# and which uses () parentheses Bracket that are Immutable

Numbers2 = (1, 2, 3)
print(Numbers2)
# Numbers2 [2]= 4
# Here if we run the above code then the error will occur,
# because a 'tuple' can be changed

Numbers3 = (1, )
# Here we cannot take only (1), Because then it will not be a tuple
# so we need to assign a comma after it (1, )
print(Numbers3)

# Swapping technics
# traditional method
a = 2
b = 3
temp = a
a=b
b= temp
print(a,b)

# modern method
a1=5
b1=3
a1, b1= b1, a1
print(a1, b1)