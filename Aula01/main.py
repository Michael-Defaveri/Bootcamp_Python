# Crie um programa que o usuário digita o nome dele 
# e o programa retorna o número de caracteres do nome sem contar espaços em branco.

# %%
nome_usuario = input("Digite seu nome: ")
print("O número de caracteres do seu nome é: ", len(nome_usuario.replace(" ", "")))


# Crie um programa onde o usuário digita dois números e tenha a soma dos valores.abs
# %%
valor1 = input('Digite o primeiro número: ')
valor2 = input('Digite o segunda número: ')

print('A soma dos valores é:', int(valor1) + int(valor2))



## DESAFIO AULA 01
# Crie um programa onde o usuário digite o nome, salario, porcentagem de bonus e receba o valor do bonus.abs

# %%
nome_user = input('Digite o seu nome: ')
salario = float(input('Digite o seu salário: '))
percentual_bonus = float(input('Digite o valor do bônus em porcentagem: '))

valor_bonus = salario * (percentual_bonus / 100)
print(f'O valor do bônus é: , {valor_bonus}')
print(f'{nome_user} o valor total com o bônus é: , {salario + valor_bonus}')