import time, os,sys
from validations.dataTypes import intValidate,strValidate,floatValidate
from utils.calculationsHistory import logCalc
from math import sin, cos, tan, asin, acos, atan, radians, degrees, pi, factorial, log, exp, e, sinh, cosh, tanh, asinh, acosh, atanh

def scintific_menu():
    """Main menu for scientific calculator mode"""
    while True:
        ##### printing options menu
        os.system('cls')
        print("\033[33mScientific Mode:\033[0m")
        print("\033[34m1.Trigonometric Functions\033[0m")
        print("\033[34m2.Hyperpolic Functions\033[0m")
        print("\033[34m3.Factorial Calculation\033[0m")
        print("\033[34m4.Logarithmic Calculations\033[0m")
        print("\033[34m5.Back to main menu\033[0m")

        choice = intValidate(input("Please Enter A Choice:"))
        if  choice is None:
            print("\033[91mError: Enter integer numbers only\033[0m")
            time.sleep(2)
            continue
        elif choice < 1 or choice > 5:
            print("\033[91mError: Select A number within the menu range\033[0m")
            time.sleep(2)
            continue    

        if choice == 1:
            trigonometric_menu()
        elif choice == 2:
            hyperpolic_menu()
        elif choice == 3:
            while True:
                 n = intValidate(input("Please enter a non zero number for factorial"))
                 if n is None:
                    print("\033[91mError: Enter integer numbers only\033[0m")
                    time.sleep(2)
                    continue 
                 if n < 0:
                    print("\033[91mError: Factorial is not defined for negative numbers.\033[0m")
                    time.sleep(2)
                    continue
                 result = factorial_function(n)
                 print(f"The answer is {result}")
                 logCalc("scientific","factorial",n,result)
                 print("Result logged to history ✅")
                 time.sleep(2)
                 break
            
        elif choice == 4:
            while True:
                exorlog = strValidate(input("Enter 'e' for exponential or 'log' for logarithm: ")).lower()
                if not exorlog :
                    print("\033[91mInput Error: Invalid choice, select 'e' or 'log'.\033[0m")
                    time.sleep(2)
                    continue
                result = None
                val = None
                validInputs = ["log","e","exp"]
                if not exorlog in validInputs:
                        print("\033[91mError: Please select a valid choice, either log or e\033[0m")
                        time.sleep(2)
                        continue
                if exorlog == 'e':
                    val = intValidate(input("Enter power value: "))
                    if val is None:
                        print("\033[91mError: please enter a valid number.\033[0m")
                        time.sleep(2)
                        continue 
                    result = exp(val)
                elif exorlog == 'log':
                    hart = intValidate(input("Enter number: "))
                    base = intValidate(input("Enter base: "))
                    if hart is None or base is None:
                        print("\033[91mError: Cannot calculate Logarithm, please enter valid values.\033[0m")
                        time.sleep(2)
                        continue
                    if hart <= 0 or base <= 0 or base == 1:
                        print("\033[91mError: Logarithm undefined for non-positive values or base 1.\033[0m")
                        time.sleep(2)
                        continue
                    result = log(hart, base)
                print(f"The answer is {result}")
                logCalc("scientific", exorlog, hart if exorlog=='log' else val, result)
                print("Result logged to history ✅")
                time.sleep(3)
                break
            
        elif choice == 5:
            print("Returning to main menu...")
            time.sleep(1)
            break

