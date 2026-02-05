string=input("enter a value for string:")
char=input("enter a character to count:")
count=0
i=0
while i<len(string):
    if string[i]==char:
          count+=1
    i+=1
print("the number of times",char,"appears in the string is:",count)