
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validacao(cpf, multi, indice):
    valor = 0
    for numero in cpf[:indice]:
        valor += int(numero) * multi
        multi -= 1
    valor_final = (valor * 10) % 11
    return valor_final if valor_final <= 9 else 0

while True:

# Pegando as Informação
    while True:
        cpf = input('Informe seu cpf: ').replace('.', '').replace('-', '').replace(' ', '')
        limpar_tela()
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

# Calculo do Primeiro
    validacao_primeiro = validacao(cpf, multi=10, indice=9)

# Calculo do Segundo
    validacao_segundo = validacao(cpf, multi=11, indice=10)

# Formatação do CPF
    cpf_formatado = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]

# Validação
    if validacao_primeiro == int(cpf[9]) and validacao_segundo == int(cpf[10]):
        print(f'O Cpf {cpf_formatado} é valido')
    else:
        print(f'O Cpf {cpf_formatado} é invalido')
