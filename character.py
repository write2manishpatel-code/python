string = input("please enter your word : ")
character =input("please enter your character : ")


i = 0
count = 0


while i < len(string):


    if string[i] == character:


        count = count + 1


    i = i + 1




print(character, "has occured = " , count)
