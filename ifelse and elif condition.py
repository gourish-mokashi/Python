# Author
# 20/06/2022

# About if else and elif conditions

var1 = 12
var2 = 56
var3 = int(input())
# Here we have used int(input()) function to just accept integer inputs

if var3 > var2:
    print("Grater")
# here if var is greater then var2 the print it or

elif var3 == var2:
    print("Equal")
# if var3 is equal to var2 then print it
else:
    print("Lesser")
# or if not anything then print this


list1 = [1, 3, 54]
if 3 in list1:
    print("yes its there")
    # here if 3 is present in list the print this or
else:
    print("Not its not there")
    # if not present then print it

print(3 in list1)
# here it returns in boolean value means true or false
# if 3 is in the list then true if not then false


if 3 not in list1:
    print("Not its not there")
    # same as above but if not there
else:
    print("yes its there")

print(3 not in list1)

# what if the number is not in list then?

if 7 in list1:
    print("yes its there")
else:
    print("Not its not there")

print(7 in list1)
