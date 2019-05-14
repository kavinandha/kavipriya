def isogram(word):
clean_word=word.lower()
letter_list=[]
for letter in clean_word:
if letter.isalpha():
if letter in letter_list:
return false
letter_list.append(letter)
return true
if__name__=='__main__':
print(isogram("machine"))
print(isogram("isogram"))
print(isogram("list"))
print(isogram("alphabet"))
