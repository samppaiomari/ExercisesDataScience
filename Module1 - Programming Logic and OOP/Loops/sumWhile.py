#Demandez à l'utilisateur de saisir un nombre N et d'additionner tous les nombres de 1 à N en utilisant la répétition de la loop while.

number = int(input('Please, enter a number: '))
i=1
sumN = 0

while i <= number:
    sumN = sumN + i
    i =i + 1
print(f' the sum from 1 to {number} is {sumN}!')