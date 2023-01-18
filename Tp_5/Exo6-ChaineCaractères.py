T=input("donner la chaine a traité ")

i=0
voyelle = 0
try:

    while T[i]!="0":

        if T[i]=='a'or T[i]=='o'or T[i]=='e'or T[i]=='u'or T[i]=='i'or T[i]=='y':
            voyelle=voyelle+1
        i=i+1

except IndexError:
    print(i)
    print(f"Pourcentage de voyelle {(voyelle/i)*100}%")

try:
    z=input("wagon")
    t="wagon dckskbwagonv ôrwagon"
    d=0
    while t[i]!="0":
        if t[i]=="w" and t[i+1]=="a" and t[i+2]=="g" and t[i+3]=="o"and t[i+4]=="n":
            d=d+1

        i=i+1
except IndexError:

    print("occurence nb",d,"fin",i+4-len(z))
