# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# %%
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
resultado = n1 + n2
print(f'O valor da soma de {n1} + {n2} é de:  {resultado}')

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# %%
n_user = int(input('Digite um número: '))
resto_div = n_user % 5
print(f'O resto da divisão de {n_user} por 5 é de: {resto_div}')

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# %%
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
resultado = n1 * n2
print(f'O valor da multiplicação de {n1} por {n2} é de: {resultado}')

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#%%
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
resultado = n1 // n2
print(f'O valor da divisão inteiro de {n1} por {n2} é de: {resultado}')

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# %%
number_user = int(input('Digite um número: '))
resultado = number_user ** 2
print(f'O valor do quadrado de {number_user} é de: {resultado}')


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
#%%
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
resultado = n1 = n2
print(f'O valor da soma dos dois número é de: {resultado}')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# %%
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
resultado = (n1 + n2) / 2
print(f'O valor da média de {n1} e {n2} é de: {resultado}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#%%
base = float(input('Digite um número: '))
expoente = float(input('Digite outro número: '))
resultado = base ** expoente
print(f'O valor da potência de {base} por {expoente} é de: {resultado}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# %%
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (celsius * 9/5) + 32
print(f'A temperatura de {celsius}°C é de {fahrenheit}°F')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# %%
raio = float(input('Digite o raio do círculo: '))
area = 3.14 * raio ** 2
print(f'A área do círculo é de: {area}')

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#%%
string_user = str(input('Digite uma palavra: '))
maius = string_user.upper()
print(f'{string_user} convertido para maiúsculo é {maius}')

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# %%
name = str(input('Digite o seu nome: '))
name_lower = name.lower()
print(f'O seu nome em minúsculo é: {name_lower}')

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# %%
frase = str(input('Digite uma frase: '))
frase_sem_esppacos = frase.replace(" ", "")
print(f'Sua frase sem espaços ficaria dessa forma: {frase_sem_esppacos}')

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# %%
data = str(input('Digite o uma data no formato dd/mm/aaaa: '))
data_formatada = data.split('/')
print(f'O dia é {data_formatada[0]}')
print(f'O mês é {data_formatada[1]}')
print(f'O ano é {data_formatada[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# %%
texto1 = str(input('Digite um texto: '))
texto2 = str(input('Digite outro texto: '))
resultado = texto1 + ' ' + texto2
print(f'A concatenação dos dois textos é: {resultado}')

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# %%
homem = input('Você é homem? (True/False): ').strip().capitalize()
mulher = input('Você é mulher? (True/False): ').strip().capitalize()
homem_bool = homem == 'True'
mulher_bool = mulher == 'True'
validacao = homem_bool and mulher_bool
print(f'Validação: {validacao}')

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# %%
valor1 = input('Você é maior de 18 anos?: ').strip().capitalize()
valor2 = input('Você é homem?: ').strip().capitalize()
valor1_bool = valor1 == 'Sim'
valor2_bool = valor2 == 'Sim'
resultado = valor1_bool or valor2_bool
print(f'É maior de 18 anos ou é homem?: {resultado}')

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# %%
valor1 = input('Digite um valor booleano (True/False): ').strip().lower()
valor1_bool = valor1 == 'true'
valor_invertido = not valor1_bool
print(f'O valor invertido é: {valor_invertido}')

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# %%
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
validacao = n1 == n2
print(f'Os números são iguais?: {validacao}')

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# %%
n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número: '))
validacao = n1 != n2
print(f'Os números são diferentes?: {validacao}')



# #### try-except e if

# 21: Conversor de Temperatura
# %%
try:
    temperatura = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (temperatura * 9/5) + 32
    print(f'A temperatura de {temperatura}°C é de {fahrenheit}°F')
except ValueError:
    print('Erro: Digite um número numérico válido: 10, 20, -15.5 etc.')

# 22: Verificador de Palíndromo
# %%
try:
    palavra = str(input('Digite uma palavra: '))
    palavra = palavra.replace(" ", "").lower()
    palavra_invertida = palavra[::-1]
    if isinstance(palavra, str):
        print(f'A variável {palavra} é uma string')
    else:
        print(f'A variável {palavra} não é uma string')
    if palavra == palavra_invertida:
        print(f'A palavra é um palíndromo')
    else:
        print(f'A palavra não é um palíndromo')
except ValueError:
    print('Erro: Digite uma string válida')

# 23: Calculadora Simples
# %%
try:
    n1 = float(input('Digite um número: '))
    operacao = input('Digite a operação (+, -, *, /, **, %): ')
    n2 = float(input('Digite outro número: '))

    resultado = None

    if operacao == '+':
        resultado = n1 + n2
    elif operacao == '-':
        resultado = n1 - n2
    elif operacao == '*':
        resultado = n1 * n2
    elif operacao == '/':
        if n2 == 0:
            print('Erro: Divisão por zero.')
        else:
            resultado = n1 / n2
    elif operacao == '**':
        resultado = n1 ** n2
    elif operacao == '%':
        resultado = n1 % n2
    else:
        print('Operação inválida.')

    if resultado is not None:
        print(f'O resultado da operação é: {resultado}')

except ValueError:
    print('Erro: Digite números válidos (10, -12.5, 0 etc.)')

# 24: Classificador de Números
# %%
valor_usuario_raw = input('Digite um número: ')

try:
    valor_usuario = float(valor_usuario_raw)

    print(f'Variável {valor_usuario} é um número')

    if valor_usuario > 0:
        print(f'O valor é positivo')
    elif valor_usuario < 0:
        print(f'O valor é negativo')
    else:
        print(f'O valor é zero')

    if valor_usuario % 2 == 0:
        print(f'O valor é par')
    else:
        print(f'O valor é ímpar')

except ValueError:
    print(f'Erro: "{valor_usuario_raw}" não é um número válido. Digite um número inteiro ou decimal.')
        
        
# 25: Conversão de Tipo com Validação
# %%
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")