import os

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativa = 0
while True:

    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra: ')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print(f'Palavra formada: ', palavra_formada) 

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Voce Ganhou!')
        print('A palavra era', palavra_secreta)
        break
