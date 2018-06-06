#Este programa serve para fazer a brincadeira do Pig_Latin.


print "Hello! This is the Pig Latin translator."
sufix = 'ay'
input_word = raw_input('To begin, please enter the word you want to translate')
if len(input_word) > 0 and input_word.isalpha():
	lower_word = input_word.lower()
	first_letter = lower_word[0]
	translated_word = lower_word + first_letter + sufix
	translated_word = translated_word[1:len(translated_word)]
	print translated_word
else:
	print "Your word must contain only letters, and cannot be blank."