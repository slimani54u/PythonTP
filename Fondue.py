base =4
#qui indique le nombre de personnes pour
#laquelle est conçue la recette de base ;
fromage=800.0
eau=2
ail=2
pain=400
print("veillez indiquez le nombre de convives ")
nbConvives=int(input())
print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :")
print("- {:.1f} gr de fromage".format(fromage*nbConvives/base))
print("- {:.1f} dl d'eau".format(eau*nbConvives/base))
print("- {:.1f} gousse(s) d'ail".format(ail*nbConvives/base))
print("- {:.1f} gr de pain".format(pain*nbConvives/base))
