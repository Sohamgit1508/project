medical_cause=input("did you have a medical cause.yes or no:")
attendence=int(input("enter the attendence:"))
if medical_cause=="Y":
    print("you are allowed")
else:
    if attendence>=75:
        print("you are allowed for exam")
    else:
        print("you are not allowed for the exam")