def hyperpolic_menu():
    """ Handles hyperbolic menu functions """
    while True:
        print("\033[33mHyperbolic1 Menu:\033[0m")
        print("\033[34m1.sinh\033[0m")
        print("\033[34m2.cosh\033[0m")
        print("\033[34m3.tanh\033[0m")
        print("\033[34m4.asinh\033[0m")
        print("\033[34m5.acosh\033[0m")
        print("\033[34m6.atanh\033[0m")
        print("\033[34m7.Back to scientific menu\033[0m") 

        choice = intValidate(input("Please Enter A Choice:"))
        if choice is None:
            print("\033[91mError: Enter integer numbers only\033[0m")
            time.sleep(2)
            continue
        elif choice <1 or choice>7:
            print("\033[91mError:Select A number within the menu range\033[0m")
            time.sleep(2)
            continue    

        
        if choice == 1:
                result,userInput = hyperbolic("sinh")
                print("The answer is ",round(result,2))
                logCalc("scientific","sinh",userInput,result)
                print("Result logged to history ✅")
                time.sleep(3)
        elif choice == 2:
                result,userInput = hyperbolic("cosh")
                print("The answer is ",round(result,2))
                logCalc("scientific","cosh",userInput,result)
                print("Result logged to history ✅")
                time.sleep(3)
        elif choice == 3:
                result,userInput = hyperbolic("tanh")
                print("The answer is ",round(result,2))
                logCalc("scientific","tanh",userInput,result)
                print("Result logged to history ✅")
                time.sleep(3)
        elif choice == 4:
                result,userInput = hyperbolic("asinh")
                print("The answer is ",round(result,2))
                logCalc("scientific","asinh",userInput,result)
                print("Result logged to history ✅")
                time.sleep(3)
        elif choice == 5:
                result,userInput = hyperbolic("acosh")
                print("The answer is ",round(result,2))
                logCalc("scientific","acosh",userInput,result)
                print("Result logged to history ✅")
                time.sleep(3)
        elif choice == 6:
                result,userInput = hyperbolic("atanh")
                print("The answer is ",round(result,2))
                logCalc("scientific","atanh",userInput,result)
                print("Result logged to history ✅")
                time.sleep(3)
        elif choice == 7:
                print("Returning to scientific menu...")
                time.sleep(1)
                break
        


def trigonometric_menu():
    """ Handles trigonometric menu functions """
    while True:
        #### printing options menu
        print("\033[33mTrigonometric Menu:\033[0m")
        print("\033[34m1.sin\033[0m")
        print("\033[34m2.cos\033[0m")
        print("\033[34m3.tan\033[0m")
        print("\033[34m4.asin\033[0m")
        print("\033[34m5.acos\033[0m")
        print("\033[34m6.atan\033[0m")
        print("\033[34m7.Back to scientific menu\033[0m")
#### validating user input
        choice = intValidate(input("Please Enter A Choice:"))
        if  choice is None:
            print("\033[91mError: Enter integer numbers only\033[0m")
            time.sleep(2)
            continue
        elif choice <1 or choice>7:
            print("\033[91mError:Select A number within the menu range\033[0m")
            time.sleep(2)
            continue    

    ### choices of menu
        if choice == 1:
                result,userInput = Trigonometric("sin")
                print("The answer is ",round(result,2))
                logCalc("scientific","sin",userInput,result)
                print("Result logged to history ✅")
                time.sleep(3)
        elif choice == 2:
                result,userInput = Trigonometric("cos")
                print("The answer is ",round(result,2))
                logCalc("scientific","cos",userInput,result)
                print("Result logged to history ✅")
                time.sleep(3)
        elif choice == 3:
                result,userInput = Trigonometric("tan")
                print("The answer is ",round(result,2))
                logCalc("scientific","tan",userInput,result)
                print("Result logged to history ✅")
                time.sleep(3)
        elif choice == 4:
                result,userInput = Trigonometric("asin")
                print("The answer is ",round(result,2))
                logCalc("scientific","asin",userInput,result)
                print("Result logged to history ✅")
                time.sleep(3)
        elif choice == 5:
                result,userInput = Trigonometric("acos")
                print("The answer is ",round(result,2))
                logCalc("scientific","acos",userInput,result)
                print("Result logged to history ✅")
                time.sleep(3)
        elif choice == 6:
                result,userInput = Trigonometric("atan")
                print("The answer is ",round(result,2))
                logCalc("scientific","atan",userInput,result)
                print("Result logged to history ✅")
                time.sleep(3)                
        elif choice == 7:
             print("Returning to scientific menu...")
             time.sleep(1)
             break



