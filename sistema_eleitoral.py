print("ELEIÇÕES PRESIDENCIAIS - 2025")

# Lista dos candidatos (o primeiro elemento é uma string vazia para facilitar a indexação)
candidatos = ["", "José", "Maria", "João", "Ana", "Voto Nulo", "Voto em Branco"]

# Lista para armazenar a contagem de votos para cada opção (inicializada com zeros)
votes = [0] * 7

# Variável para armazenar o total de votos
total = 0

# Loop principal para a votação
while True:
    print("\nOs números de cada candidato são:")
    print("1 - José | 2 - Maria | 3 - João | 4 - Ana")
    print("5 - Voto Nulo | 6 - Voto em Branco | 7 - Sair")

    # Bloco try-except para lidar com a entrada do usuário (garantir que seja um número inteiro)
    try:
        voto = int(input("Digite o número do seu voto: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número entre 1 e 7.")
        continue  # Volta para o início do loop

    # Verifica se o usuário deseja sair
    if voto == 7:
        break  # Sai do loop de votação

    # Verifica se o voto é válido
    if voto < 1 or voto > 7:
        print("Número inválido.")
        continue  # Volta para o início do loop

    # Incrementa a contagem de votos para o candidato escolhido
    votes[voto] += 1
    total += 1  # Incrementa o total de votos

# Resultados da Eleição
print("\nResultados da Eleição:")

# Imprime o número de votos para cada candidato
for i in range(1, 5):
    print(f"{candidatos[i]} obteve: {votes[i]} votos")

# Imprime o total de votos nulos e em branco
print(f"Total de Votos Nulo: {votes[5]}")
print(f"Total de Votos em Branco: {votes[6]}")

# Verifica se houve votos para calcular as porcentagens
if total > 0:
    # Calcula e imprime a porcentagem de votos nulos
    print(f"Porcentagem de Votos Nulo: {round((votes[5] / total) * 100, 2)}%")
    # Calcula e imprime a porcentagem de votos em branco
    print(f"Porcentagem de Votos em Branco: {round((votes[6] / total) * 100, 2)}%\n")

    # Encontra o maior número de votos
    highestValue = max(votes)

    # Encontra os candidatos com o maior número de votos (pode haver empate)
    empate = [i for i, v in enumerate(votes) if v == highestValue]

    # Verifica se houve empate
    if len(empate) > 1:
        print("Houve empate entre:")
        # Imprime os candidatos que empataram
        for i in empate:
            print(f"{candidatos[i]} com {votes[i]} votos")
    else:
        # Determina o vencedor (se não houver empate)
        winner = empate[0]
        print(f"O vencedor foi {candidatos[winner]} com {votes[winner]} votos")
else:
    # Caso não tenha ocorrido votação
    print("Nenhum voto foi computado.")