import random
import string
from erros import *

lista_palavras = ['BANANA', 'MELANCIA', 'MORANGO', 'PERA', 'ABACAXI', 'CAQUI', 'JAMBO', 'ABACATE', 'MANGA', 'LARANJA']

# Escolher uma palavra aleatória entre as possíveis
senha = random.choice(lista_palavras)
# Definir a saída ao usuário como uma sequência de '_' com base no número de letras da senha
saida = ['_' for letra in senha]
# Transformar a saida em um iterável para que possa imprimir de maneira limpa
saida_limpa = iter(saida)
erros = 6


print(senha) # TODO: TIRAR
print(*saida_limpa)
print(erro0)

while erros > 0:
    entrada_usuario = input("PALPITE: ").upper()
    # Garantir que só sejam contabilizadas letras
    if entrada_usuario not in string.ascii_letters:
        print("Valor inválido. Insira uma letra.")
    else:
        # Verificar se o usuário acertou uma letra da senha e substituir o '_' pela letra certa
        if entrada_usuario in senha:
        # Inicia o index em 0 e itera por cada letra da senha
            index = 0
            for letra in senha:
                if entrada_usuario == letra:
                    saida[index] = entrada_usuario
                #Acrescenta 1 ao index para que letras repetidas sejam englobadas
                index += 1
            saida_limpa = iter(saida)
            print(*saida_limpa)
            # Todas as letras preenchidas = senha correta
            if '_' not in saida:
                print('Você acertou!!')
                break

        # Contabilizar os erros
        else:
            erros -= 1
            if erros != 0:
                print(f"Você errou! Restam {erros} erros.")
            # Tentativas esgotadas
            else:
                print(f"Você perdeu!")
                print(erro6)
        # Imprimir as imagens da forca com base no número de erros
        if erros == 6:
            print(erro0)
        elif erros == 5:
            print(erro1)
        elif erros == 4:
            print(erro2)
        elif erros == 3:
            print(erro3)
        elif erros == 2:
            print(erro4)
        elif erros == 1:
            print(erro5)

