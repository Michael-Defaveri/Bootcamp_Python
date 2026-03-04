def validacao_nome_usuario() -> str:
    while True:
        nome = input("Digite seu nome: ").strip()
        if not nome:
            print("Erro: O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            print("Erro: O nome não deve conter números.")
        elif len(nome) < 2:
            print("Erro: Nome muito curto.")
        else:
            return nome

def validacao_valor(frase_input: str) -> float:
    """Função genérica para validar números (salário ou bônus)"""
    while True:
        try:
            valor = float(input(frase_input))
            if valor < 0:
                print("Erro: Digite um valor positivo.")
                continue
            return valor
        except ValueError:
            print("Erro: Entrada inválida. Digite um número.")


usuario = {}

# Alimentando o dicionário usando as funções
usuario["nome"] = validacao_nome_usuario()
usuario["salario"] = validacao_valor("Digite o seu salário: ")
usuario["bonus_percentual"] = validacao_valor("Digite o valor do bônus (em %): ")

# Calculando o valor final e guardando no dicionário também
usuario["valor_bonus"] = usuario["salario"] * (usuario["bonus_percentual"] / 100)
usuario["total"] = usuario["salario"] + usuario["valor_bonus"]

print("-" * 60)
print(f"Relatório de {usuario['nome']}:")
print(f"Salário Base: R${usuario['salario']:.2f}")
print(f"Bônus ({usuario['bonus_percentual']}%): R${usuario['valor_bonus']:.2f}")
print(f"Total a Receber: R${usuario['total']:.2f}")