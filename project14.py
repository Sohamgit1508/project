num = int(input("Enter a number: "))
count = 1  
while num // 10 != 0:
    num = num // 10
    count += 1

print("Number of digits:", count)
