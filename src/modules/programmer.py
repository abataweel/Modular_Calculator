"""
Programmer Calculator Module
Handles base conversions and bitwise operations

"""
from validations.dataTypes import intValidate,strValidate,floatValidate
from utils.calculationsHistory import logCalc
import os,time,sys
# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def programmer_menu():
    """Main menu for programmer calculator mode"""
    while True:
            os.system('cls')
            print("\033[33mProgrammer Mode:\033[0m")
            print("\033[34m1. Base Conversion\033[0m")
            print("\033[34m2. Bitwise Operations\033[0m")
            print("\033[34m3. Back to Main Menu\033[0m")
        
            choice = intValidate(input("Select an option (1-3): "))
            if choice is None:
                print("\033[91mError: Please enter letters only.\033[0m")
                time.sleep(2)
                continue
            elif choice <1 or choice>3:
                   print("\033[91mError:Select A number within the menu range\033[0m")
                   time.sleep(2)
                   continue
            if choice == 1:
                base_conversions_menu()
            elif choice == 2:
                 bitwise_operations_menu()
                 
            elif choice == 3:
                print("Returning to Main Menu...")
                time.sleep(1.5)
                break
        

        
""" Handles base conversions between Binary, Decimal, Hexadecimal, and Octal """
def base_conversions_menu():
    while True:
        
            os.system('cls')
            print("\033[33mBase Conversion Mode:\033[0m")
            print("\033[34m1. Convert from binary\033[0m")
            print("\033[34m2. Convert from decimal\033[0m")
            print("\033[34m3. Convert from octal\033[0m")
            print("\033[34m4. Convert from hexadecimal\033[0m")
            print("\033[34m5. Back to Programmer Menu\033[0m")
     
            choice=intValidate(input("Select an option (1-5): "))
            if choice is None:
                print("\033[91mError: Please enter letters only.\033[0m")
                time.sleep(2)
                continue
            elif choice <1 or choice>5:
                   print("\033[91mError:Select A number within the menu range\033[0m")
                   time.sleep(2)
                   continue
            if choice == 1:
                 binary_to_others_menu()
            
            elif choice == 2:
                 decimal_to_others_menu()
            
            elif choice == 3:
                 octal_to_others_menu()
            
            elif choice == 4:
                 hexadecimal_to_others_menu()
            
            elif choice == 5:
                print("Returning to programmer menu...")
                time.sleep(1.5)
                break
           
       
    

