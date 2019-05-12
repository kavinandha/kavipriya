def check(string):
vowels=set("aeiou")
s=set({})
for char in string:
if char in vowels:
s.add(char)
else:
pass
if len(s)==len(vowels):
print("accepted")
else:
print("not accepted")
if__name__=="__main__":
string="seequial"
string=string.lower()
check(string)
