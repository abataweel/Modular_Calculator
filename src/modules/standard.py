#from validations.validators import *
import math

def standard_menu():
    #Enter while loop in menu, if choice is 1-9 keeps asking again, and if choice is 0 return to main menu
    while True:
        print("Standard Mode: ")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulo (%)")
        print("6. Exponentiation (**)")
        print("7. Square Root (√)")
        print("8. Reciprocal (1/x)")
        print("9. Percentage (% of a number)")
        print("0. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Returning to main menu.....")
            break
#operations from 1-6 requires 2 numbers for input so if choice 1-6 :
        try:
            if choice in ["1", "2", "3", "4", "5", "6"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = num1 + num2
                elif choice == "2":
                    result = num1 - num2
                elif choice == "3":
                    result = num1 * num2
                elif choice == "4":
                    if num2 == 0:
                        print("Error: Cannot divide by zero.")
                        continue
                    result = num1 / num2
                elif choice == "5":
                    result = num1 % num2
                elif choice == "6":
                    result = num1 ** num2

                print(f"Result: {result}")

            elif choice == "7":
                num = float(input("Enter number: "))
                if num < 0:
                    print("Error: square root of negative number is not supported in standard mode.")
                else:
                    print(f"Result: {math.sqrt(num)}")

            elif choice == "8":
                num = float(input("Enter number: "))
                if num == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print(f"Result: {1 / num}")

            elif choice == "9":
                base = float(input("Enter base number: "))
                percent = float(input("Enter percentage: "))
                print(f"Result: {base * (percent / 100)}")

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Error: Please enter valid numbers.")
        
standard_menu()
