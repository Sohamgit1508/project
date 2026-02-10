num = int(input("enter a number: "))
count = 1  
while num // 10 != 0:
    num = num // 10
    count += 1

print("number of digits are", count)