def Trigonometric(trig_function): 
    while True:
        Degrees_or_radians =strValidate(input('Enter "degrees" or "radians": ').strip().lower())
        if not Degrees_or_radians:
            print("\033[91mError: Please enter letters only.\033[0m")
            time.sleep(2)
            continue

        if Degrees_or_radians in ['deg', 'degree', 'degrees']:
            Degrees_or_radians = 'degrees'
        elif Degrees_or_radians in ['rad', 'radian', 'radians']:
            Degrees_or_radians = 'radians'
        else:
            print("\033[91mError: Please enter only 'Degrees' or 'radians' (or 'deg'/'rad').\033[0m")
            time.sleep(2)
            continue  
# DONT YOU REMOVE THIS!!!
        while True:
         try:   
          value = eval(input("Please enter a value:"))
         

          if Degrees_or_radians == 'degrees' and not trig_function.startswith('a'):
              value = radians(value)

          try:
              if trig_function == 'sin':
                  return sin(value), value 
              elif trig_function == 'cos':
                  return cos(value), value
              elif trig_function == 'tan':
                  deg_value = degrees(value)%360
                  while deg_value > 360:
                      deg_value -= 360
                  while deg_value < 0:
                      deg_value += 360
                  if deg_value % 180 == 90:
                      print("\033[91mDomain Error: Cannot perform calculation at this value\033[0m")
                      print("\033[91m tan function isn't defined at this value\033[0m")
                      time.sleep(4)
                      continue
                  else: 
                      return tan(radians(deg_value)), deg_value
              elif trig_function == 'asin':
                  if value < -1 or value > 1:
                      print("\033[91mDomain Error: Cannot perform calculation at this value\033[0m")
                      print("\033[91m asin value must be between -1 and 1.\033[0m")
                      time.sleep(4)
                      continue
                  else:
                     result = asin(value)
              elif trig_function == 'acos':
                  if value < -1 or value > 1:
                      print("\033[91mDomain Error: Cannot perform calculation at this value\033[0m")
                      print("\033[91m acos value must be between -1 and 1.\033[0m")
                      time.sleep(4)
                      continue
                  else:    
                   result = acos(value)
              elif trig_function == 'atan':
                  result = atan(value)  
              if Degrees_or_radians == 'degrees':
                  return degrees(result), value
                  #######################################       
##############################
              return result, value
              
              
          except Exception as e:
             print(f"\033[91mUnexpected error: {e}\033[0m")
             time.sleep(2)
             return None, None
         except ValueError:
             print("\033[91mError: Enter integer numbers only\033[0m")
             time.sleep(2)
             continue


def factorial_function(n):

        return factorial(n)
    

def hyperbolic(hyperbolic_function): 
    while True:
     try:
         value = floatValidate(input("Please enter a value:"))
         if  value is None:
           print("\033[91mError: Enter numeric values only\033[0m")
           time.sleep(2)
           continue
         if hyperbolic_function == 'sinh':
             return sinh(value), value
         elif hyperbolic_function == 'cosh':
             return cosh(value), value
         elif hyperbolic_function == 'tanh': 
             return tanh(value), value
         elif hyperbolic_function == 'asinh':
             return asinh(value), value
         elif hyperbolic_function == 'acosh':
             if value < 1:
                 print("\033[91mDomain Error: Cannot perform calculation at this value\033[0m")
                 print("\033[91macosh is defined for x ≥ 1.\033[0m")
                 time.sleep(4)
                 continue
             else:
                return acosh(value), value
         elif hyperbolic_function == 'atanh':
             if value <= -1 or value >= 1:
                 print("\033[91mDomain Error: Cannot perform calculation at this value\033[0m")
                 print("\033[91matanh is defined for -1 < x < 1.\033[0m")
                 time.sleep(4)
                 continue
             else: return atanh(value),value
            
            
#### ##########################
     except Exception as e:
         print(f"\033[91mUnexpected error: {e}\033[0m")
         time.sleep(2)
         return None, None