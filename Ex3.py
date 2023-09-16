# Escreva um algoritmo que peça ao usuário 5 números, calcule e mostre a média desses 
#5 números e mostre ainda quantos, desses números, são maiores que a média.
somaNumero = 0
media = 0
maiormedia = 0
quantidadeDeNumeros = 5
todosOsNumeros = []
numerosMaioresQueAMedia = []

for n in range(0,quantidadeDeNumeros): 
    # Escrevendo o nome do numero que o usuario ira inserir EX: 1° número
    print('{}° número'.format(n+1))
    # Solicitando entrada de dados para o usuario
    numero = int(input('Digite um número: '))
    # somaNumero = somaNumero + numero
    somaNumero += numero
    # Adiciona numeros na lista de todos os numeros
    todosOsNumeros.insert(n, numero)

# Calcula a media
media = somaNumero / quantidadeDeNumeros

# Este for verifica quais os numeros sao maiores que a media
for n in range(0,quantidadeDeNumeros): 
    valorDaPosicao = todosOsNumeros[n]

    if(valorDaPosicao > media):
        numerosMaioresQueAMedia.append(valorDaPosicao)



print('Essa é a lista {}'.format(todosOsNumeros))
print('Essa é o valor da media {}'.format(media))
print('Essa é a lista de numeros maiores que a media {}'.format(numerosMaioresQueAMedia))
