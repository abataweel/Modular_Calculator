
#constants
#we convert everything to the base then to the required unit
import time, os,sys
from validations.dataTypes import intValidate,strValidate
from utils.calculationsHistory import logCalc
FT_IN_M = 0.3048
IN_IN_M = 0.0254
LB_IN_KG = 0.45359237
OZ_IN_KG = 0.0283495
###################################### MENUS ################
def converter_menu():
    while True:
        os.system("cls")
        print("\033[33mConverter Mode:\033[0m")
        print("\033[34m1.Length")
        print("2.Weight")
        print("3.Temperature")
        print("4.Volume (optional)")
        print("5.Back/Exit\033[0m")
        choice = intValidate(input("Please Enter A Choice:"))
        if choice is None:
            print("\033[91mError: Enter integer numbers only\033[0m")
            time.sleep(2)
            continue
        elif choice < 1 or choice > 5:
            print("\033[91mError: Select A number within the menu range\033[0m")
            time.sleep(2)
            continue  
        if choice == 5:
            print("Returning to main menu...")
            time.sleep(2)
            break
        elif choice == 1:
            length_menu()
        elif choice == 2:
            weight_menu()
        elif choice == 3:
            temperature_menu()
            
            
def temperature_menu():
    print("\nTemperature units: C, F, K")
    f = get_unit("From", ["c", "f", "k"])   #from
    t = get_unit("To",   ["c", "f", "k"])   # to
    v = get_float("Value: ")
    res = from_kelvin(to_kelvin(v, f), t)
    print('Result:', fmt(res), t.upper())

def weight_menu():
    print("\n[Weight] units: kg, g, lb, oz")
    f = get_unit("From", ["kg", "g", "lb", "oz"])
    t = get_unit("To",   ["kg", "g", "lb", "oz"])
    v = get_value("Value: ", nonneg=True)
    res = from_kg(to_kg(v, f), t)
    print(f"Result: {fmt(res)} {t}")
    
def length_menu():
    print("\n[Length] units: m, cm, ft, in")
    f = get_unit("From", ["m", "cm", "ft", "in"])
    t = get_unit("To",   ["m", "cm", "ft", "in"])
    v = get_value("Value: ", nonneg=True)
    res = from_meters(to_meters(v, f), t)
    print("Result:", fmt(res), t)
    #logCalc("scientific","trig",userInput,result)
    print("Result logged to history ✅")
    time.sleep(2)
    
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: enter a number.")

def get_unit(prompt, allowed):
    while True:
        u = input(f"{prompt} {allowed}: ").strip().lower()
        if u in allowed:
            return u
        print(f"Error: unknown unit. Units supported: {allowed}")

def get_value(prompt, nonneg=False):
    while True:
        v = get_float(prompt)
        if not nonneg or v >= 0:
            return v
        print("Error: value must be non-negative.")

def fmt(x):
    return f"{x:.2f}"
#------

# length meter is the base
def to_meters(value, unit):
    if unit == "m":  return value
    if unit == "cm": return value / 100
    if unit == "ft": return value * FT_IN_M
    if unit == "in": return value * IN_IN_M

def from_meters(m, unit):
    if unit == "m":  return m
    if unit == "cm": return m * 100
    if unit == "ft": return m / FT_IN_M
    if unit == "in": return m / IN_IN_M

 
#  weight :kilogram is the base
def to_kg(value, unit):
    if unit == "kg": return value
    if unit == "g":  return value / 1000
    if unit == "lb": return value * LB_IN_KG
    if unit == "oz": return value * OZ_IN_KG

def from_kg(kg, unit):
    if unit== "kg": return kg
    if unit== "g":  return kg * 1000
    if unit== "lb": return kg / LB_IN_KG
    if unit == "oz": return kg / OZ_IN_KG


# temperature Kelvin is the base
def to_kelvin(x, unit):
    unit = unit.lower()
    if unit == "k": return x
    if unit == "c": return x + 273.15
    if unit == "f": return (x - 32) * 5/9 + 273.15

def from_kelvin(k, unit):
    unit = unit.lower()
    if unit == "k": return k
    if unit == "c": return k - 273.15
    if unit == "f": return (k - 273.15) * 9/5 + 32