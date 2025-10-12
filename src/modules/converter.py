import time, os
from validations.dataTypes import intValidate,floatValidate
from utils.calculationsHistory import logCalc
def _get_float(prompt):
    """Ask until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

def converter_menu():
    while True:
        os.system('cls')
        print("\033[33mConverter Menu:\033[0m")
        print("\033[34m1.Length")
        print("2.Weight")
        print("3.Temperature")
        print("4.Back\033[0m")
        choice = intValidate(input("Please Enter A Choice:"))
        if not choice:
            print("\033[91mError: Enter integer numbers only\033[0m")
            time.sleep(2)
            continue
        elif choice < 1 or choice > 4:
            print("\033[91mError: Select A number within the menu range\033[0m")
            time.sleep(2)
            continue    

        if choice == 4:
            print("Returning to main menu...")
            time.sleep(2)
            break
        elif choice == 1:
            _length_converter()
        elif choice == 2:
            _weight_converter()
        elif choice == 3:
            _temperature_converter()
 
def _length_converter():
    print("\033[33mLength Converter Mode\033[0m")
    print("\033[34m1.Meters to Centimeters")
    print("2.Centimeters to Meters")
    print("3.Meters to Kilometers")
    print(".Kilometers to Meters")
    print("5.Back to converter menu\033[0m")
    while True:
        choice = intValidate(input("Please Enter A Choice:"))
        if not choice:
           print("\033[91mError: Enter integer numbers only\033[0m")
           time.sleep(2)
           continue
        elif choice < 1 or choice > 5:
            print("\033[91mError: Select A number within the menu range\033[0m")
            time.sleep(2)
            continue    
        
        if choice == 5:
            print("Returning to converter menu...")
            time.sleep(2)
            break
        elif choice == 1:
            x = _get_float("Meters: ")
            print(f"Result: {x * 100} cm")
        elif choice == "2":
            x = _get_float("Centimeters: ")
            print(f"Result: {x / 100} m")
        elif choice == "3":
            x = _get_float("Meters: ")
            print(f"Result: {x / 1000} km")
        elif choice == "4":
            x = _get_float("Kilometers: ")
            print(f"Result: {x * 1000} m")
        else:
            print("Invalid choice.")
            
def _weight_converter():
    print("\033[33mWeight Converter Mode:\033[0m")
    print("1.Kilograms to Grams")
    print("2.Grams to Kilograms")
    print("3.Kilograms to Pounds")
    print("4.Pounds to Kilograms")
    print("5.Back to converter menu")
    while True:
        choice = input("Choice: ").strip()
        if choice == "0":
            return
        elif choice == "1":
            x = _get_float("Kilograms: ")
            print(f"Result: {x * 1000} g")
        elif choice == "2":
            x = _get_float("Grams: ")
            print(f"Result: {x / 1000} kg")
        elif choice == "3":
            x = _get_float("Kilograms: ")
            print(f"Result: {x * 2.20462} lb")
        elif choice == "4":
            x = _get_float("Pounds: ")
            print(f"Result: {x / 2.20462} kg")
        else:
            print("Invalid choice.")       
            
def _temperature_converter():
    print("\n[Temperature Converter]")
    print("1) Celsius to Fahrenheit")
    print("2) Fahrenheit to Celsius")
    print("3) Celsius to Kelvin")
    print("4) Kelvin to Celsius")
    print("0) Back")
    while True:
        choice = input("Choice: ").strip()
        if choice == "0":
            return
        elif choice == "1":
            x = _get_float("Celsius: ")
            print(f"Result: {(x * 9/5) + 32} F")
        elif choice == "2":
            x = _get_float("Fahrenheit: ")
            print(f"Result: {(x - 32) * 5/9} C")
        elif choice == "3":
            x = _get_float("Celsius: ")
            print(f"Result: {x + 273.15} K")
        elif choice == "4":
            x = _get_float("Kelvin: ")
            print(f"Result: {x - 273.15} C")
        else:
            print("Invalid choice.")