def bitwise_operations_menu():
    """Handles bitwise operations: AND, OR, XOR, NOT, Left Shift, Right Shift"""
    while True:
            os.system('cls')
            print("\033[33mBitwise Operations Menu:\033[0m")
            print("\033[34m1. AND\033[0m")
            print("\033[34m2. OR\033[0m")
            print("\033[34m3. XOR\033[0m")
            print("\033[34m4. NOT\033[0m")
            print("\033[34m5. Left Shift\033[0m")
            print("\033[34m6. Right Shift\033[0m")
            print("\033[34m7. Back to Programmer Menu\033[0m")
            choice = intValidate(input("Select an option (1-7): "))
            if choice is None:
                 print("\033[91mError: Please enter letters only.\033[0m")
                 time.sleep(2)
                 continue
            elif choice <1 or choice>7:
                    print("\033[91mError:Select A number within the menu range\033[0m")
                    time.sleep(2)
                    continue
            BinValid = [1,0]
            if choice == 1:
                while True:
                 a = intValidate(input("Enter first integer: "))
                 b = intValidate(input("Enter second integer: "))
                 if a is None or b is None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                #  if a or b not in BinValid:
                #      print("\033[91mError: Please binary numbers only (0,1)\033[0m")
                #      time.sleep(2)
                #      continue
                 result = a & b
                 print(f"The result of {a} & {b} is {result}")
                 logCalc("Programmer","AND",f"{a},{b}",result)
                 break
            
            elif choice == 2:
                while True:
                 a = intValidate(input("Enter first integer: "))
                 b = intValidate(input("Enter second integer: "))
                 if a is None or b is None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                #  if a or b not in BinValid:
                #       print("\033[91mError: Please binary numbers only (0,1)\033[0m")
                #       time.sleep(2)
                #       continue
                 result = a | b
                 print(f"The result of {a} & {b} is {result}")
                 logCalc("Programmer","OR",f"{a},{b}",result)
                 break
            
            elif choice == 3:
                while True:
                 a = intValidate(input("Enter first integer: "))
                 b = intValidate(input("Enter second integer: "))
                 if a is None or b is None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                #  if a or b not in BinValid:
                #      print("\033[91mError: Please binary numbers only (0,1)\033[0m")
                #      time.sleep(2)
                #      continue
                 result = a & b
                 print(f"The result of {a} XOR ^ {b} is {result}")
                 logCalc("Programmer","XOR",f"{a},{b}",result)
                 break
            
            elif choice == 4:
                while True:
                 a = intValidate(input("Enter first integer: "))
                 if a is  None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                #  if a or b not in BinValid:
                #      print("\033[91mError: Please binary numbers only (0,1)\033[0m")
                #      time.sleep(2)
                #      continue
                 result = ~a
                 print(f"The result of {a} ~ NOT {b} is {result}")
                 logCalc("Programmer","NOT",a,result)
                 break
            
            elif choice == 5:
                while True:
                 a = intValidate(input("Enter an integer: "))
                 n = intValidate(input("Enter number of posistions to shift left"))
                 if a  or b is  None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                #  if a  not in BinValid:
                #      print("\033[91mError: Please binary numbers only (0,1)\033[0m")
                #      time.sleep(2)
                #      continue
                 result = a <<n
                 print(f"The result of {a} << let shift {n} positions is {result}")
                 logCalc("Programmer","LEFT SHIFT",a,result)
                 break
            
            elif choice == 6:
                while True:
                 a = intValidate(input("Enter an integer: "))
                 n = intValidate(input("Enter number of posistions to shift right"))
                 if a  or b is  None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                #  if a  not in BinValid:
                #      print("\033[91mError: Please binary numbers only (0,1)\033[0m")
                #      time.sleep(2)
                #      continue
                 result = a <<n
                 print(f"The result of {a} << let shift {n} positions is {result}")
                 logCalc("Programmer","LEFT SHIFT",a,result)
                 break
            
            elif choice == 7:
                print("Returning to Programmer Menu...")
                time.sleep(2)
                break
                  
            


def binary_to_others_menu():
    """ Converts Binary to Decimal, Hexadecimal, and Octal """
    while True:
            os.system('cls')
            print("\033[33mBinary Conversion Menu:\033[0m")
            print("\033[34m1. Binary to Decimal")
            print("\033[34m2. Binary to Octal")
            print("\033[34m3. Binary to Hexadecimal")
            print("\033[34m4. Back to Base Conversion Menu\033[0m")
    
            choice = intValidate(input("Select an option (1-4): "))
            if choice is None:     
                 print("\033[91mError: Please enter letters only.\033[0m")
                 time.sleep(2)
                 continue
            elif choice <1 or choice>4:
                   print("\033[91mError:Select A number within the menu range\033[0m")
                   time.sleep(2)
                   continue
            if choice == 1:
               while True: 
                 binaryNumberUser = intValidate(input("Enter a Binary number: "))
               
                 if binaryNumberUser is  None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                #  if binaryNumberUser not in [1,0]:
                #      print("\033[91mError: Please binary numbers only (0,1)\033[0m")
                #      time.sleep(2)
                #      continue
                 result = binary_to_decimal(binaryNumberUser)
                 print(f"The result of {binary_to_decimal} number to decimal is  {result}")
                 logCalc("Programmer","Bin>Dec",binaryNumberUser,result)
                 time.sleep(3)
                 break

            elif choice == 2:
                while True: 
                 binaryNumberUser = intValidate(input("Enter a Binary number: "))
               
                 if binaryNumberUser is  None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                #  if binaryNumberUser not in [1,0]:
                #      print("\033[91mError: Please binary numbers only (0,1)\033[0m")
                #      time.sleep(2)
                #      continue
                 result = binary_to_octal(binaryNumberUser)
                 print(f"The result of {binary_to_decimal} number to octal is  {result}")
                 logCalc("Programmer","Bin>Oct",binaryNumberUser,result)
                 time.sleep(3)
                 break
            
            elif choice == 3:
               while True: 
                 binaryNumberUser = intValidate(input("Enter a Binary number: "))
               
                 if binaryNumberUser is  None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                #  if binaryNumberUser not in [1,0]:
                #      print("\033[91mError: Please binary numbers only (0,1)\033[0m")
                #      time.sleep(2)
                #      continue
                 result = binary_to_hexadecimal(binaryNumberUser)
                 print(f"The result of {binary_to_decimal} number to hexadecimal is {result}")
                 logCalc("Programmer","Bin>Hex",binaryNumberUser,result)
                 time.sleep(3)
                 break

            elif choice == 4:
                  print("Returning to Base Conversion Menu...")
                  time.sleep(2)
                  break
              
            
    """ Converts Decimal to Binary, Hexadecimal, and Octal """

