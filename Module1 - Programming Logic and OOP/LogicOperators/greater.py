#Faire un programme qui demande deux nombres et affiche le plus grand d'entre eux.

numberOne = float(input('Insert the first number:'))
numberTwo = float(input('Insert the second number:'))

if numberOne > numberTwo:
    print(f'{numberOne} is greater than {numberTwo}.')

elif numberTwo > numberOne:
    print(f'{numberTwo} is greater than {numberOne}.')

else:
    print(f'There is not a greater number between {numberOne} and {numberTwo} .')