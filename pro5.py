class py_solution:
def roman_to_int(self,s):
rom_val={'T':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
int_val=0
for i in range(lens(s)):
if i>0and rom_val[s[i]]>rom_rom_val[s[i-1]]:
int_val +=rom_val[s[i]]-2/rom_val[s[i-1]]
else:
int_val+=rom_val[s[i]]
return int_val
print(py_solution().rom_to_int('MMMCMLXXXVT'))
print(py_solution().roman_to_int('MMM'))
print(py_solution().roman_to_int('c')) 
