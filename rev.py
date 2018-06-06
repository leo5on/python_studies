def rev(text):
    word = text[::-1]
    return word 
string = input("type in your word: ").strip().lower()
print(rev(string))