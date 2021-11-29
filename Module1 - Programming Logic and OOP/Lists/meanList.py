#Réalisez un programme qui demande les 4 notes bimestrielles et en montre la moyenne arithmétique, en utilisant des listes.

grades = input("Insert your four bimonthly grades separated by comma: ").split(",")
grades = [float(i) for i in grades]
arithmeticMean = 0

for i in range(len(grades)):
    arithmeticMean += grades[i]  

arithmeticMean = arithmeticMean/len(grades)

print(f"Your arithmetic mean is {round(arithmeticMean, 2)}! ")