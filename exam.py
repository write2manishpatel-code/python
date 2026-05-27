medical_cause = input("did you have a medical cause? (yes/no)")

if medical_cause == "yes":
    print("you are allowed to give the exam")


else:

    attendance = int(input("enter the attendance of the student"))

    if attendance >= 75:
        print("allowed to give the exam")
    else:
        print("not allowed to give the exam")