from modules import scientific, programmer, standard, converter
from validations.dataTypes import intValidate
import os
file_path = os.path.join(os.path.dirname(__file__), "utils", "history.csv") # adding history file to the path to open
import time
def main_menu():
    os.system('cls')
    try:
     while True:
    
      print("\033[33mWelcome to Multi-Mode CLI Calculator\033[0m\n\033[34m1.Standarrd Mode\n2.Programmer Mode\n3.Scientific Mode\n4.Converter Mode\n5.Calculations History\n6.Exit\033[0m")   
      choice = intValidate(input("Please Enter A Choice:"))
      if not choice:
          print("\033[91mError:  Enter integer numbers only\033[0m")
          time.sleep(3)
          os.system("cls")
          continue
      elif choice <1 or choice>6:
          print("\033[91mError:Select A number within the menu range\033[0m")
          time.sleep(3)
          os.system("cls")
          continue
      if choice == 1:
          os.system("cls")
          standard.standard_menu()
          os.system("cls")
      if choice == 2:
          os.system("cls")
          programmer.programmer_menu()
          os.system("cls")
      if choice == 3:
          os.system("cls")
          scientific.scintific_menu()
          os.system("cls")
      if choice == 4:
          os.system("cls")
          converter.converter_menu()
          os.system("cls")
      if choice == 5: # choice of history of calculations
          file_path = os.path.join(os.path.dirname(__file__), "utils", "history.csv")
          print("History File Opening...")
          os.startfile(file_path)
          time.sleep(4)
          os.system("cls")
          continue
      if choice == 6:
          print("Thanks for using Multi-Mode CLI calculator\n Program exit...")
          break
    except KeyboardInterrupt:
        print("\nProgram closed....")
     
main_menu()
