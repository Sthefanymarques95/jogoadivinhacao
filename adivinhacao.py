import random

numero_secreto = random.randrange(1, 101)
numero_tentativas = 0 

print('qual nivel de dificuldade?')
print('1- fácil, 2- médio, 3- dificil ')
nivel = int(input('Digite o nível de dificuldade'))

if nivel == 1:
    número_tentativas = 20
elif nivel == 2:
    numero_tentativas = 10
elif nivel == 3:
    numero_tentativas = 5

for rodada in range(1, numero_tentativas +1):
    print(f'tentativas {rodada} de {numero_tentativas}')
    valor_escolhido_str = input('Digite um numero de 1 a 100: ')
    print('você digitou', valor_escolhido_str)
    valor_escolhido = int(valor_escolhido_str)

    if valor_escolhido < 1 or valor_escolhido > 100: 
        print('Numero invalido, o número deve ser de 1 a 100')


        continue


    acertou = valor_escolhido == numero_secreto
    maior = valor_escolhido > numero_secreto
    menor = valor_escolhido < numero_secreto

    if acertou: 
        print('Parabéns você acertou o número secreto')
        break 
    else:
        if maior:
            print('Você errou! o número que você digitou é maior que o número secreto')
        elif menor:
            print('Você errou! o número que você digitou é menor que o número secreto')
print('Fim de Jogo')