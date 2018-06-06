# Asks user for name
print("Hello there, could you please tell me your name?")
name = input('---> ')
# Asks for Age and turns a number into a string
print("Now, could you please tell me your age?")
age = str(input('---> '))
#Asks for city
print("Where do you live?")
city = input('---> ')
#Asks for hobbies
print("What in the hell do you like to do?")
hobbie = input('---> ')
#Creates output text
text = "Ok, so your frigging name is {}, you're {} years old, you live in {}, and your hobbie is {}"
output_text = text.format(name,age,city,hobbie)
#Prints output to screen
print(output_text)