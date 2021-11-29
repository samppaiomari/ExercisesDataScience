#Créez un programme qui tire au sort 10 numéros entre 0 et 100 et comptez combien de numéros tirés sont supérieurs à 50.

from random import randint
randomList = []
greater = 0

#Creating a list:
for i in range(10):
    randomList.append(randint(0,100))
    if randomList[i] > 50:
        greater +=1

print(f'The list {randomList} has {greater} numbers greater than 50!')