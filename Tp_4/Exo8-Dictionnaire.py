# 1)
dictio={"name":"titi","firstname":"toto" ,"promo":2022 ,"group":122}
print(f"votre nom est {dictio['firstname']}, prénom est {dictio['firstname']} , vous faites partie de la promo {dictio['promo']} et votre groupes est {dictio['group']}")

# 2)
print("Les clés du dictionnaire sont :")
for x in dictio:
    print("-"+x)
print("Les valeurs du dictionnaire sont :")
for x in dictio:
    print(f"-{dictio[x]}")
print("Les tuplets du dictionnaire sont :")
la=list(dictio.items())
print(la[0])








