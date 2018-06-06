#List of pre added names:
names = ["Leo","Joe","Jack"]
#Calculates the number of names in the pre added list
len_names = int(len(names))
#Loop for never ending program:
while True:
#Prints welcome message:
    print("Hello there, would you please confirm your name? ")
#Puts user name into variable:
    name = str(input('---> ').strip().capitalize())
#Checks if the name is in the list:
    if name in names:
#If yes, print a message and asks if the name should be removed from the list
        text1 = "Welcome Mr(s). {}"
        output_text1 = text1.format(name)
        print(output_text1)
        print("Would you like to be removed from the list? (y/n)")
        answer1 = input('---> ').capitalize()
#If yes, removes name and starts over:
        if answer1 == "Y":
            names.remove(name)
#If not, prints a message and starts over:
        elif answer1 == "N":
            print("That's just fine, no problem!")
    else:
#If the name is not on the list it prints a message and asks if the name should be added:
        print("You are not on the list. Would you like to be added?")
        print("Enter Y for yes or N for no: ")
        answer2 = input('---> ').capitalize()
#If yes, adds the name to the list
        if answer2 == "Y":
            names.append(name)
#If not, prints a message and starts over:
        elif answer2 == "N":
            print("Sure, see you later then!")