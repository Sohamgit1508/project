def add(p,s):
    return p+s
def sub(p,s):
    return p-s
def mutiply(p,s):
    return p*s
def divide(p,s):
    return p/s
print("choose the operator:")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice=int(input("enter the choice:1/2/3/4:"))
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if choice==1:
    print(num1,"+",num2,"=",add(num1,num2))
elif choice==2:
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice==3:
    print(num1,"*",num2,"=",mutiply(num1,num2))
elif choice==4:
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("invalid input")