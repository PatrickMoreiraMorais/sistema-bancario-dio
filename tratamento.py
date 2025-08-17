from datetime import datetime

def entrar_com_float(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('Valor inválido. Por favor, Tente novamente.')

def entrar_com_inteiro(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Valor inválido. Por favor, Tente novamente.')

def formatar_dinheiro(valor):
    return f'R$ {valor:.2f}'




def data_hora_atual_formatada():
    agora = datetime.now()
    return agora.strftime('%d/%m/%y %H:%M')

