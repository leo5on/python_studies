import random
print("Hello there mere mortal. Using my mental power I can see that you need some health potion. But first I would like you to tell me which difficulty you're playing in and how much health you have right now.")
print("The difficulty level goes from 1 to 3, 1 being the easy one. Please tell me your difficulty level:")
level = int(input('---> '))
if level==3:
    print("ok, hard it is then")
else:
    if level==2:
        print("hmm, medium sized guy")
    else:
        print("ok you fagget go for the easy then")
print("Now, how much HP do you have now?")
hp = int(input('---> '))
while (hp<0 or hp>100):
    print("That's not fucking possible. Try Again")
    hp = int(input('---> '))
potion = int(random.randint(25,50)/level)
hp = (hp + potion)
text = "Ok motherf* your new HP level is {}"
output_text = text.format(hp)
print(output_text)