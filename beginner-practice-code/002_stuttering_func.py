def stutter(word):
    stutter_word = word[:2]+'... '+ word[:2]+ '... '+ word+'?'
    return stutter_word


print("Enter a word: ")
word = input()
print(stutter(word))