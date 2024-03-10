# Ahmed Mohamed Noureldin     

# this is Numbering system converter

# function converts decimal number to binary number
def decimal_to_binary(dec_num):
    binary_num = ""  # Make octal_result empty so that it does not take a random value

    dec_num_int = int(dec_num)
    # Convert decimal to binary
    while dec_num_int > 0:
        remainder = dec_num_int % 2
        binary_num = str(remainder) + binary_num
        dec_num_int //= 2  # I used // "Assign. operator" because it used to perform floor division and update the value of the variable on the left-hand side.

    return binary_num


# function converts decimal number to octal number
def decimal_to_octal(dec_num):
    octal_num = ""  # Make octal_result empty so that it does not take a random value
    dec_num_int = int(dec_num)
    # Convert decimal to octal
    while dec_num_int > 0:
        remainder = dec_num_int % 8
        octal_num = str(remainder) + octal_num
        dec_num_int //= 8  # I used // "Assign. operator" because it used to perform floor division and update the value of the variable on the left-hand side.

    return octal_num


# function converts decimal number to hexadecimal number
def decimal_to_hexadecimal(dec_num):
    hex_characters = "0123456789ABCDEF"
    hexadecimal_num = (
        ""  # Make octal_result empty so that it does not take a random value
    )

    dec_num_int = int(dec_num)

    # Convert decimal to hexadecimal
    while dec_num_int > 0:
        remainder = dec_num_int % 16
        hexadecimal_num = hex_characters[remainder] + hexadecimal_num
        dec_num_int //= 16  # I used // because it used to perform floor division and update the value of the variable on the left-hand side.

    return hexadecimal_num


# function converts binary number to decimal number
def binary_to_decimal(bin_num):
    # Ensure bin_num is a string
    bin_num_str = str(bin_num)
    # Convert binary to decimal
    dec_num = 0
    power = 0
    bin_num = bin_num_str[::-1]

    # Reverse the binary number to start from the rightmost digit
    for digit in bin_num_str:
        dec_num += int(digit) * (2**power)
        power += 1

    return dec_num


# function converts binary number to octal number
def binary_to_octal(bin_num):
    octal_num = ""  # Make octal_result empty so that it does not take a random value
    dictionary = {
        "000": "0",
        "001": "1",
        "010": "2",
        "011": "3",
        "100": "4",
        "101": "5",
        "110": "6",
        "111": "7",
    }
    # Adding Zeros if needed
    while len(bin_num) % 3 != 0:
        bin_num = "0" + bin_num

    # Convert binary to octal
    for i in range(0, len(bin_num), 3):
        chunck = bin_num[i : i + 3]
        octal_digit = dictionary[chunck]
        octal_num += octal_digit  # octal_result = octal_result + octal_digit

    return octal_num


# function converts binary number to hexadecimal number
def binary_to_hexadecimal(bin_num):
    hex_num = ""  # Make hex_result empty so that it does not take a random value
    Hex_Dictionary = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1011": "E",
        "1111": "F",
    }
    # Adding Zeros if needed
    while len(bin_num) % 4 != 0:
        bin_num = "0" + bin_num
    # Convert binary to octal
    for i in range(0, len(bin_num), 4):  # Make for loop and its steps are 4
        chunck = bin_num[i : i + 4]
        hex_digit = Hex_Dictionary[chunck]
        hex_num += hex_digit

    return hex_num


# function converts octal number to decimal number
def octal_to_decimal(octal_num):
    dec_num = ""  # Make dec_result empty so that it does not take a random value
    octal_num_str = str(octal_num)
    # Convert octal to decimal
    dec_num = 0
    power = 0

    # Reverse the octal number to start from the rightmost digit
    reversed_octal_str = octal_num_str[::-1]

    for digit in reversed_octal_str:
        dec_num += int(digit) * (8**power)
        power += 1

    return dec_num


# function converts hexadecimal number to decimal number
def hexadecimal_to_decimal(hex_num):
    # Convert hexadecimal to decimal
    dec_num = 0
    power = 0
    # Reverse the hexadecimal number to start from the rightmost digit
    hex_num = hex_num[::-1]
    digit = 0

    for i in range(len(hex_num)):
        if hex_num[i] == "A":
            digit = 10
        elif hex_num[i] == "B":
            digit = 11
        elif hex_num[i] == "C":
            digit = 12
        elif hex_num[i] == "D":
            digit = 13
        elif hex_num[i] == "E":
            digit = 14
        elif hex_num[i] == "F":
            digit = 15
        else:
            digit = int(hex_num[i])

        dec_num += int(digit) * (16**power)
        power += 1

    return dec_num


