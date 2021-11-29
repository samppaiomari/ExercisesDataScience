#Faire un programme qui demande les quatre notes bimestrielles d'un étudiant et qui affiche la moyenne arithmétique de ces notes.

grade1, grade2, grade3, grade4 = input("Insert your four grades separated by comma: ").split(",")
meanOp = (float(grade1) + float(grade2) + float(grade3) + float(grade4))/4
print(f'Your average note is:{meanOp}')
