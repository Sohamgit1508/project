try:
    age = int(input("Enter your age: "))   # Convert input directly to integer
    
    print("Age is valid.")
    
    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")

except ValueError:
    print("Invalid input! Please enter a valid integer")