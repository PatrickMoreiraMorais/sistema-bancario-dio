from  menu import exibir_menu
from tratamento import formatar_dinheiro,data_hora_atual_formatada

def realizar_saque(saldo, extrato, valor, saques_hoje):
    if valor > saldo:
        print('Saldo insuficiente para realizar o saque.')
    else:
        if saques_hoje <= 2:
            if valor > 500:
                print('Valor máximo para saque é de R$ 500,00. , Tente Novamente.')
            else:
                saldo -= valor
                hora_atual = data_hora_atual_formatada()
                extrato.append(f'Saque: {formatar_dinheiro(valor)}; {hora_atual}')
                print(f'Saque realizado com sucesso! Novo saldo: {formatar_dinheiro(saldo)}')
                saques_hoje += 1
                return saldo,saques_hoje
        else:
            print('Número máximo de saques diários atingido.')
    return saldo,saques_hoje

def realizar_deposito(saldo, extrato, valor):
    if valor <= 0:
        print('Valor inválido para depósito.')
    else:
        hora_atual = data_hora_atual_formatada()
        saldo += valor
        extrato.append(f'Depósito: {formatar_dinheiro(valor)}; {hora_atual}')
        print(f'Depósito realizado com sucesso! Novo saldo: {formatar_dinheiro(saldo)}')
        return saldo
    return saldo

def exibir_extrato(saldo, extrato):
    print('\n ============= Extrato =============')
    if not extrato:
        print('Não foram realizadas movimentações.')
    else:
        for item in extrato:
            print(item)
    print(f'\nSaldo atual: {formatar_dinheiro(saldo)}')
    print('====================================\n')


        
        
       
    
