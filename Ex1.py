N = int(input('Digite o número (Maximo 50)'))
if N > 50:
    print('Valor de sequência não aceito!')
else:
    for C in range (N, 0, -1):
        print(C)
