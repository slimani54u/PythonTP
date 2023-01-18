billet100=0
billet50=0
billet10=0
piece2=0
piece1=0
a=int(input("quelle est la somme"))
billet100=a//100
reste100=a%100
billet50=reste100//50
reste50=reste100%50
billet10=reste50//10
reste10=reste50%10
piece2=reste10//2
piece1=reste10%2

print(f"""soit la somme de {a} euros. Le message à afficher est : « {a} euros, c’est donc {billet100}
billets de 100, {billet50} de 50, {billet10} de 10, {piece2} pièces de 2 et {piece1} pièce 1. """)