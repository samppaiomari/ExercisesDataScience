#Faire un programme qui demande la température en Fahrenheit (F), transformer et montrer la température en Celsius (°C).
#Essayez aussi de créer un programme qui fasse l'inverse : demandez la température en degrés Celsius et transformez-la en degrés Fahrenheit.

#Choosing the mode
mode = input('What is the desired mode? 1 - Fahrenheit to Celsius; 2 - Celsius to fahrenheit ')
if mode == '1':
    Frnht = float(input('Insert the temperature in degrees Fahrenheit: '))
    Celsius = (5*(Frnht - 32))/9
    print(f'{Frnht} degrees Fahrenheit equals {Celsius} degrees Celsius.')
elif mode == '2':
    Celsius = float(input('Insert the temperature in degrees Celsius: '))
    Frnht = (9 * Celsius)/5 + 32
    print(f'{Celsius} degrees Celsius equals {Frnht} degrees Fahrenheit.')
else:
    print('It was not possible to understand the desired mode. Please try again.')
