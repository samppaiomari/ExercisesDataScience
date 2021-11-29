#Faire un programme qui demande un nombre et montre s'il est positif ou négatif.

number = float(input('Insert a number:'))
if number > 0:
    print(f'{number} is a positive number.')
elif number == 0:
    print(f'{number} is zero.')
else:
    print(f'{number} is a negative number.')