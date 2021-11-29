#Créez un programme dans lequel l'utilisateur doit deviner le nombre choisi par l'ordinateur. L'ordinateur doit sélectionner un nombre entier de 1 à 5 et demander à l'utilisateur d'essayer de découvrir ce nombre. Une fois que l'utilisateur a donné sa réponse, le programme doit lui indiquer si elle est correcte ou non. 
#Conseil : pour tirer un numéro, vous devrez utiliser la bibliothèque random.

from random import randint

randomNumber =  randint(1,5)
again = 'Y'

name = input('Insert your name and good luck:')
print(f'Hi {name} Holmes!! Our system chose a secret number! Now it is your turn to try to guess the correct number! You can choose a number from 1 to 5! ')
userAnswer = int(input('Your answer is: '))
while userAnswer<1 or userAnswer>5:
    userAnswer = int(input('Invalid input. Your answer is: '))
if userAnswer == randomNumber:
    print(f"Congrats!! You chose the correct answer: {userAnswer}!")

else:
    print(f"Ooops, you chose the wrong answer: {userAnswer}. The right option is {randomNumber}!")
