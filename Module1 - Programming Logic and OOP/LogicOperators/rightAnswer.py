#Créez un programme qui affiche une question à choix multiple avec cinq possibilités (lettres a, b, c, d, e). Connaissant la réponse correcte, le programme doit recevoir le choix de l'utilisateur et informer la lettre que l'utilisateur a marquée et si la réponse est correcte ou fausse.

from random import randint

print(r'''The question has five options. You must choose one of them.
        a) Insert A
        b) Insert B
        c) Insert C
        d) Insert D
        e) Insert E
        ''')

options = ['A','B','C','D','E']
userAnswer = input('Your answer is: ').strip()[0].upper()
correctAnswer =  options[randint(0,4)]

if userAnswer == correctAnswer:
    print(f"Congrats!! You chose the correct answer: {userAnswer}!")
else:
    print(f"Ooops, you chose the wrong answer: {userAnswer}. The right option is {correctAnswer}!")
