#Tirez une liste de 10 nombres et imprimez :
#a. une liste avec les 4 premiers numéros ;
#b. une liste avec les 5 derniers numéros ;
#c. une liste contenant uniquement les éléments des positions paires ;
#d. une liste contenant uniquement les éléments des positions impaires ;
#e. la liste inverse de la liste tirée (c'est-à-dire une liste qui commence par le dernier élément de la liste tirée et se termine par le premier élément) ;
#f. une liste inverse des 5 premiers chiffres
#g. une liste inverse des 5 derniers numéros.

from random import randint 
randomList = []

#Creating a list:
for i in range(10):
    randomList.append(randint(1,100))

#Printing:
print(f"\nRandom List: {randomList}")
print(f"\nThe first four numbers list: {randomList[0:4]}")
print(f"\nThe last five numbers list: {randomList[5:10]}")
print(f"\nThe elements at even positions (0°,2°,4°,6°,8°): {randomList[0::2]}")
print(f"\nThe elements at odds positions (1°,3°,5°,7°,9°): {randomList[1::2]}")
print(f"\nThe inverse list: {randomList[::-1]}")
print(f"\nThe first five numbers inverse list: {randomList[4::-1]}")
print(f"\nThe last five numbers inverse list: {randomList[9:4:-1]}")
