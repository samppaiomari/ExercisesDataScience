#Faire un programme qui tire un nombre N et demande à l'utilisateur de deviner le nombre tiré. À chaque erreur de réponse, votre programme doit imprimer un avertissement indiquant que la réponse est fausse et demander à nouveau à l'utilisateur de répondre.
#REMARQUE : pour cet exercice, utilisez une fonction de la bibliothèque aléatoire (par exemple randint()).

from random import randint
randomNumber =  randint(1,100)


name = input('Insert your name and good luck:').strip()
print(f'Hi {name} Holmes!! Our system chose a secret number! Now it is your turn to try to guess the correct number! You can choose a number from 1 to 100! (Only integer numbers) ')
print('To stop the program, insert 0!')

userAnswer = int(input('Your answer is: '))
#print(randomNumber)

while userAnswer != randomNumber and userAnswer != 0:
    userAnswer = int(input('Unsucessful attempt!! Try again:'))
if userAnswer == randomNumber:
    print(f'WOW! You got it {name}!! The answer is correct! The secret number is {randomNumber}!')