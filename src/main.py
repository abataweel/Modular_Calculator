from modules import scientific,programmer,standard,converter
from utils.calculationsHistory import logCalc


def main_menu():
    while True:
     print("Welcome to Multi-Mode CLI Calculator\n1.Standarrd Mode\n2.Programmer Mode\n3.Scientific Mode\n4.Converter Mode\n5.Calculations History\n6.Exit")   
     choice = input("Please Enter A Choice:")
     if not isinstance(choice,int):
         print("\033[91mError:  Enter numbers only\033[0m")
         continue
     logCalc("scintific","sin","3","2")
     
main_menu()
