#from validations.validators import *
import time, os,math
from validations.dataTypes import intValidate,floatValidate
from utils.calculationsHistory import logCalc

def standard_menu():
    #Enter while loop in menu, if choice is 1-9 keeps asking again, and if choice is 0 return to main menu
    while True:
        os.system("cls")
        print("\033[33mStandard Mode:\033[0m")
        print("\033[34m1.Addition (+)")
        print("2.Subtraction (-)")
        print("3.Multiplication (*)")
        print("4.Division (/)")
        print("5.Modulo (%)")
        print("6.Exponentiation (**)")
        print("7.Square Root (√)")
        print("8.Reciprocal (1/x)")
        print("9.Percentage (% of a number)")
        print("10.Return to Main Menu\033[0m")
        

        choice = intValidate(input("Please Enter A Choice:"))
        if choice is None:
          print("\033[91mError:  Enter integer numbers only\033[0m")
          time.sleep(2)
          os.system("cls")
          continue
        elif choice <1 or choice>10:
          print("\033[91mError:Select A number within the menu range\033[0m")
          time.sleep(2)
          os.system("cls")
          continue
        if choice == 10:
            print("Returning to main menu.....")
            time.sleep(2)
            break
#operations from 1-6 requires 2 numbers for input so if choice 1-6 :
        
        if choice in [1,2,3,4,5,6]:
                try:
                    num1 = eval(input("Enter first number: "))
                    num2 = eval(input("Enter second number: "))
                except Exception:
                    print("\033[91mError: Please enter valid numbers only.\033[0m")
                    time.sleep(2)
                    os.system("cls")
                    continue

                if choice == 1:
                    result = num1 + num2
                    print("The answer is ",result)
                    logCalc("standard","addition",f"({num1},{num2})",result)
                    print("Result logged to history ✅")
                    time.sleep(2)
                elif choice == 2:
                    result = num1 - num2
                    print("The answer is ",result)
                    logCalc("standard","subtraction",f"({num1},{num2})",result)
                    print("Result logged to history ✅")
                    time.sleep(2)
                elif choice == 3:
                    result = num1 * num2
                    print("The answer is ",result)
                    logCalc("standard","multiplication",f"({num1},{num2})",result)
                    print("Result logged to history ✅")
                    time.sleep(2)
                elif choice == 4:
                    if num2 == 0:
                        print("\033[91mError: Cannot divide by zero.\033[0m")
                        continue
                    result = num1 / num2
                    print("The answer is ",result)
                    logCalc("standard","division",f"({num1},{num2})",result)
                    print("Result logged to history ✅")
                    time.sleep(2)
                elif choice == 5:
                    result = num1 % num2
                    print("The answer is ",result)
                    logCalc("standard","reminder",f"({num1},{num2})",result)
                    print("Result logged to history ✅")
                    time.sleep(2)
                elif choice == 6:
                    result = num1 ** num2
                    print("The answer is ",result)
                    logCalc("standard","exponential",f"({num1},{num2})",result)
                    print("Result logged to history ✅")
                    time.sleep(2)

                elif choice == 7:
                 try:
                    num = eval(input("Enter number: "))
                 except Exception:
                    print("\033[91mError: Please enter a valid number.\033[0m")
                    time.sleep(2)
                    os.system("cls")
                    continue
                 if num < 0:
                    print("Error: square root of negative number is not supported in standard mode.")
                 else:
                    result = math.sqrt(num)
                    print("The answer is ",result)
                    logCalc("standard","Square Root",num,result)
                    print("Result logged to history ✅")
                    time.sleep(2)

                elif choice == 8:
                 try:
                    num = eval(input("Enter number: "))
                 except Exception:
                    print("\033[91mError: Please enter a valid number.\033[0m")
                    time.sleep(2)
                    os.system("cls")
                    continue
                 if num == 0:
                    print("Error: Cannot divide by zero.")
                 else:
                    result =1 / num
                    print("The answer is ",result)
                    logCalc("standard","Reciprical",num,result)
                    print("Result logged to history ✅")
                    time.sleep(2)

                elif choice == 9: 
                  try:
                    base = eval(input("Enter base number: "))
                    percent = eval(input("Enter percentage: "))
                    result = base * (percent / 100)
                    print("The answer is ",result)
                    logCalc("standard","Percentage",(base,percent),result)
                    print("Result logged to history ✅")
                    time.sleep(2)
                  except Exception:
                    print("\033[91mError: Please enter valid numbers.\033[0m")
                    time.sleep(2)
                    os.system("cls")
                    continue
      
        

