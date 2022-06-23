# Author Gourish Mokashi
# 23/6/2022
# About for loops

list1 = ["Karnataka", "Maharashtra", "Goa", "kerala"]

for item in list1:
    print(item)

list2 = ("Karnataka", "Maharashtra", "Goa", "kerala")

for item in list2:
    print(item)

list3 = [["Karnataka", 1], ["Maharashtra", 2], ["Goa", 3], ["kerala", 4]]

for item in list3:
    print(item)

for state, rank in list3:
    print(state, "Ranked:", rank)

dict1 = dict(list3)

for item, ranks in dict1.items():
    print(item, "Ranked no.", ranks)

#Quiz

Quizlist = [12, 34, 1, 2, 4, 7, 67, 89, 96, 3, 45,423, 5, 4, 6, 423,]

for num in Quizlist:
    if num > 6:
        print(num)
