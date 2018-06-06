films = {
   "Finding Dory":[3, 10],
   "Bourne":[18, 10],
   "Tarzan":[15, 3],
   "Ghost Busters":[12,3] 
}
while True:
   print("Hello there, which filme would you like to watch?")
   choice = input('---> ').strip().title()
   if choice in films:
       age = int(input("I have to check if you are old enough for this one, how old are you?: ").strip())
       if age >= films[choice][0]:
           num_seats = films[choice][1]
           if num_seats > 0:
                print("Enjoy!")
                films[choice][1] = films[choice][1] - 1
           else:
               print("Sorry, this movie is fully booked.")
       else:
            print("You are not alowed in this movie.")
   else:
        print("That's not currently being displayed.")