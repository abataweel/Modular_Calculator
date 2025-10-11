import time,os
from ..validations.dataTypes import intValidate
from ..utils.calculationsHistory import logCalc

from math import sin, cos, tan, asin, acos, atan, radians, degrees , pi , factorial , log ,exp , e ,sinh , cosh , tanh ,asinh , acosh , atanh
def scintific_menu():
    
    """Main menu for scintific calculator mode"""

    while True:
            os.system('cls')
            print("\033[33mScientific Mode:\033[0m")
            print("\033[34m1.Trigonometric Functions\033[0m")
            print("\033[34m2.Hyperpolic Functions\033[0m")
            print("\033[34m3.Factorial Calculation\033[0m")
            print("\033[34m4.Logarethmic Calculations\033[0m")
            print("\033[34m5.Back to main menu\033[0m")
            choice = intValidate(input("Please Enter A Choice:"))
            if not intValidate(choice):
              print("\033[91mError:  Enter integer numbers only\033[0m")
              time.sleep(3)
              os.system("cls")
              continue
            elif choice <1 or choice>5:
              print("\033[91mError:Select A number within the menu range\033[0m")
              time.sleep(3)
              os.system("cls")
              continue    
            if choice == 1:
                trigonometric_menu()
                 
            elif choice == 2:
                hyperpolicandInverse_menu()
                
            elif choice == 3:
                print("factorial")
                break
            elif choice == 4:
                
                break
            elif choice == 5:
             print("Returning to main menu...")
             time.sleep(2)
             break
def hyperpolicandInverse_menu():
    """ Handles hyperpolic menu functions """
    
    while True:
      print("\033[33mHyperpolic & Inverse Menu:\033[0m")
      print("\033[34m1.sinh\033[0m")
      print("\033[34m2.cosh\033[0m")
      print("\033[34m3.tanh\033[0m")
      print("\033[34m4.asin\033[0m")
      print("\033[34m5.acos\033[0m")
      print("\033[34m6.atan\033[0m")
      print("\033[34m7.Back to scientific menu\033[0m") 
      choice = intValidate(input("Please Enter A Choice:"))
      if not intValidate(choice):
          print("\033[91mError:  Enter integer numbers only\033[0m")
          time.sleep(3)
          os.system("cls")
          continue
      elif choice <1 or choice>7:
          print("\033[91mError:Select A number within the menu range\033[0m")
          time.sleep(3)
          os.system("cls")
          continue    
      if choice == 1:
             result,userInput = hyperbolic("sinh")
             print("The answer is ",result)
             logCalc("scientific","sinh",userInput,result)
             print("Result logged to history ✅")
             time.sleep(3)
                 
      elif choice == 2:
             result,userInput = hyperbolic("cosh")
             print("The answer is ",result)
             logCalc("scientific","cosh",userInput,result)
             print("Result logged to history ✅")
             time.sleep(3)
             
      elif choice == 3:
             result,userInput = hyperbolic("tanh")
             print("The answer is ",result)
             logCalc("scientific","tanh",userInput,result)
             print("Result logged to history ✅")
             time.sleep(3)
      elif choice == 4:
             result,userInput = hyperbolic("asin")
             print("The answer is ",result)
             logCalc("scientific","asin",userInput,result)
             print("Result logged to history ✅")
             time.sleep(3)
      elif choice == 5:
             result,userInput = hyperbolic("acos")
             print("The answer is ",result)
             logCalc("scientific","acos",userInput,result)
             print("Result logged to history ✅")
             time.sleep(3)
      elif choice == 6:
             result,userInput = Trigonometric("atan")
             print("The answer is ",result)
             logCalc("scientific","atan",userInput,result)
             print("Result logged to history ✅")
             time.sleep(3)
      elif choice == 7:
             print("Returning to scientific menu...")
             time.sleep(2)
             break
         
def trigonometric_menu():
    """ Handles trigonometric menu functions """
    os.system("cls")
    while True:
      print("\033[33mTrigonometric Menu:\033[0m")
      print("\033[34m1.sin\033[0m")
      print("\033[34m2.cos\033[0m")
      print("\033[34m3.tan\033[0m")
      print("\033[34m4.Back to scientific menu\033[0m")
    
      choice = intValidate(input("Please Enter A Choice:"))
      if not intValidate(choice):
          print("\033[91mError:  Enter integer numbers only\033[0m")
          time.sleep(3)
          os.system("cls")
          continue
      elif choice <1 or choice>4:
          print("\033[91mError:Select A number within the menu range\033[0m")
          time.sleep(3)
          os.system("cls")
          continue    
      if choice == 1:
             result,userInput = Trigonometric("sin")
             print("The answer is ",result)
             logCalc("scientific","sin",userInput,result)
             print("Result logged to history ✅")
             time.sleep(3)
             
                 
      elif choice == 2:
             result,userInput = Trigonometric("cos")
             print("The answer is ",result)
             logCalc("scientific","cos",userInput,result)
             print("Result logged to history ✅")
             time.sleep(3)
             
      elif choice == 3:
             result,userInput = Trigonometric("tan")
             print("The answer is ",result)
             logCalc("scientific","cos",userInput,result)
             print("Result logged to history ✅")
             time.sleep(3)
      elif choice == 4:
             print("Returning to scientific menu...")
             time.sleep(2)
             break

        

def Trigonometric(trig_faunction) : 
    Degrees_or_radians = input('Degrees or radians? ')
    value = eval(input('Enter value: '))
    if Degrees_or_radians == 'Degrees' and not trig_faunction.startswith('a') : 
        value = radians(value)
    if trig_faunction  ==  'sin' :
        return sin(value),value 
    elif trig_faunction  ==  'cos' :
        return cos(value),value
    elif trig_faunction  ==  'tan' : 
        value = round(degrees(value) ,3)
        while value >360  : 
            value = value - 360 
        while value <0 : 
            value = value +360 
        if value == 90 or value == 270 :
            return 'undefined'
        else : 
            return tan(radians(value)),value

    elif value  <=1 and value >=  -1 and (trig_faunction == 'asin' or trig_faunction == 'acos'):
        if trig_faunction  ==  'asin' :
         result =  asin(value) 
        elif trig_faunction  ==  'acos' :
         result =  acos(value) 
    elif trig_faunction  ==  'atan' :
         result =  atan(value)
    if Degrees_or_radians == 'Degrees' : 
          return degrees(result)
    return result,value
def main() : 
   q = input('function')
   a = eval(input('value'))
   b = eval(input('value2')) 
   print(loge(q,a,b))


def factorial_function(n) :
    return factorial(n) 

def loge(*x) :
    exorlog = x[0] 
    if exorlog == 'e' : 
        powerr = x[1]
        return exp(powerr) 
    elif exorlog == 'log' :
     hart = x[1] 
     base = x[2]
     if hart >0 and base >0 and base !=1 :
      return log(hart, base)  
def hyperbolic(hyperbolic_function) : 
    value = eval(input('Enter value: '))
    if hyperbolic_function  ==  'sinh' :
        return sinh(value),value
    elif hyperbolic_function  ==  'cosh' :
        return cosh(value),value
    elif hyperbolic_function  ==  'tanh' : 
        return tanh(value),value
    elif hyperbolic_function  ==  'asinh' :
         return asinh(value),intValidate
    elif hyperbolic_function  ==  'acosh' and value >=1 :
         return acosh(value),value
    elif hyperbolic_function  ==  'atanh' and value <1 and value > -1:
         return atanh(value),value



        