def decimal_to_others_menu():
   while True:
            os.system('cls')
            print("\033[33mDecimal Conversion Menu:\033[0m")
            print("\033[34m1. Decimal to Binary\033[0m")
            print("\033[34m2. Decimal to Octal\033[0m")
            print("\033[34m3. Decimal to Hexadecimal\033[0m")
            print("\033[34m4. Back to Base Conversion Menu\033[0m")
    
        
            choice=intValidate(input("Select an option (1-4): "))
            if choice is None:    
                 print("\033[91mError: Please enter letters only.\033[0m")
                 time.sleep(2)
                 continue
            elif choice <1 or choice>4:
                   print("\033[91mError:Select A number within the menu range\033[0m")
                   time.sleep(2)
                   continue
            if choice == 1:
                while True: 
                 decimalNumberUser = intValidate(input("Enter a decimal number: "))
                 if decimalNumberUser is  None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                 result = decimal_to_binary(decimalNumberUser)
                 print(f"The result of {decimalNumberUser} number to Binary is {result}")
                 logCalc("Programmer","Dec>Bin",decimalNumberUser,result)
                 time.sleep(3)
                 break
            
            elif choice == 2:
                while True: 
                 decimalNumberUser = intValidate(input("Enter a decimal number: "))
                 if decimalNumberUser is  None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                 result = decimal_to_octal(decimalNumberUser)
                 print(f"The result of {decimalNumberUser} number to octal is {result}")
                 logCalc("Programmer","Dec>Oct",decimalNumberUser,result)
                 time.sleep(3)
                 break
            
            elif choice == 3:
               while True: 
                 decimalNumberUser = intValidate(input("Enter a decimal number: "))
                 if decimalNumberUser is  None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                 result = decimal_to_hexadecimal(decimalNumberUser)
                 print(f"The result of {decimalNumberUser} number to hexadecimal is {result}")
                 logCalc("Programmer","Dec>Hex",decimalNumberUser,result)
                 time.sleep(3)
                 break
            
            elif choice == 4:
                  print("Returning to Base Conversion Menu...")
                  time.sleep(2)
                  break
        
""" Converts Octal to Decimal,Binary and Hexadecimal """

