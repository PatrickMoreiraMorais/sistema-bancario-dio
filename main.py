from menu import exibir_menu
from tratamento import entrar_com_float, entrar_com_inteiro
from banco import *
saldo = 1500
extrato = []
saques_hoje = 0

while True:
    exibir_menu()
    opcao = entrar_com_inteiro('Escolha uma opção: ')   
    
    if opcao == 1:  
        valor = entrar_com_float('Digite o valor do depósito: ')
        saldo = realizar_deposito(saldo, extrato, valor)
        
            
    elif opcao == 2: 
        valor = entrar_com_float('Digite o valor do saque: ')
        saldo,saques_hoje = realizar_saque(saldo, extrato, valor, saques_hoje)
    
    elif opcao == 3:  
        exibir_extrato(saldo, extrato)
    elif opcao == 0:  
        print('Saindo... Obrigado por usar nosso sistema bancário!')
        break
    else:
        print('Opção inválida, por favor selecione novamente.')