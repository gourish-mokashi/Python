# Project
# Quiz

# Driving license approval

print("Enter Your Age")
candidates_age = int(input())

if candidates_age > 18 :
    print("You can have driving license and have your drive")
elif candidates_age < 18:
    print("Sorry, you need to be above 18 to ride vehicle")
elif candidates_age == 18:
    print("You can have your ride, but make sure to have you driving license")
else:
    print("Invalid Input")