def octal_to_others_menu():
   while True:
            os.system('cls')
            print("\033[33mOctal Conversion Menu:\033[0m")
            print("\033[34m1. Octal to Decimal\033[0m")
            print("\033[34m2. Octal to Hexadecimal\033[0m")
            print("\033[34m3. Octal to Binary\033[0m")
            print("\033[34m4. Back to Base Conversion Menu\033[0m")
            choise = intValidate(input(" Select an option (1-4): "))
            if choise is None:    
                 print("\033[91mError: Please enter letters only.\033[0m")
                 time.sleep(2)
                 continue
            elif choise <1 or choise>4:
                   print("\033[91mError:Select A number within the menu range\033[0m")
                   time.sleep(2)
                   continue
            if choise==1:
               while True: 
                 octalNumber = intValidate(input("Enter a octal number: "))
                 if octalNumber is  None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                 result = octal_to_Decimal(octalNumber)
                 print(f"The result of {octalNumber} number to decimal is {result}")
                 logCalc("Programmer","Oct>Dec",octalNumber,result)
                 time.sleep(3)
                 break
            

            elif choise==2:
                while True: 
                 octalNumber = intValidate(input("Enter a octal number: "))
                 if octalNumber is  None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                 result = octal_to_hexadecimal(octalNumber)
                 print(f"The result of {octalNumber} number to hexadecimal is {result}")
                 logCalc("Programmer","Oct>Hex",octalNumber,result)
                 time.sleep(3)
                 break
            
            elif choise==3:
                while True: 
                 octalNumber = intValidate(input("Enter a octal number: "))
                 if octalNumber is  None:
                     print("\033[91mError: Please enter numbers only.\033[0m")
                     time.sleep(2)
                     continue
                 result = octal_to_binary(octalNumber)
                 print(f"The result of {octalNumber} number to binary is {result}")
                 logCalc("Programmer","Oct>Bin",octalNumber,result)
                 time.sleep(3)
                 break
            

            elif choise==4:
                  print("Returning to Base Conversion Menu...")
                  time.sleep(2)
                  break
            

""" Converts Hexadecimal to Binary, Decimal and Octal """
def hexadecimal_to_others_menu():
   while True:
            os.system('cls')
            print("\033[33mHexadecimal Conversion Menu:\033[0m")
            print("\033[34m1. Hexadecimal to Decimal\033[0m")
            print("\033[34m2. Hexadecimal to Binary\033[0m")
            print("\033[34m3. Hexadecimal to Octal\033[0m")
            print("\033[34m4. Back to Main Menu\033[0m")    
            choice = intValidate(input("Select an option (1-4): "))
            if choice is None:    
                 print("\033[91mError: Please enter letters only.\033[0m")
                 time.sleep(2)
                 continue
            elif choice <1 or choice>4:
                   print("\033[91mError:Select A number within the menu range\033[0m")
                   time.sleep(2)
                   continue
            if choice==1:
                hex_string = input("Enter a hexadecimal number: ").upper()
                if hexadecimal_to_decimal(hex_string) is not None:
                    result = hexadecimal_to_decimal(hex_string)
                    print(f"The result of {hex_string}  to decimal is {result}")
                    logCalc("Programmer","Hex>Dec",hex_string,result)
                    time.sleep(3)
                
            elif choice==2:
                hex_string = input("Enter a hexadecimal number: ").upper()
                if hexadecimal_to_binary(hex_string) is not None:
                    result = hexadecimal_to_binary(hex_string)
                    print(f"The result of {hex_string}  to binary is {result}")
                    logCalc("Programmer","Hex>Bin",hex_string,result)
                    time.sleep(3)

            elif choice==3:
                hex_string = input("Enter a hexadecimal number: ").upper()
                if hexadecimal_to_octal(hex_string) is not None:
                    result = hexadecimal_to_octal(hex_string)
                    print(f"The result of {hex_string}  to octal is {result}")
                    logCalc("Programmer","Hex>Oct",hex_string,result)
                    time.sleep(3)

            elif choice==4:
                print("Returning to Base Conversion Menu...")
                time.sleep(2)
                break
             


