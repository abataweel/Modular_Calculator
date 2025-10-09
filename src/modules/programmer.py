#from validations.validators import *
"""
Programmer Calculator Module
Handles base conversions and bitwise operations

"""

def programmer_menu():
 
    """Main menu for programmer calculator mode"""
    print("="*30)
    print("Programmer Calculator Mode")
    print("="*30) 
    print("1. Base Conversion\n")
    print("2. Bitwise Operations\n")
    print("3. Back to Main Menu")
    
    while True:
        try:
            print("="*30)
            choice = int(input("Select an option (1-3): "))
            if choice == 1:
                base_conversions_menu()
                break
            elif choice == 2:
                value2=bitwise_operations_menu()
                print(value2)
                break
            elif choice == 3:
                return
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue
        except KeyboardInterrupt:
            print("Exiting to Main Menu.")
            return

        break



def base_conversions_menu():

    """ Handles base conversions between Binary, Decimal, Hexadecimal, and Octal """
    print("="*30)
    print("Base Conversion")
    print("="*30)
    print("1. Binary to Decimal/Octal\n")
    print("2. Decimal to Binary/Hexadecimal/Octal\n")
    print("3. Hexadecimal to Binary/Decimal/Octal\n")
    print("4. Octal to Binary/Decimal/Hexadecimal\n")
    print("5. Back to Programmer Menu")

    while True:
        try:
            print("="*30)
            choice=int(input("Select an option (1-5): "))
            if choice == 1:
                binary_to_others_menu()
            elif choice == 2:
                return decimal_to_others_menu()
            elif choice == 3:
                return hexadecimal_to_others_menu()
            elif choice == 4:
                return octal_to_others_menu()
            elif choice == 5:
                return
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        except KeyboardInterrupt:
            print("Exiting to Programmer Menu.")
            return
        break
    
def decimal_to_binary(decimalNumberUser):
    """Convert decimal to binary"""  
    decimalNumber=abs(decimalNumberUser)
    if decimalNumber == 0:
        return "0"
    result=""
    while decimalNumber > 0:
        """
        Example => Decimal 13
        13 / 2 = 6 remainder 1
        6 / 2 = 3 remainder 0
        3 / 2 = 1 remainder 1
        1 / 2 = 0 remainder 1
        Result = 1101
        """
        remainder = decimalNumber % 2 # Get Remainder 0 or 1
        result += str(remainder) # Append Remainder to Result String
        decimalNumber = decimalNumber // 2 # Refresh Decimal Number by Floor Division
    result = result[::-1] # Reverse the Result List to get the correct order
    return result

def decimal_to_hexadecimal(decimalNumberUser):
    """Convert decimal to hexadecimal"""
    try:
        decimalNumber=abs(decimalNumberUser)

        if decimalNumber == 0:
            return "0"
                
        result=""
        hex_chars = "0123456789ABCDEF"  # Hexadecimal characters
        while decimalNumber > 0:
            """
            Example => Decimal 254
            254 / 16 = 15 remainder 14 (E)
            15 / 16 = 0 remainder 15 (F)
            Result = FE
            """
            remainder = decimalNumber % 16 # Get Remainder between 0-15
            result += hex_chars[remainder] # Append Corresponding Hex Character to Result String
            decimalNumber = decimalNumber // 16 # Refresh Decimal Number by Floor Division
        result = result[::-1] # Reverse the Result to get the correct order
        return result
    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")
        return
    except KeyboardInterrupt:
        print("Exiting to Base Conversion Menu.")
        return
    except TypeError:
        print("Invalid input. Please enter a valid decimal number.")
        return

def decimal_to_others_menu():
    """ Converts Decimal to Binary, Hexadecimal, and Octal """
    print("="*30)
    print("1. Decimal to Binary")
    print("2. Decimal to Hexadecimal")
    print("3. Decimal to Octal")
    print("4. Back to Base Conversion Menu")
    while True:
        try:
            print("="*30)
            choice=int(input("Select an option (1-4): "))
            if choice == 1:
                decimalNumberUser=int(input("Enter a Decimal number: "))
                return print("Binary:",decimal_to_binary(decimalNumberUser))
            
            elif choice == 2:
                """Convert decimal to hexadecimal"""
                decimalNumberUser=int(input("Enter a Decimal number: "))
                return print("Hexadecimal:",decimal_to_hexadecimal(decimalNumberUser)) 
            

            elif choice == 3:
                return 
            elif choice == 4:
                return
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        except KeyboardInterrupt:
            print("Exiting to Base Conversion Menu.")
            return


def octal_to_Decimal(octal_number):
    octal_number = str(octal_number)
    octal_number = octal_number[::-1]
    decimal_number = 0
    try:
        for i in range(len(octal_number)):
            # since octal is base 8 we have 8**i for evrey index
            # multiply by the number in the same index  
            # for example number: 70 we reverse the number to 07
            # then (8**0 *0)(loop1) +8**1 * 7(loop2)= 56  
            if int(octal_number[i]) <= 7: # check if it's a valid digit
                decimal_number += 8**i * int(octal_number[i])
            else:
                print('Octal number can’t have 8 or 9, please enter a number that has only 0–7.')
                return
        return decimal_number
    except ValueError:
        print('Invalid input. Octal number has digits range of 0..7.')
        return
    except KeyboardInterrupt:
        print("Exiting to Base Conversion Menu.")
        return

