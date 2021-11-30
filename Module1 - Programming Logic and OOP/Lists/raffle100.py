#Faire un programme qui tire 10 nombres entre 0 et 100 et les imprime :
#a. le plus grand nombre tiré au sort ;
#b. le plus petit nombre tiré au sort ;
#c. la moyenne des numéros tirés ;
#d. la somme des numéros tirés.

from random import randint 
randomList = []

#Creating a list:
for i in range(10):
    randomList.append(randint(1,100))

#Printing:
print(f"\nRandom List: {randomList}")
print(f"\nThe greatest number in the list: {max(randomList)}")
print(f"\nThe smallest number in the list: {min(randomList)}")
print(f"\nThe mean of the numbers: {sum(randomList)/len(randomList)}")
print(f"\nThe sum of the elements in the list: {sum(randomList)}")