# function converts octal number to hexadecimal number
def octal_to_hexadecimal(octal_num):
    hex_num = ""

    dec_num = octal_to_decimal(octal_num)
    hex_num = decimal_to_hexadecimal(dec_num)
    return hex_num


# function converts hexadecimal number to octal number
def hexadecimal_to_octal(hex_num):
    octal_num = ""
    dec_num = hexadecimal_to_decimal(hex_num)
    octal_num = decimal_to_octal(dec_num)
    return octal_num


# function converts octal number to binary number
def octal_to_binary(octal_num):
    binary_num = ""

    dec_num = octal_to_decimal(octal_num)
    binary_num = decimal_to_binary(dec_num)

    return binary_num


# function converts hexadecimal number to binary number
def hexadecimal_to_binary(hex_num):
    bin_num = ""
    dec_num = hexadecimal_to_decimal(hex_num)
    bin_num = decimal_to_binary(dec_num)

    return bin_num


while True:
    # Menu 1
    print("**Numbering system converter**")
    print("A) insert a new number")
    print("B) Exit program\n")

    choice_menu1 = input("Please enter your choise (A/B):")

    if choice_menu1 == "A":
        Num = str(input("Please insert a number: "))

        # Menu 2
        print("**Please select the base you want to convert a number from**")
        print("A) Decimal")
        print("B) Binary")
        print("C) Octal")
        print("D) Hexadecimal")

        # Ensure that the input is valid
        choice_menu2 = input("Please enter your choise (A/B/C/D):")
        if choice_menu2 not in ["A", "B", "C", "D"]:
            print("Please select a valid choice.\n")
            continue

        # Menu 3
        print("**Please select the base you want to convert a number to**")
        print("A) Decimal")
        print("B) Binary")
        print("C) Octal")
        print("D) Hexadecimal")

        # Ensure that the input is valid
        choice_menu3 = input("Please enter your choise (A/B/C/D):")
        if choice_menu3 not in ["A", "B", "C", "D"]:
            print("Please select a valid choice.\n")
            continue

        # Call decimal_to_binary function
        if choice_menu2 == "A" and choice_menu3 == "B":
            decimal_to_binary(Num)
            print(decimal_to_binary(Num))
            print("\n")

        # Call decimal_to_octal function
        elif choice_menu2 == "A" and choice_menu3 == "C":
            decimal_to_octal(Num)
            print(decimal_to_octal(Num))
            print("\n")

        # Call decimal_to_hexadecimal function
        elif choice_menu2 == "A" and choice_menu3 == "D":
            decimal_to_hexadecimal(Num)
            print(decimal_to_hexadecimal(Num))
            print("\n")

        # Call binary_to_decimal function
        elif choice_menu2 == "B" and choice_menu3 == "A":
            binary_to_decimal(str(Num))
            print(binary_to_decimal(str(Num)))
            print("\n")

        # Call binary_to_octal function
        elif choice_menu2 == "B" and choice_menu3 == "C":
            binary_to_octal(str(Num))
            print(binary_to_octal(str(Num)))
            print("\n")

        # Call binary_to_hexadecimal function
        elif choice_menu2 == "B" and choice_menu3 == "D":
            binary_to_hexadecimal(str(Num))
            print(binary_to_hexadecimal(str(Num)))
            print("\n")

        # Call octal_to_decimal function
        elif choice_menu2 == "C" and choice_menu3 == "A":
            octal_to_decimal(Num)
            print(octal_to_decimal(Num))
            print("\n")

        # Call octal_to_binary function
        elif choice_menu2 == "C" and choice_menu3 == "B":
            octal_to_binary(Num)
            print(octal_to_binary(Num))
            print("\n")

        # Call octal_to_hexadecimal function
        elif choice_menu2 == "C" and choice_menu3 == "D":
            octal_to_hexadecimal(Num)
            print(octal_to_hexadecimal(Num))
            print("\n")

        # Call hexadecimal_to_decimal function
        elif choice_menu2 == "D" and choice_menu3 == "A":
            hexadecimal_to_decimal(Num)
            print(hexadecimal_to_decimal(Num))
            print("\n")

        # Call hexadecimal_to_binary function
        elif choice_menu2 == "D" and choice_menu3 == "B":
            hexadecimal_to_binary(Num)
            print(hexadecimal_to_binary(Num))
            print("\n")

        # Call hexadecimal_to_octal function
        elif choice_menu2 == "D" and choice_menu3 == "C":
            hexadecimal_to_octal(Num)
            print(hexadecimal_to_octal(Num))
            print("\n")

    elif choice_menu1 == "B":
        print("Exiting program.\n")
        break

    else:
        print("please select a valid choice\n")
