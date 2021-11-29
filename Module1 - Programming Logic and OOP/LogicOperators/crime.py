#Créez un programme pour vérifier qui est le meurtrier d'un crime. Pour découvrir le meurtrier, la police établit un court questionnaire de 5 questions auxquelles la réponse doit être oui ou non :
#a. Vous habitez à proximité de la victime ?
#b. Avez-vous déjà travaillé avec la victime ?
#c. Avez-vous appelé la victime ?
#d. Vous avez été sur la scène du crime ?
#e. Avez-vous une dette à la victime ?
#Chaque réponse positive donne un point au suspect. La police considère les suspects avec 5 points comme les meurtriers, avec 4 à 3 points comme des complices et avec 2 points comme de simples suspects, nécessitant une enquête plus approfondie. Les valeurs inférieures à 1 sont libérées.

#starting

start = input('Do you wanna start the interrogation? (Y/N): ').strip()[0].upper()

if start == 'Y':
    afirmations = 0

    if input("Do you live near the victim? (Y/N) ").strip()[0].upper() == 'Y':
        afirmations += 1
        
    if input("Have you ever worked with the victim? (Y/N) ").strip()[0].upper() == 'Y':
        afirmations += 1

    if input("Did you call the victim? (Y/N) ").strip()[0].upper() == 'Y':
        afirmations += 1

    if input("Were you at the crime scene? (Y/N) ").strip()[0].upper() == 'Y':
        afirmations += 1

    if input("Did you owe the victim? (Y/N) ").strip()[0].upper() == 'Y':
        afirmations += 1

    if afirmations == 2:
        print("Suspect! Watch out!")
    elif 3 <= afirmations <= 4:
        print("Accomplice! Be careful!")
    elif afirmations == 5:
        print("Murderer! Arrest him now!")
    else:
        print("Innocent! You can let him go!")
else:
    pass