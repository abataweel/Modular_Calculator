import time, os
from validations.dataTypes import intValidate
from utils.calculationsHistory import logCalc
from math import sin, cos, tan, asin, acos, atan, radians, degrees, pi, factorial, log, exp, e, sinh, cosh, tanh, asinh, acosh, atanh

def scintific_menu():
    """Main menu for scientific calculator mode"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[33mScientific Mode:\033[0m")
        print("\033[34m1.Trigonometric Functions\033[0m")
        print("\033[34m2.Hyperpolic Functions\033[0m")
        print("\033[34m3.Factorial Calculation\033[0m")
        print("\033[34m4.Logarithmic Calculations\033[0m")
        print("\033[34m5.Back to main menu\033[0m")

        choice = intValidate(input("Please Enter A Choice:"))
        if choice is None:
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
            hyperpolicandInverse_menu()
        elif choice == 3:
            try:
                n = int(input("Enter a number for factorial: "))
                if n < 0:
                    print("\033[91mError: Factorial is not defined for negative numbers.\033[0m")
                    time.sleep(2)
                    continue
                result = factorial_function(n)
                print(f"The answer is {result}")
                logCalc("scientific","factorial",n,result)
                print("Result logged to history ✅")
                time.sleep(2)
            except ValueError:
                print("\033[91mError: Please enter a valid integer.\033[0m")
                time.sleep(2)
        elif choice == 4:
            try:
                exorlog = input("Enter 'e' for exponential or 'log' for logarithm: ").strip()
                if exorlog == 'e':
                    val = int(input("Enter power value: "))
                    result = exp(val)
                elif exorlog == 'log':
                    hart = int(input("Enter number: "))
                    base = int(input("Enter base: "))
                    if hart <= 0 or base <= 0 or base == 1:
                        print("\033[91mError: Logarithm undefined for non-positive values or base 1.\033[0m")
                        time.sleep(2)
                        continue
                    result = log(hart, base)
                else:
                    print("\033[91mError: Invalid choice, select 'e' or 'log'.\033[0m")
                    time.sleep(2)
                    continue
                print(f"The answer is {result}")
                logCalc("scientific", exorlog, hart if exorlog=='log' else val, result)
                print("Result logged to history ✅")
                time.sleep(2)
            except ValueError:
                print("\033[91mError: Invalid input.\033[0m")
                time.sleep(2)
        elif choice == 5:
            print("Returning to main menu...")
            time.sleep(2)
            break


def hyperpolicandInverse_menu():
    """ Handles hyperbolic menu functions """
    while True:
        print("\033[33mHyperbolic & Inverse Menu:\033[0m")
        print("\033[34m1.sinh\033[0m")
        print("\033[34m2.cosh\033[0m")
        print("\033[34m3.tanh\033[0m")
        print("\033[34m4.asin\033[0m")
        print("\033[34m5.acos\033[0m")
        print("\033[34m6.atan\033[0m")
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

        try:
            if choice == 1:
                result,userInput = hyperbolic("sinh")
            elif choice == 2:
                result,userInput = hyperbolic("cosh")
            elif choice == 3:
                result,userInput = hyperbolic("tanh")
            elif choice == 4:
                result,userInput = hyperbolic("asinh")
            elif choice == 5:
                result,userInput = hyperbolic("acosh")
            elif choice == 6:
                result,userInput = hyperbolic("atanh")
            elif choice == 7:
                print("Returning to scientific menu...")
                time.sleep(2)
                break
            print("The answer is ",result)
            logCalc("scientific","function",userInput,result)
            print("Result logged to history ✅")
            time.sleep(2)
        except ValueError:
            print("\033[91mError: Invalid numeric input.\033[0m")
            time.sleep(2)
        except Exception as e:
            print(f"\033[91mUnexpected error: {e}\033[0m")
            time.sleep(2)


def trigonometric_menu():
    """ Handles trigonometric menu functions """
    while True:
        print("\033[33mTrigonometric Menu:\033[0m")
        print("\033[34m1.sin\033[0m")
        print("\033[34m2.cos\033[0m")
        print("\033[34m3.tan\033[0m")
        print("\033[34m4.Back to scientific menu\033[0m")

        choice = intValidate(input("Please Enter A Choice:"))
        if choice is None:
            print("\033[91mError: Enter integer numbers only\033[0m")
            time.sleep(2)
            continue
        elif choice <1 or choice>4:
            print("\033[91mError:Select A number within the menu range\033[0m")
            time.sleep(2)
            continue    

        try:
            if choice == 1:
                result,userInput = Trigonometric("sin")
            elif choice == 2:
                result,userInput = Trigonometric("cos")
            elif choice == 3:
                result,userInput = Trigonometric("tan")
            elif choice == 4:
                print("Returning to scientific menu...")
                time.sleep(2)
                break

            print("The answer is ",result)
            logCalc("scientific","trig",userInput,result)
            print("Result logged to history ✅")
            time.sleep(2)
        except ValueError:
            print("\033[91mError: Invalid numeric input.\033[0m")
            time.sleep(2)
        except Exception as e:
            print(f"\033[91mUnexpected error: {e}\033[0m")
            time.sleep(2)


def Trigonometric(trig_function): 
    while True:
        Degrees_or_radians = input('Degrees or radians? ').strip().lower()

        # Allow common shorthand inputs
        if Degrees_or_radians in ['deg', 'degree', 'degrees']:
            Degrees_or_radians = 'degrees'
        elif Degrees_or_radians in ['rad', 'radian', 'radians']:
            Degrees_or_radians = 'radians'
        else:
            print("\033[91mError: Please enter only 'Degrees' or 'radians' (or 'deg'/'rad').\033[0m")
            time.sleep(2)
            continue  # ask again instead of breaking

        try:
            value = int(input('Enter value: '))
        except ValueError:
            print("\033[91mError: Please enter an integer value.\033[0m")
            time.sleep(2)
            continue

        if Degrees_or_radians == 'degrees' and not trig_function.startswith('a'):
            value = radians(value)

        try:
            if trig_function == 'sin':
                return sin(value), value 
            elif trig_function == 'cos':
                return cos(value), value
            elif trig_function == 'tan':
                deg_value = degrees(value)
                while deg_value > 360:
                    deg_value -= 360
                while deg_value < 0:
                    deg_value += 360
                if deg_value == 90 or deg_value == 270:
                    return 'undefined', deg_value
                else: 
                    return tan(radians(deg_value)), deg_value
            elif trig_function == 'asin':
                if value < -1 or value > 1:
                    print("\033[91mError: asin value must be between -1 and 1.\033[0m")
                    return None, None
                result = asin(value)
            elif trig_function == 'acos':
                if value < -1 or value > 1:
                    print("\033[91mError: acos value must be between -1 and 1.\033[0m")
                    return None, None
                result = acos(value)
            elif trig_function == 'atan':
                result = atan(value)

            if Degrees_or_radians == 'degrees':
                return degrees(result), value
            return result, value
        except Exception as e:
            print(f"\033[91mUnexpected error: {e}\033[0m")
            time.sleep(2)
            return None, None


def factorial_function(n):
    try:
        return factorial(n)
    except ValueError:
        print("\033[91mError: Factorial undefined for negative numbers.\033[0m")
        return None


def hyperbolic(hyperbolic_function): 
    try:
        value = int(input('Enter value: '))
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
                print("\033[91mError: acosh is defined for x ≥ 1.\033[0m")
                return None, value
            return acosh(value), value
        elif hyperbolic_function == 'atanh':
            if value <= -1 or value >= 1:
                print("\033[91mError: atanh is defined for -1 < x < 1.\033[0m")
                return None, value
            return atanh(value), value
    except ValueError:
        print("\033[91mError: Invalid numeric input.\033[0m")
        time.sleep(2)
        return None, None
    except Exception as e:
        print(f"\033[91mUnexpected error: {e}\033[0m")
        time.sleep(2)
        return None, None

        








