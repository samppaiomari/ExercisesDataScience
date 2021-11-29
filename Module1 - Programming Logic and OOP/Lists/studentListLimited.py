#Réalisez un programme qui demande à l'utilisateur d'entrer le nom et l'âge d'un élève et le nombre de tests que cet élève a effectués. Ensuite, le programme doit demander à l'utilisateur de saisir les notes de chaque test de l'étudiant. A la fin, le programme doit imprimer une liste contenant :
#a. Le nom de l'élève en position 0;
#b. Âge de l'élève en position 1;
#c. Une liste de tous les grades en position 2;
#d. À la position 3, la moyenne de l'élève sans tenir compte de la meilleure et de la moins bonne note de l'élève (dans ce cas, le nombre d'épreuves doit être supérieur à deux);
#e. True ou False, si la moyenne est supérieure à 5 ou non, à la position 4;

studentList = []
grades = []
arithmeticMean = 0

studentList.append(input("Hello! Enter the student name: \n").strip())
studentList.append(int(input("Now, enter the student age: \n").strip()))
tests = int(input("Okay, tell me how many tests this student did: \n"))

for i in range(tests):
    grades.append(int(input(f"Insert the grade {i+1}: \n").strip()))
studentList.append(grades)

gradesCopy = sorted(grades)
gradesCopy.pop(0)
gradesCopy.pop(-1)

for i in range(len(gradesCopy)):
    arithmeticMean += gradesCopy[i]  
arithmeticMean = arithmeticMean/len(gradesCopy)
studentList.append(arithmeticMean)

if arithmeticMean>5:
    studentList.append(True)
else:
    studentList.append(False)

print(f"The student list is: {studentList} ")
