# 1)
dictio1={"name":"titi","firstname":'toto' ,"promo":2022 ,"group":122}
print(f"votre nom est {dictio1['firstname']}, prénom est {dictio1['firstname']} , vous faites partie de la promo {dictio1['promo']} et votre groupes est {dictio1['group']}")

# 2)
print("Les clés du dictionnaire sont :")
for x in dictio1:
    print("-"+x)
print("Les valeurs du dictionnaire sont :")
for x in dictio1:
    print(f"-{dictio1[x]}")
print("Les tuplets du dictionnaire sont :")
la=list(dictio1.items())
for i in range(0,len(la)):
    print("-",la[i])


# 3)
dictio2={"name":"tata","firstname":'tete' ,"promo":2022 ,"group":122}

# 4)
dictioBinome={"ID1":dictio1,"ID2":dictio2}
print("Les étudiants formants le binôme sont :")
print(f"L'étudiant {dictioBinome['ID1']['firstname']} {dictioBinome['ID1']['name']} du groupe {dictioBinome['ID1']['group']}")
print(f"L'étudiant {dictioBinome['ID2']['firstname']} {dictioBinome['ID2']['name']} du groupe {dictioBinome['ID2']['group']}")


#syntaxe
date="122111"
jour=int(date[0:2])




























