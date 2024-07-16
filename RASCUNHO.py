# lista = ['_','_','_','_','_','_']
# print(lista)
# lista_limpa = iter(lista)
# print(*lista_limpa)



        # if (chute in palavra_secreta):
        #     index = 0 # posição
        #     for letra in palavra_secreta:
        #         if (chute.upper() == letra.upper()):  # Transforma as duas em letras maiúsculas, para a comparação ser igual
        #             letras_acertadas[index] = letra # Sobrescreve na lista, na posição representada pelo index, a letra acertada no chute
        #         index = index + 1


# if entrada_usuario in senha:
#     # Inicia o index em 0 e itera por cada letra da senha
#     index = 0
#     for letra in senha:
#         if entrada_usuario == letra:
#             saida[index] = entrada_usuario
#         # Acrescenta 1 ao index para que letras repetidas sejam englobadas
#         index += 1
#     saida_limpa = iter(saida)
#     print(*saida_limpa)
#     # Todas as letras preenchidas = senha correta
#     if '_' not in saida:
#         print('Você acertou!!')
#         break


#     index_letra = senha.index(entrada_usuario)
#     saida[index_letra] = entrada_usuario
#     saida_limpa = iter(saida)
#     print(*saida_limpa)
#     # Todas as letras preenchidas = senha correta
#     if '_' not in saida:
#         print('Você acertou!!')
#         break



senha = 'banana'

saida = ['_' for letra in senha]
saida_limpa = (" ".join(saida))

print(saida)
print(saida_limpa)

saida = ['_', 'a', '_', 'a']
print(" ".join(saida))