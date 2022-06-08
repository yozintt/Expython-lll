numeroTimes = int(input('Quantos times estão disputando o campeonato? (máximo 50) '))
if numeroTimes > 50:
    print('Numero de times inválido!')
else:
    vencedor = 0
    pontos = 0
    numeroVencedores = 0
    for i in range (1, numeroTimes+1):
        pontos = int(input('Qual a pontuação do time {}? '.format(i)))
        if vencedor < pontos:
            vencedor = pontos
            numeroVencedores = 0
        if vencedor == pontos:
            numeroVencedores = numeroVencedores+1
    print('A pontuação dos times vencedores é {} e {} dividiram o titulo'.format(vencedor, numeroVencedores))
            