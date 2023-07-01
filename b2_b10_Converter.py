# Function to check if a string is a valid binary number
def is_valid_binary(binary_num):
    for digit in binary_num:
        if digit != '0' and digit != '1':
            return False
    return True

# Function to convert decimal to binary
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    binary = ''
    while decimal_num > 0:
        binary = str(decimal_num % 2) + binary
        decimal_num //= 2
    return binary

# Function to convert binary to decimal
def binary_to_decimal(binary_num):
    decimal = 0
    power = 0
    for digit in reversed(binary_num):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

# User input to determine the conversion type
conversion_type = input("Enter '1' if you have a binary number or '2' if you have a decimal number: ")

if conversion_type == '1':
    # Conversion from binary to decimal
    binary_number = input("Enter a binary number: ")
    if is_valid_binary(binary_number):
        decimal_number = binary_to_decimal(binary_number)
        print("Decimal representation:", decimal_number)
    else:
        print("Invalid binary number. Please enter a valid binary number.")
elif conversion_type == '2':
    # Conversion from decimal to binary
    decimal_number = int(input("Enter a decimal number: "))
    binary_number = decimal_to_binary(decimal_number)
    print("Binary representation:", binary_number)
else:
    # Invalid input
    print("Invalid input. Please enter either '1' or '2'.")
