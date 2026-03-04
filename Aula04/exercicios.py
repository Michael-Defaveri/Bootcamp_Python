# 1.Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

numeros = list(range(1, 11))

for i in numeros:
    print(i ** 2)

# 2.Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

lista: list = ["Python", "Java", "C++", "JavaScript"]
lista.remove("C++")
lista.insert(2, "Ruby")

print(lista)

# 3.Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livro: dict = {"titulo": "Amor", "autor": "Deus", "ano_publicacao": "Eternidade"}

for i in livro.items():
    print(i)

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

def contar_caracteres(letra: str) -> dict:
    contagem: dict = {}
    for caractere in letra:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))

5.Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista: list = ["maçã", "banana", "cereja"]
precos: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

preco_total: float = 0

for i in lista:
    preco_total += precos[i]

print(preco_total)
