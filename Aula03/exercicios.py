## Exercícios de Python - Aula 03

#1. Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

# %%
try:
    print('Verificação de Qualidade de Dados')
    
    quantidade = int(input('Digite uma quantidade: '))
    preco = float(input('Digite um preço: '))

    # Agora verificamos se são positivos
    if quantidade > 0 and preco > 0:
        print('Dados válidos, pois são numéricos e positivos.')

    elif quantidade > 0 and preco < 0:
        print('Dados inválidos, pois o preço não é positivo. Tente novamente')
        preco = float(input('Digite um preço positivo desta vez ou o programa irá encerrar: '))

        if preco < 0:
            print('Programa encerrado')
            exit()

    elif quantidade < 0 and preco > 0:
        print('Dados inválidos, pois a quantidade não é positiva.')
        quantidade = int(input('Digite uma quantidade positiva desta vez ou o programa irá encerrar: '))
        
        if quantidade < 0:
            print('Programa encerrado')
            exit()
    else:
        print('Dados inválidos, pois ambos não são positivos')

except ValueError:
    print('Erro: Use apenas números. Espaços ou letras não são permitidos.')


# Exercicio 1 Versao 2
# %% 
try:
    print('--- Verificação de Qualidade de Dados ---')
    
    quantidade = int(input('Digite uma quantidade: '))
    # Enquanto o número for menor ou igual a zero, ele pede de novo
    while quantidade <= 0:
        print('A quantidade deve ser positiva!')
        quantidade = int(input('Digite uma quantidade válida: '))

    preco = float(input('Digite um preço: '))
    while preco <= 0:
        print('O preço deve ser positivo!')
        preco = float(input('Digite um preço válido: '))

    print(f'✅ Sucesso! Qtd: {quantidade} | Preço: R${preco:.2f}')

except ValueError:
    print('❌ Erro: Entrada inválida. Digite apenas números sem espaços ou letras.')


# %%
