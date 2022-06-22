# Faulty Calculator

# Harry bhai is an investigator and heard conversation of two students, talking about cheating in exams by writing a
# python code to make a calculator But unfortunately they don't knew that harry bhai is hearing them, And although
# harry bhai is the father of them in cheating So, harry bhai told us to write a code for faulty calculator which
# would prints 5 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4 which will be wrong, and these calculation were normally used in question

# 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4


print("If Addition press 1 \nIf Subtraction press 2 \nIf multiplication press 3 \nIf Division press 4")
cal = int(input())
if cal > 4:
    print("Invalid Input")
elif cal < 1:
    print("Invalid Input")
else:
    print("")

if cal == 1:
    print("Addition")
elif cal == 2:
    print("Subtraction")
elif cal == 3:
    print("Multiply")
elif cal == 4:
    print("Divide")

print("_________________________")

print("Enter First number:")
num1 = int(input())
print("Enter Second number:")
num2 = int(input())

print("_________________________")

if cal == 1:
    if num1 == 56 and num2 == 9:
        print("Sum is: 77")
    elif num1 == 9 and num2 == 56:
        print("Sum is: 77")
    else:
        print("Sum is: ", num1 + num2)

if cal == 2:
    print("Subtraction is: ", num1 - num2)

if cal == 3:
    if num1 == 45 and num2 == 3:
        print("Product is: 555")
    elif num1 == 3 and num2 == 45:
        print("Product is: 555")
    else:
        print("Product is: ", num1 * num2)

if cal == 4:
    if num1 == 56 and num2 == 6:
        print("Answer is: 4 ")
    elif num1 == 6 and num2 == 56:
        print("Answer is: 4 ")
    else:
        print("Answer is: ", num1 / num2)
