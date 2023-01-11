T=[]

for i in range (0,3) :
    if i==0 :

        T.append(int(input("entrez le jour : ")))
    if i ==1 :
        T.append(int(input("entrez le mois : ")))
    if i==2 :
        T.append(int(input("entrez l'annee : ")))
if T [2]<1000 :
    print("la date est incorrecte")
if T[1] not in range(0,13) :
    print("la date est incorrecte")
if T[0] not in range(0,32) :
    print("la date est incorrecte")


if (T[2]%4 ==0 and T[2]%100 != 0)or T[2]%400 ==0 :
    if T[1] ==(1 or 3 or 5 or 7 or 8 or 10 or 12) :
        if T[0]>31 or T[0]<=0 :
            print("la date est incorrecte")
    elif T[1]==2 :
        if  T[0]>29 or T[0]<=0:
            print("date incorrecte")
    else :
        if T[0] > 30 or T[0] <= 0:
            print("date incorrecte")
elif T[1] ==(1 or 3 or 5 or 7 or 8 or 10 or 12) :
        if T[0]>31 or T[0]<=0 :
            print("la date est incorrecte")
elif T[1]==2 :
    if  T[0]>28 or T[0]<=0:
        print("date incorrecte")
else :
    if T[0] > 30 or T[0] <= 0:
        print("date incorrecte")