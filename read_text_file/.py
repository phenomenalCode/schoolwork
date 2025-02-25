f = open("customers-100.csv")
for ln in f:
    print(ln)
#loop through string one character at a time
i = 0


   
val = ""
while  i <= len(ln):
 c = [i]
 if  c != ",":
    val += c
else: 
    print(val)
    val = ""
i = i + 1
print(f.read())
f.close()