
#constants
#we convert everything to the base then to the required unit
FT_IN_M = 0.3048
IN_IN_M = 0.0254
LB_IN_KG = 0.45359237
OZ_IN_KG = 0.0283495

def _get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: enter a number.")

def _get_unit(prompt, allowed):
    while True:
        u = input(f"{prompt} {allowed}: ").strip().lower()
        if u in allowed:
            return u
        print(f"Error: unknown unit. Units supported: {allowed}")

def _get_value(prompt, nonneg=False):
    while True:
        v = _get_float(prompt)
        if not nonneg or v >= 0:
            return v
        print("Error: value must be non-negative.")

def _fmt(x):
    return f"{x:.2f}"
#------

# length meter is the base
def _to_meters(value, unit):
    if unit == "m":  return value
    if unit == "cm": return value / 100
    if unit == "ft": return value * FT_IN_M
    if unit == "in": return value * IN_IN_M

def _from_meters(m, unit):
    if unit == "m":  return m
    if unit == "cm": return m * 100
    if unit == "ft": return m / FT_IN_M
    if unit == "in": return m / IN_IN_M

def _length_menu():
    print("\n[Length] units: m, cm, ft, in")
    f = _get_unit("From", ["m", "cm", "ft", "in"])
    t = _get_unit("To",   ["m", "cm", "ft", "in"])
    v = _get_value("Value: ", nonneg=True)
    res = _from_meters(_to_meters(v, f), t)
    print("Result:", _fmt(res), t)

#  weight :kilogram is the base
def _to_kg(value, unit):
    if unit == "kg": return value
    if unit == "g":  return value / 1000
    if unit == "lb": return value * LB_IN_KG
    if unit == "oz": return value * OZ_IN_KG

def _from_kg(kg, unit):
    if unit== "kg": return kg
    if unit== "g":  return kg * 1000
    if unit== "lb": return kg / LB_IN_KG
    if unit == "oz": return kg / OZ_IN_KG


def _weight_menu():
    print("\n[Weight] units: kg, g, lb, oz")
    f = _get_unit("From", ["kg", "g", "lb", "oz"])
    t = _get_unit("To",   ["kg", "g", "lb", "oz"])
    v = _get_value("Value: ", nonneg=True)
    res = _from_kg(_to_kg(v, f), t)
    print(f"Result: {_fmt(res)} {t}")


# temperature Kelvin is the base
def _to_kelvin(x, unit):
    unit = unit.lower()
    if unit == "k": return x
    if unit == "c": return x + 273.15
    if unit == "f": return (x - 32) * 5/9 + 273.15

def _from_kelvin(k, unit):
    unit = unit.lower()
    if unit == "k": return k
    if unit == "c": return k - 273.15
    if unit == "f": return (k - 273.15) * 9/5 + 32

def _temperature_menu():
    print("\nTemperature units: C, F, K")
    f = _get_unit("From", ["c", "f", "k"])   #from
    t = _get_unit("To",   ["c", "f", "k"])   # to
    v = _get_float("Value: ")
    res = _from_kelvin(_to_kelvin(v, f), t)
    print('Result:', _fmt(res), t.upper())


def main_menu():
    while True:
        print("\n---Converter Mode---")
        print("1) Length")
        print("2) Weight")
        print("3) Temperature")
        print("4) Volume (optional)")
        print("0) Back/Exit")
        choice = input("Which option would you like to choose? (Type the number): ").strip()
        if choice == "0":
            return
        elif choice == "1": _length_menu()
        elif choice == "2": _weight_menu()
        elif choice == "3": _temperature_menu()
        else: print("Invalid choice.")

main_menu()

