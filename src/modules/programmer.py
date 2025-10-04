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
                value1=base_conversions_menu()
                print(value1)
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
                value = decimal_to_others_menu()
                print(value)
                break
            elif choice == 3:
                hexadecimal_to_others_menu()
            elif choice == 4:
                octal_to_others_menu()
            elif choice == 5:
                return
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        except KeyboardInterrupt:
            print("Exiting to Programmer Menu.")
            return
        break
    
            



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
            
            elif choice == 2:
                return 
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
        

programmer_menu()

