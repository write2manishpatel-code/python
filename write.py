print("select your ride")
print("option1.bike")
print("option2.car")

choice = int( input("enter your choice") )

if choice == 1 :

    print("what type of bike do you want?")
    print("1.scooty\n")
    print("2.scooter\n")

    choicebike=int(input("enter your chiocebike"))

    if choicebike==1:
        print("you have selected scooty")
    else:
        print("you have selected scooter")