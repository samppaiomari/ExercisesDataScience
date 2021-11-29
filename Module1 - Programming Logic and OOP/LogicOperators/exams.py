#Ecrivez un programme qui demande la note de trois examens d'un étudiant et montre s'il a passé ou non.
#Remarque : l'élève passera l'année si la moyenne de ses notes est supérieure ou égale à six (la moyenne est la somme des notes divisée par le nombre des examens).

scoreOne, scoreTwo, scoreThree = input('Insert your score for the three exams separated by a comma:').split(',')
average = (float(scoreOne) + float(scoreTwo) + float(scoreThree))/3

print(f'Your grade average is {round(average,2)}. You are approved!!') if average >= 6 else print(f'Your grade average is {round(average,2)}. You have failed!!!')