def binary_to_decimal(binaryNumberUser):
    """ Convert Binary to Decimal """

    # Check if binaryNumberUser is a valid binary number
    checkBinary = binaryNumberUser
    while checkBinary > 0:
        if checkBinary % 10 > 1:
            print("Error: Not binary")
            return
        checkBinary = checkBinary // 10

    try:
        binary_number = abs(binaryNumberUser)
        if binary_number == 0:
            return "0"
        
        result = 0
        power = 0
        while binary_number > 0:
            """
            Example => Binary 0110
            (0110 % 10) * (2 ** i) remainder 0
            (0011 % 10) * (2 ** i) remainder 1
            (0001 % 10) * (2 ** i) remainder 1
            (0000 % 10) * (2 ** i) remainder 1
            (0000 % 10) * (2 ** i) remainder 0
            Result = 6
            0*2**0 + 1*2**1 + 1*2**2 + 0*2**3 = 6
            0 + 2 + 4 + 0 = 6
            """
            digit = binary_number % 10
            if digit == 1:
                result += 2 ** power
            binary_number = binary_number // 10
            power += 1

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



def binary_to_octal(binaryNumberUser):
    """ Convert Binary to Octal """
    
    # Check if binaryNumberUser is a valid binary number
    checkBinary = binaryNumberUser
    while checkBinary > 0:
        if checkBinary % 10 > 1:
            print("Error: Not binary")
            return
        checkBinary = checkBinary // 10

    # convert to decimal first then to octal
    """ Example => Binary 1000001
    1*2**6 + 0*2**5 + 0*2**4 + 0*2**3 + 0*2**2 + 1*2**1 + 1*2**0 = 65
    64 + 0 + 0 + 0 + 0 + 2 + 1 = 65
    Result= 65
    """
    try:
        decimal_number = abs(binary_to_decimal(binaryNumberUser))
        if decimal_number == 0:
            return "0"

        octal_result = ""
        while decimal_number > 0:
            """
            Example => Decimal 65
            65 / 8 = 8 remainder 1
            8 / 8 = 1 remainder 0
            1 / 8 = 0 remainder 1
            Result = 101
            """
            remainder = decimal_number % 8
            octal_result += str(remainder)
            decimal_number = decimal_number // 8

        return octal_result
    
    except ValueError:
            print("Invalid input. Please enter a valid binary number.")
            return
    except KeyboardInterrupt:
            print("Exiting to Base Conversion Menu.")
            return
    except TypeError:
            print("Invalid input. Please enter a valid binary number.")
            return



def binary_to_hexadecimal(binaryNumberUser):
    """ Convert Binary to Hexadecimal """

    # Check if binaryNumberUser is a valid binary number
    checkBinary = binaryNumberUser
    while checkBinary > 0:
        if checkBinary % 10 > 1:
            print("Error: Not binary")
            return
        checkBinary = checkBinary // 10

    # convert to decimal first then to hexadecimal
    """
    Example => Binary 10100110
    1*2**7 + 0*2**6 + 1*2**5 + 0*2**4 + 0*2**3 + 1*2**2 + 1*2**1 + 0*2**0 = 166
    128 + 0 + 32 + 0 + 0 + 4 + 2 + 0 = 166
    Result= 166
    """
    try:
        decimal_number = abs(binary_to_decimal(binaryNumberUser))
        if decimal_number == 0:
            return "0"

        hex_digits = "0123456789ABCDEF"
        hex_result = ""
        while decimal_number > 0:
            """
            Example => Decimal 166
            166 / 16 = 10 remainder 6
            10 / 16 = 0 remainder 10 (A)
            Result = A6
            """
            remainder = decimal_number % 16
            hex_result += hex_digits[remainder] 
            decimal_number = decimal_number // 16

        return hex_result
    
    except ValueError:
            print("Invalid input. Please enter a valid binary number.")
            return
    except KeyboardInterrupt:
            print("Exiting to Base Conversion Menu.")
            return
    except TypeError:
            print("Invalid input. Please enter a valid binary number.")
            return



def decimal_to_binary(decimalNumberUser):
    """Convert decimal to binary"""  

    try:
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
    
    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")
        return
    except KeyboardInterrupt:
        print("Exiting to Base Conversion Menu.")
        return
    except TypeError:
        print("Invalid input. Please enter a valid decimal number.")
        return
    


