#This program will slice an user e-mail and tell them specific stuff about it

#Prints the Welcome message
print("Hello there, and welcome to the e-mail slicer.")
print("Please, tell me your e-mail address:")
#Input of the e-mail address:
e_mail = input('--->').strip()
#Attributes the lenght of the mail to the variable:
len_mail = len(e_mail)
#Loop for writing the specific strings:
for x in range(0, len_mail):
    if e_mail[x] == "@":
        at_index = int(x)
        username = e_mail[:at_index]
        holder = e_mail[at_index+1:len_mail]
text1 = "Ok, so your username is: {}"
output_text1 = text1.format(username)
text2 = "And your e-mail is held at: {}"
output_text2 = text2.format(holder)
print(output_text1)
print(output_text2)