def octal_to_others_menu():
    #Converts Octal to Decimal,Binary and Hexadecimal
    print("="*30)
    print("1. Octal to Decimal")
    print("2. Octal to Hexadecimal")
    print("3. Octal to Binary")
    print("4. Back to Base Conversion Menu")
    while True :
        try:
            print("="*30)
            choise = int(input(" Select an option (1-4): "))
            if choise==1:
                octal_number = input('Enter your octal number: ')
                return print('Octal:',octal_to_Decimal(octal_number))

            elif choise==2:
                octal_number = input('Enter your octal number ')
                decimal_number=octal_to_Decimal(octal_number)
                if decimal_number is None:
                    return
                print('Hexadecimal:',decimal_to_hexadecimal(decimal_number))
                return

            elif choise==3:
                octal_number = input('Enter your octal number ')
                decimal_number=octal_to_Decimal(octal_number)
                if decimal_number is None:
                    return
                print('Binary:',decimal_to_binary(decimal_number))
                return

            elif choise==4:
                print("Returning to Base Conversion Menu...")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        except KeyboardInterrupt:
             print("Exiting to Base Conversion Menu.")
             return     

def hexChar_To_Decimal(ch):
    if 'A' <= ch <= 'F': # Check if it's a number between A-F or 0-9
        return 10 + (ord(ch) - ord('A'))
    else:
        return ord(ch) - ord('0')

def hexadecimal_to_decimal(hex_string):
    """Convert a hexadecimal string to a decimal integer."""
    try:
        decimalValue = 0
        hex_string = hex_string[::-1]  # Reverse the string to process numbers correctly
        
        for i in range(len(hex_string)):
            ch = hex_string[i]
            if 'A' <= ch <= 'F' or '0' <= ch <= '9': # Check if it's a valid hex character
                decimalValue += 16**i*hexChar_To_Decimal(ch) # transform hex to decimal by taking the sum of
            else:                                            #  16**i * value of char at index i
                raise ValueError() # flag invalid hexadecimal character

        return decimalValue
    except ValueError:
        print("Invalid hexadecimal number, hexadecimal numbers go from 0-9,a-f.")
        return
    except KeyboardInterrupt:
        print("Exiting to Base Conversion Menu.")
        return

def hexadecimal_to_others_menu():
    # Converts Hexadecimal to Binary, Decimal and Octal
    print("="*30)
    print("Hexadecimal to Others Conversion Menu")
    print("1. Hexadecimal to Decimal")
    print("2. Hexadecimal to Binary")
    print("3. Hexadecimal to Octal")
    print("4. Back to Main Menu")
    while True:
        try:
            print('=' * 30)
            choice = int(input("Select an option (1-4): "))
            if choice==1:
                hex_string = input("Enter a hexadecimal number: ").upper()
                return print('Hexadecimal:',hexadecimal_to_decimal(hex_string))
                

            elif choice==2:
                hex_string = input("Enter a hexadecimal number: ").upper()
                decimal_number=hexadecimal_to_decimal(hex_string)
                if decimal_number is None:
                    return
                print('Binary:',decimal_to_binary(decimal_number))
                return

            elif choice==3:
                return

            elif choice==4:
                print("Returning to Base Conversion Menu...")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        except KeyboardInterrupt:
             print("Exiting to Base Conversion Menu.")
             return      

def bitwise_operations_menu():
    """Handles bitwise operations: AND, OR, XOR, NOT, Left Shift, Right Shift"""
    print("="*30)
    print("Bitwise Operations Menu")
    print("="*30)
    print("1. AND")
    print("2. OR")
    print("3. XOR")
    print("4. NOT")
    print("5. Left Shift")
    print("6. Right Shift")
    print("7. Back to Programmer Menu")

    while True:
        try:
            print("="*30)
            choice = int(input("Select an option (1-7): "))
            if choice == 1:
                a = int(input("Enter first integer: "))
                b = int(input("Enter second integer: "))
                return f"{a} & {b} = {a & b}"
            elif choice == 2:
                a = int(input("Enter first integer: "))
                b = int(input("Enter second integer: "))
                return f"{a} | {b} = {a | b}"
            elif choice == 3:
                a = int(input("Enter first integer: "))
                b = int(input("Enter second integer: "))
                return f"{a} ^ {b} = {a ^ b}"
            elif choice == 4:
                a = int(input("Enter an integer: "))
                return f"~{a} = {~a}"
            elif choice == 5:
                a = int(input("Enter an integer: "))
                n = int(input("Enter number of positions to shift left: "))
                return f"{a} << {n} = {a << n}"
            elif choice == 6:
                a = int(input("Enter an integer: "))
                n = int(input("Enter number of positions to shift right: "))
                return f"{a} >> {n} = {a >> n}"
            elif choice == 7:
                return
            else:
                print("Invalid choice. Please select a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter valid integers and options.")
            continue
        except KeyboardInterrupt:
            print("Exiting to Programmer Menu.")
            return

programmer_menu()

 