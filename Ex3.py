# Escreva um algoritmo que peça ao usuário 10 números, calcule e mostre a média desses 
#10 números e mostre ainda quantos, desses números, são maiores que a média.
somaNumero = 0
media = 0
maiormedia = 0

for n in range(0,3):
    print('{}° número'.format(n))
    numero = int(input('Digite um número: '))
    somaNumero += numero
    if maiormedia > media:
        
        
        
        
media = somaNumero / 3
print ('A media dos seus 10 números é igual a:{} '.format(media))