# ## Exercícios de Python - Aula 03

# #1. Verificação de Qualidade de Dados
# # Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. 
# # Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

# # %%
# try:
#     print('Verificação de Qualidade de Dados')
    
#     quantidade = int(input('Digite uma quantidade: '))
#     preco = float(input('Digite um preço: '))

#     # Agora verificamos se são positivos
#     if quantidade > 0 and preco > 0:
#         print('Dados válidos, pois são numéricos e positivos.')

#     elif quantidade > 0 and preco < 0:
#         print('Dados inválidos, pois o preço não é positivo. Tente novamente')
#         preco = float(input('Digite um preço positivo desta vez ou o programa irá encerrar: '))

#         if preco < 0:
#             print('Programa encerrado')
#             exit()

#     elif quantidade < 0 and preco > 0:
#         print('Dados inválidos, pois a quantidade não é positiva.')
#         quantidade = int(input('Digite uma quantidade positiva desta vez ou o programa irá encerrar: '))
        
#         if quantidade < 0:
#             print('Programa encerrado')
#             exit()
#     else:
#         print('Dados inválidos, pois ambos não são positivos')

# except ValueError:
#     print('Erro: Use apenas números. Espaços ou letras não são permitidos.')


# # Exercicio 1 Versao 2
# # %% 
# try:
#     print('--- Verificação de Qualidade de Dados ---')
    
#     quantidade = int(input('Digite uma quantidade: '))
#     # Enquanto o número for menor ou igual a zero, ele pede de novo
#     while quantidade <= 0:
#         print('A quantidade deve ser positiva!')
#         quantidade = int(input('Digite uma quantidade válida: '))

#     preco = float(input('Digite um preço: '))
#     while preco <= 0:
#         print('O preço deve ser positivo!')
#         preco = float(input('Digite um preço válido: '))

#     print(f'✅ Sucesso! Qtd: {quantidade} | Preço: R${preco:.2f}')

# except ValueError:
#     print('❌ Erro: Entrada inválida. Digite apenas números sem espaços ou letras.')


# # 2. Classificação de Dados de Sensor
# # Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. 
# # Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# # Temperatura < 18°C é 'Baixa'
# # Temperatura >= 18°C e <= 26°C é 'Normal'
# # Temperatura > 26°C é 'Alta'

# # %%
# baixa = 15
# normal = 22
# alta = 29

# temperatura = float(input('Digite um temperatura: '))

# if temperatura < baixa:
#     print('Temperatura baixa')

# elif temperatura <= normal:
#     print('Temperatura normal')

# else:
#     print('Temperatura alta')



# # 3. Filtragem de Logs por Severidade
# # Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
# # Dado um registro de log em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
# # escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# # %%
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     print(log['message'])


# # 4. Validação de Dados de Entrada
# # Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# # Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# # %%
# idade_user1 = 15
# idade_user2 = 30
# idade_user3 = 70

# email_user1 = ['email_user1']
# email_user2 = ['email_user2']
# email_user3 = ['email_user3']

# if idade_user1 >= 18 and idade_user1 <= 65 and email_user1 == email_user1:
#     print('Dados de usuário válidos')

# elif idade_user2 >= 18 and idade_user2 <= 65 and email_user2 == email_user2:
#     print('Dados de usuário válidos')

# elif idade_user3 >= 18 and idade_user3 <= 65 and email_user3 == email_user3:
#     print('Dados de usuário válidos')

# else:
#     print('Dados de usuário inválidos')


# # 5. Detecção de Anomalias em Dados de Transações
# # Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. 
# # Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# # Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

# # %%
# transacao = {'valor': 12000, 'hora': 20}

# if transacao['valor'] > 10000 or (transacao['hora'] < 9 or transacao['hora'] > 18):
#     print('Transação suspeita')
# else:
#     print('Transação normal')

# 6. Dado um texto, contar quantas vezes cada palavra única aparece nele.

# # %%
# texto = 'O homem andou até o outro homem não aguentar andar mais.'
# palavras = texto.split()

# contagem_palavras = {}

# for i in palavras:
#     if i in contagem_palavras:
#         contagem_palavras[i] +=1
#     else:
#         contagem_palavras[i] = 1

# print(contagem_palavras)


# #  7. Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# # %%
# numeros = [100, 200, 300, 400, 500]
# maximo = max(numeros)
# minimo = min(numeros)

# normalizados = []

# for i in numeros:
#     resultado = (i - minimo) / (maximo - minimo)
#     normalizados.append(resultado) # O método append adiciona um elemento ao final da lista e não funciona para dicionários

# print(normalizados)

# # 8. Filtragem de Dados Faltantes
# # Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validos = []

# for u in usuarios:
#     if u['email']:
#         usuarios_validos.append(u)
#     else:
#         print(f'Usuário {u['nome']} inválido')

# print(usuarios_validos)

# # 9. Extração de Subconjuntos de Dados
# # Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

# # %%
# numeros = range(10, 31)
# pares = [p for p in numeros if p % 2 == 0]
# print(pares)

# # Método tradicional
# for p in numeros:
#     if p % 2 == 0:
#         pares.append(p)
# print(pares)


# # 10. Agregação de Dados por Categoria
# # Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# # %%
# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# total_por_categoria = {}

# for i in vendas:
#     categoria = i['categoria']
#     valor = i['valor']
#     if categoria in total_por_categoria:
#         total_por_categoria[categoria] += valor
#     else:
#         total_por_categoria[categoria] = valor

# print(total_por_categoria)


#11. Leitura de Dados até Flag
#Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# %%



#12. Validação de Entrada
#Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# %%



#13. Consumo de API Simulado
#Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# %%




#14. Tentativas de Conexão
#Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# %%



#15. Processamento de Dados com Condição de Parada
#Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.

# %%