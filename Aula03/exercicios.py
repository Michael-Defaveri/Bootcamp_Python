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


# 2. Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

# %%
baixa = 15
normal = 22
alta = 29

temperatura = float(input('Digite um temperatura: '))

if temperatura < baixa:
    print('Temperatura baixa')

elif temperatura <= normal:
    print('Temperatura normal')

else:
    print('Temperatura alta')



# 3. Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
# Dado um registro de log em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# %%
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])


# 4. Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# %%
idade_user1 = 15
idade_user2 = 30
idade_user3 = 70

email_user1 = ['email_user1']
email_user2 = ['email_user2']
email_user3 = ['email_user3']

if idade_user1 >= 18 and idade_user1 <= 65 and email_user1 == email_user1:
    print('Dados de usuário válidos')

elif idade_user2 >= 18 and idade_user2 <= 65 and email_user2 == email_user2:
    print('Dados de usuário válidos')

elif idade_user3 >= 18 and idade_user3 <= 65 and email_user3 == email_user3:
    print('Dados de usuário válidos')

else:
    print('Dados de usuário inválidos')


# 5. Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. 
# Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

# %%
transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000 or (transacao['hora'] < 9 or transacao['hora'] > 18):
    print('Transação suspeita')
else:
    print('Transação normal')

6. Dado um texto, contar quantas vezes cada palavra única aparece nele.

# %%
texto = 'O homem andou até o outro homem não aguentar andar mais.'
palavras = texto.split()

contagem_palavras = {}

for i in palavras:
    if i in contagem_palavras:
        contagem_palavras[i] +=1
    else:
        contagem_palavras[i] = 1

print(contagem_palavras)

