import csv

caminho_arquivo: str = 'Aula04/exemplo.csv'
arquivo_csv: list = []

# abrindo uma janela de contexto com with
with open(file=caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for i in leitor_csv:
        arquivo_csv.append(i)

print(arquivo_csv)