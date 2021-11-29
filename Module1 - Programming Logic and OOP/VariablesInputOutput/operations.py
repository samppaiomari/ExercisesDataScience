#Faire un programme qui demande deux nombres entiers et un nombre réel, calculer et afficher: 
# Le produit de deux fois le premier par la moitié du deuxième 
# La somme du triple du premier avec le troisième.
#Le troisième élevé au cube.

number1 = int(input('Insert the first integer number: '))
number2 = int(input('Insert the second integer number: '))
number3 = float(input('Insert a real number: '))

print(f'The product of double of the first number with half of the second number is {(2*number1)*(number2/2)} .')
print(f'Sum of the triple of the first number with the third number is {(3*number1) + number3} .')
print(f'The third number raised to the cube is {number3 ** 3} .')