def decimal_to_octal(decimalNumberUser):
    """Convert decimal to octal"""
    
    try:
        decimalNumber=abs(decimalNumberUser)
        if decimalNumber == 0:
            return "0"
                
        result=""
        while decimalNumber > 0:
            """
            Example => Decimal 378
            378 / 8 = 47 remainder 2
            47 / 8 = 5 remainder 7
            5 / 8 = 0 remainder 5
            Result = 572
            """
            remainder = decimalNumber % 8 # Get Remainder between 0-7
            result += str(remainder) # Append Remainder to Result String
            decimalNumber = decimalNumber // 8 # Refresh Decimal Number by Floor Division
        result = result[::-1] # Reverse the Result List to get the correct order

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



def octal_to_Decimal(octal_number):
    """Convert octal to decimal"""

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
    except TypeError:
        print('Invalid input. Octal number has digits range of 0..7.')
        return

def octal_to_binary(octal_number):
    """Convert octal to binary by first converting to decimal then to binary."""
    
    try:
        decimal_number=octal_to_Decimal(octal_number)
        if decimal_number is None:
            return  # If conversion failed, exit the function
        return print('Binary:',decimal_to_binary(decimal_number))
    
    except ValueError:
        print("Invalid input. Please enter a valid octal number.")
        return
    except KeyboardInterrupt:
        print("Exiting to Base Conversion Menu.")
        return
    except TypeError:
        print("Invalid input. Please enter a valid octal number.")
        return

def octal_to_hexadecimal(octal_number):
    """Convert octal to hexadecimal by first converting to decimal then to hexadecimal."""
    
    try:
        decimal_number=octal_to_Decimal(octal_number)
        if decimal_number is None:
            return  # If conversion failed, exit the function
        return print('Hexadecimal:',decimal_to_hexadecimal(decimal_number))
    
    except ValueError:
        print("Invalid input. Please enter a valid octal number.")
        return
    except KeyboardInterrupt:
        print("Exiting to Base Conversion Menu.")
        return
    except TypeError:
        print("Invalid input. Please enter a valid octal number.")
        return


def hexChar_To_Decimal(ch):
    """Convert a single hexadecimal character to its decimal value."""

    try:
        if 'A' <= ch <= 'F': # Check if it's a number between A-F or 0-9
            return 10 + (ord(ch) - ord('A'))
        
        elif '0' <= ch <= '9':
            return ord(ch) - ord('0')
        
        else:
            raise ValueError() # flag invalid hexadecimal character
        
    except ValueError:
        print("Invalid input. Please enter a valid hexadecimal character.")
        return
    except TypeError:
        print("Invalid input. Please enter a valid hexadecimal character.")
        return

    

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
    except TypeError:
        print("Invalid input. Please enter a valid hexadecimal number.")
        return

def hexadecimal_to_binary(hex_string):
    """Convert hexadecimal to binary by first converting to decimal then to binary."""

    try:
        decimal_number=hexadecimal_to_decimal(hex_string)
        if decimal_number is not None:
            return print('Binary:',decimal_to_binary(decimal_number))
        return  # If conversion failed, exit the function
    except ValueError:
        print("Invalid input. Please enter a valid hexadecimal number.")
        return
    except KeyboardInterrupt:
        print("Exiting to Base Conversion Menu.")
        return
    except TypeError:
        print("Invalid input. Please enter a valid hexadecimal number.")
        return
 
def hexadecimal_to_octal(hex_string):
    """Convert hexadecimal to octal by first converting to decimal then to octal."""

    try:
        decimal_number=hexadecimal_to_decimal(hex_string)
        if decimal_number is not None:
            return print('Octal:',decimal_to_octal(decimal_number))
        return  # If conversion failed, exit the function
    except ValueError:
        print("Invalid input. Please enter a valid hexadecimal number.")
        return
    except KeyboardInterrupt:
        print("Exiting to Base Conversion Menu.")
        return
    except TypeError:
        print("Invalid input. Please enter a valid hexadecimal number.")
        return

# Main execution block - runs when file is executed directly
if __name__ == "__main__":
    programmer_menu()