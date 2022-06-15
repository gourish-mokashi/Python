mystr= "Python is a programming language"
print(len(mystr))
#here len() function shows the length of the string
"""-----------------------------------------------------------------------------------------------------------------"""
#About String Slicing

#string name[] function is used to slice strings

print("String Slicing 1:",mystr[0:10])
"""here the '0:10' tells to print specific sting in the order (but the string would only be till 9  
not till because 10th string will not be included)
In Python the for anything is 0"""

print("String Slicing 2:",mystr[0:40])
#if we took the numbers like 0:40 where 40th string do not exsist then the compilar would print whole string

print("String Slicing 3:",mystr[0:])
#if another number is not given like'0: ' then the compilar would print whole string ([0:length of string])

print("String Slicing 4:",mystr[:5])
#if another number is not given like':5' then the compilar would only print tell specified number 5 as given
# ([0:5])

print("String Slicing 5:",mystr[:])
#if it's blank the by defalt [0:length of string] would print

print("String Slicing 6:",mystr[0:32:2])
"""here extra collam represents after how many term the string must print
 if their is 0:32:2 then sting would print after single gaps and if 0:32:3 then with double gaps"""

print("String Slicing 7:",mystr[::])
#If it's blank then by defalt[0:string length:1] would print

print("\n")
#Negative indusise
# mystr= "Python is a programming language"

#Negative indusise is same as string spliting but in opposite manner

print("Negative indusise 1:",mystr[-8:-4])
#here -8th means L and -4th term is u but -4th term is not included in it so we must take -5th term g

print("Negative indusise 2:",mystr[-8:])
#here -8th means L and so there is no end splitting term entered so by default it will be zero and 1st string is e

print("Negative indusise 3:",mystr[::-1])
#here the whole given string is printed inversely

print("Negative indusise 4:",mystr[::-2])
#here the whole given string is printed inversely but with single strings gaps, if there is -3 or -4 then the string
# would print with double and three times gaps.
print("\n")
#fun
print("fun-time activities")
funstr = "time for fun"
print(len(funstr))

print(funstr[0:12])
funstr2 = funstr[0:10]
print(funstr2)
funstr3 = funstr[::-1]
print(funstr3)