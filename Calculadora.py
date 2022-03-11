while True:
    num = int(input('Informe um número para calcular (negativo para parar): '))
    quant = int(input('Informe a quantidade de vezes: '))

    print('-'*30)
    if num < 0:
        break
    for cont in range(1, quant+1):
        print('|', f'{num} X {cont:2} = {num*cont}', '|')
    print('-'*30)
print('Programa encerrado.')
