# Author Gourish Mokashi
# 27/06/2006

i = 0

while True:
    # here we use true to continue loop to infinity
    if i + 1 < 5:
        i = i + 1
        continue
    # here continue keyword is use to skip below code and just return to Above condition
    # Until the above condition is unfilled till it would continue same condition
    print(i + 1, end=" ")
    # end=" " is used to print next output in same line but by giving a space
    if i == 44:
        break
    # break keyword is used to break a condition
    i = i + 1

print("\n")
# Quiz! (failed)
while True:
    inp = int(input("Enter a number \n"))
    if inp < 100:
        continue
    else:
        print("congrats you have entered number grater then 100")
        break