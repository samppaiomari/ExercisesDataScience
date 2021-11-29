#Créez un programme qui demande les symptômes que la personne présente et répond si elle doit ou non se faire hospitaliser.
#Symptômes : a. Avez-vous une fièvre persistante ? b. Avez-vous des difficultés à respirer ?
#La réponse du programme doit suivre le tableau suivant :
#A | B | Résultat
#----- | ---- | --------------------
#Oui | Non | Rester à la maison
#Non | Oui | Rester à la maison
#Non | Non | Rester à la maison
#Oui | Oui | Voir un hôpital

name = input("Please, enter the pacient's name: ")
print(f"Now {name}, let's ask you two questions about your health: ")
questionOne = input("Do you have persistent fever? (Y/N) ").strip()[0].upper()
questionTwo = input("Do you have difficulty to breathe?? (Y/N) ").strip()[0].upper()

print("Thank you for your answers!")

if (questionOne == 'Y' and questionTwo == 'Y'):
    print("Get to a hospital urgently!")
elif (questionOne == 'Y' and questionTwo == 'N') or (questionOne == 'N' and questionTwo == 'Y') or (questionOne == 'N' and questionTwo == 'N'):
    print("You should stay at home, but beware!")
else:
    print("It was not possible to understand your health status!")