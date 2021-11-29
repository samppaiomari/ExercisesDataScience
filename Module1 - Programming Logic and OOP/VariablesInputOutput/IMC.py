#Faire un programme qui demande le poids et la taille d'une personne et calcule son IMC (indice de masse corporelle).
#Remarque : IMC = Poids / Taille **2

weight = float(input('Insert your weight (Kg): '))
height = float(input('Insert your height (Meters): '))

print(f'Your IMC is {weight / (height ** 2)}')