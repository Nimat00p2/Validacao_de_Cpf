
import os
import random
import sys

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validacao(cpf, multi, indice):
    valor = 0
    for numero in cpf[:indice]:
        valor += int(numero) * multi
        multi -= 1
    valor_final = (valor * 10) % 11
    return valor_final if valor_final <= 9 else 0

def validacao_cpf():
    while True:
        cpf = input('\nEscreva "sair" para sair\n\nInforme seu cpf: ').replace('.', '').replace('-', '').replace(' ', '')
        limpar_tela()
        if cpf == 'sair':
            return
        if not cpf.isdigit():
            print('Digite apenas numeros')
            continue
        if cpf == cpf[0] * 11:
            print('Digitou o mesmo numero')
            continue
        if len(cpf) != 11:
            print('Quantidade de numeros invalido')
            continue
        break

    validacao_primeiro = validacao(cpf, multi=10, indice=9)
    validacao_segundo = validacao(cpf, multi=11, indice=10)
    cpf_formatado = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]

    if validacao_primeiro == int(cpf[9]) and validacao_segundo == int(cpf[10]):
        print(f'O Cpf {cpf_formatado} é valido')
    else:
        print(f'O Cpf {cpf_formatado} é invalido')

    input('\nEnter para continuar...\n')
    limpar_tela()

def gerador_cpf(quantidade):
    limpar_tela()
    print('')
    for _ in range(int(quantidade)):
        cpf_parcial = ''
        for _ in range(9):
            cpf_parcial += str(random.randint(0, 9))

        numero_gerado_1 = validacao(cpf_parcial, multi=10, indice=9)
        cpf_parcial += str(numero_gerado_1)

        numero_gerado_2 = validacao(cpf_parcial, multi=11, indice=10)
        cpf_parcial += str(numero_gerado_2)

        cpf_formatado = cpf_parcial[:3] + '.' + cpf_parcial[3:6] + '.' + cpf_parcial[6:9] + '-' + cpf_parcial[9:]
        print(f'Cpf {cpf_formatado} gerado')

    input('\nEnter para continuar...\n')
    limpar_tela()



while True:
    resposta = input(
        '\n---Cpf Completo---\n\n'
        'Qual opção deseja?\n'
        '1-Validar Cpf\n'
        '2-Gerar Cpf\n'
        '3-Sair\n\n'
    )
    limpar_tela()

    if resposta == '1':
        validacao_cpf()

    elif resposta == '2':
        quantidade = input('Maximo de 100\nQuantidade de Cpf que deseja gerar: ').replace(' ', '')
        if not quantidade.isdigit():
            print('Digite apenas numeros\n')
            continue
        if int(quantidade) >= 101:
            print('Limite maximo de 100')
            continue
        quantidade = quantidade if int(quantidade) >= 1 else 1
        gerador_cpf(quantidade)

    elif resposta == '3':
        print('Saindo do Sistema')
        sys.exit()

    else:
        print('Resposta Invalida')

