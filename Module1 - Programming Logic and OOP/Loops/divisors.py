#Créez un programme qui reçoit un nombre entier de l'utilisateur et imprime à l'écran le nombre de diviseurs de ce nombre et ce qu'ils sont.

number = int(input('Please, enter a number: '))
i = 1
count =0
while i<=number:
    if number%i == 0:
        print(f'{i} is a divisor of {number}!')
        count +=1
    i += 1
print(f'{number} has {count} divisors!')