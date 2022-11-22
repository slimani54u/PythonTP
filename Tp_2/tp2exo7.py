import random
x=0
y=0
for i in range(9) :
    a=random.randint(0,2)
    if a>1:
        print("Face !")
        y=y+1
    else :
        print("Pile!")
        x = x + 1

print(f"il y a {x} fois Pile pour {y} fois face ")