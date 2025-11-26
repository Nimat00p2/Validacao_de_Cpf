
import os
import random

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

# Gerando Cpf Aleatorio
    cpf_parcial = ''
    for i in range(9):
        cpf_parcial += str(random.randint(0, 9))

# Calculo do Primeiro
    numero_gerado_1 = validacao(cpf_parcial, multi=10, indice=9)
    cpf_parcial += str(numero_gerado_1)

# Calculo do Segundo
    numero_gerado_2 = validacao(cpf_parcial, multi=11, indice=10)
    cpf_parcial += str(numero_gerado_2)

# Formatação do CPF
    cpf_formatado = cpf_parcial[:3] + '.' + cpf_parcial[3:6] + '.' + cpf_parcial[6:9] + '-' + cpf_parcial[9:]

    limpar_tela()
    input(f'Cpf {cpf_formatado} gerado')
