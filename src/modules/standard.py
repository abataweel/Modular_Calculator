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
            time.sleep(1)
            break
#operations from 1-6 requires 2 numbers for input so if choice 1-6 :
        
        if choice in [1,2,3,4,5,6]:
                while True:
                    num1 = floatValidate(input("Enter first number: "))
                    num2 = floatValidate(input("Enter second number: "))
                    if num1 is None or num2 is None:
                         print("\033[91mError: Please enter valid numbers only.\033[0m")
                         time.sleep(2)
                         continue
                    elif choice == 1:
                      result = num1 + num2
                      print("The answer is ",result)
                      logCalc("standard","addition",f"({num1},{num2})",result)
                      print("Result logged to history ✅")
                      time.sleep(2)
                      break
                    elif choice == 2:
                     result = num1 - num2
                     print("The answer is ",result)
                     logCalc("standard","subtraction",f"({num1},{num2})",result)
                     print("Result logged to history ✅")
                     time.sleep(2)
                     break
                    elif choice == 3:
                     result = num1 * num2
                     print("The answer is ",result)
                     logCalc("standard","multiplication",f"({num1},{num2})",result)
                     print("Result logged to history ✅")
                     time.sleep(2)
                     break
                    elif choice == 4:
                      while True:
                        if num2 == 0:
                         print("\033[91mError: Cannot divide by zero.\033[0m")
                         time.sleep(2)
                         continue
                        result = num1 / num2
                        print("The answer is ",result)
                        logCalc("standard","division",f"({num1},{num2})",result)
                        print("Result logged to history ✅")
                        time.sleep(2)
                        break
                      break
                    elif choice == 5:
                     result = num1 % num2
                     print("The answer is ",result)
                     logCalc("standard","reminder",f"({num1},{num2})",result)
                     print("Result logged to history ✅")
                     time.sleep(2)
                     break
                    elif choice == 6:
                     result = num1 ** num2
                     print("The answer is ",result)
                     logCalc("standard","exponential",f"({num1},{num2})",result)
                     print("Result logged to history ✅")
                     time.sleep(2)
                     break

        elif choice == 7:
                 while True:
                     num = floatValidate(input("Enter number: "))
                     if num is None:
                      print("\033[91mError: Invalid choice, select 'e' or 'log'.\033[0m")
                      time.sleep(2)
                      continue
                     if num < 0:
                      print("\033[91mError: square root of negative number cannot be calculated\033[0m")
                      time.sleep(2)
                      continue  
                     result = math.sqrt(num)
                     print("The answer is ",result)
                     logCalc("standard","Sqrt",num,result)
                     print("Result logged to history ✅")
                     time.sleep(2)
                     break

        elif choice == 8:
                  while True:
                     num = intValidate(input("Enter number: "))
                     if num is None:
                      print("\033[91mError: Please enter a valid number.\033[0m")
                      time.sleep(2)
                      continue
                     if num == 0:
                      print("\033[91mError: Cannot divide by zero.\033[0m")
                      time.sleep(2)
                      continue
                     result =1 / num
                     print("The answer is ",result)
                     logCalc("standard","Reciprical",num,result)
                     print("Result logged to history ✅")
                     time.sleep(2)
                     break

        elif choice == 9: 
                  while True:
                     base = intValidate(input("Enter base number: "))
                     percent = intValidate(input("Enter percentage: "))
                     if base is None or percent is None:
                       print("\033[91mError: Please enter valid numbers.\033[0m")
                       time.sleep(2)
                       os.system("cls")
                       continue
                     result = base * (percent / 100)
                     print("The answer is ",result)
                     logCalc("standard","Percentage",(base,percent),result)
                     print("Result logged to history ✅")
                     time.sleep(2)
                     break
      
        

