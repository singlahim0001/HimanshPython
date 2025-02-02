print("\n **************Calculator Made by Himanshu**************\n")
# Author: Himanshu Singla
# Date: 2 Feb 2025
# Calculator
while True:
    a= input("Please Enter Your Name: \n")
    if a.strip() == ""  or " " in a or not a.isalpha():
        print("Please write your name to go further")
    else:
        break
print("Your Name: "+ a)
print("If you want to perform Calculation of Two Numbers ")
for attempt in range(5):  # Loop 5 times
    b = input("Please choose (Y or N): ")  # Ask for input

    if b == 'Y':
        print("Thank you for choosing the Calculator")
        print("Choose your operation you want to perform \n Addition (1) , Substraction (2), Division (3), Multiplication (4)")

        #Validation to check c
        while True:
            c = int(input("Please choose operation : \n"))
            if c not in [1,2,3,4]:
                print("Please choose valid input (1 , 2 , 3, 4)")
            else:
                break
        d= int(input("Choose 1st Number: "))
        e= int(input("Choose 2nd Number: "))
        if c == 1:
            result = d+e
            print("Addition of Two Numbers are : ", result)
        elif c == 2:
            result= d-e
            print("Substraction of Two Numbers are : ", result)
        elif c == 3:
            if e==0:
                print("******Error Cannot divide******")
            else:
                result = d / e
                print("Division of Two Numbers are : ", result)
        elif c == 4:
            result = d*e
            print("Multiplication of Two Numbers are : ", result)

        break  # Exit the loop if input is valid
    elif b == 'N':
        print("No problem, anything else that I can help you with?")
        break  # Exit the loop if input is valid
    else:
        print("You chose a wrong input. Please choose (Y or N)")

    # If the user reaches 5 attempts without a valid input, inform them
    if attempt == 4:
        print("You've reached the maximum number of attempts.")

print("~~~~~~~~Thankyou~~~~~~~~")
#Thankyou----
# Himanshu.