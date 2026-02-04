print(ord('A'))     
print(ord('a'))     
print(ord('0'))    
print(ord('@'))
#chr is used to know the assined charactar of number
print(chr(65))
print(chr(97))


x = input("Enter a single character: ")
if type(x) is str and len(x) == 1:
      print("Valid input!")
else:
     print("Please enter exactly ONE character!")


y = ord(x)
print("Character: "+x)
print("ASCII Value: "+str(y))