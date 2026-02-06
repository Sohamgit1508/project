rows=int(input("enter the number of rows:"))
num=1
print("floyd's triangle")
for i in range(rows+1):
    for j in range(1,i+1):
        print(num,end="")
        num=num+1
    print()