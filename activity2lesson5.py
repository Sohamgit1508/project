x=float(input("enter the actual cost:"))
y=float(input("enter the selling cost:"))
if y>x:
    amount=y-x
    print("profit amount:",amount)
else:
    print("no profit no loss")