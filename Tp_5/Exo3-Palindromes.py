palindrome=input("ecrivez le palindrome : ")
pal=""
for a in palindrome:
    if a.isalpha()==True:
        pal+=a
print(pal)
pal1=pal[0:len(pal)]

pal2=pal[-len(pal):len(pal)]


if pal1==pal2:
    print("ceci est un palindrome")
else: print("la chaine est pas un palidrome")
