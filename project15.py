num = int(input("Enter a decimal number: "))
binary = ""

while num > 0:          # Outer loop
    temp = num
    while temp >= 2:    # Inner loop
        temp = temp - 2
    remainder = temp
    binary = str(remainder) + binary
    num = num // 2

print("Binary number is:", binary)
