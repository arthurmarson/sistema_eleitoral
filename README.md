# Sistema de Eleição Presidencial em Python

Este projeto é uma aplicação de console simples em Python que simula o processo de votação e apuração de uma eleição presidencial. Ele foi desenvolvido como parte de um trabalho acadêmico para o curso de Graduação em Engenharia de Software da UNIUBE, seguindo os requisitos especificados no enunciado do trabalho.

## Contexto do Projeto

O programa foi criado para atender ao seguinte enunciado:

> Resolva a questão a seguir utilizando a linguagem Python.
> Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
> 1 , 2, 3, 4  - Votos para os respectivos candidatos
> (você deve montar a tabela ex: 1 - José/ 2- João/etc)
> 5 - Voto Nulo
> 6 - Voto em Branco
> Faça um programa que calcule e mostre:
> O total de votos para cada candidato;
> O total de votos nulos;
> O total de votos em branco;
> A percentagem de votos nulos sobre o total de votos;
> A percentagem de votos em branco sobre o total de votos.
> O Candidato que venceu as eleições.

## Funcionalidades

O sistema implementa as seguintes funcionalidades:

* **Registro de Votos:** Permite que o usuário insira votos para quatro candidatos pré-definidos, além de registrar votos nulos e em branco.
* **Contagem de Votos:** Calcula o total de votos recebidos por cada candidato.
* **Contagem de Votos Nulos e em Branco:** Calcula o total de votos nulos e o total de votos em branco.
* **Cálculo de Percentuais:** Calcula a porcentagem de votos nulos e de votos em branco em relação ao número total de votos computados.
* **Determinação do Vencedor:** Identifica o candidato com o maior número de votos e o declara como vencedor. Em caso de empate, o programa informa os candidatos que empataram.
* **Interface de Console:** Interage com o usuário por meio de um menu de texto simples no console.
* **Validação de Entrada:** Verifica se a entrada do usuário é válida (números dentro do intervalo esperado).

## Estrutura do Código (`sistema_eleitoral.py`)

O código é estruturado da seguinte forma:

1.  **Inicialização:**
    * Uma mensagem de boas-vindas "ELEIÇÕES PRESIDENCIAIS - 2025" é exibida.
    * `candidatos`: Uma lista de strings que armazena os nomes dos candidatos e as opções de voto nulo/branco. O primeiro elemento é uma string vazia para que os índices da lista correspondam diretamente aos códigos de votação (1 a 6).
        * `candidatos[1]` = "José"
        * `candidatos[2]` = "Maria"
        * `candidatos[3]` = "João"
        * `candidatos[4]` = "Ana"
        * `candidatos[5]` = "Voto Nulo"
        * `candidatos[6]` = "Voto em Branco"
    * `votes`: Uma lista de inteiros, inicializada com zeros, com tamanho 7. Cada índice corresponde a uma opção de voto, armazenando a contagem de votos para essa opção.
    * `total`: Uma variável inteira, inicializada com 0, para rastrear o número total de votos válidos computados.

2.  **Loop de Votação (`while True`):**
    * O programa entra em um loop contínuo para coletar os votos.
    * A cada iteração, o menu de opções é exibido:
        ```
        Os números de cada candidato são:
        1 - José | 2 - Maria | 3 - João | 4 - Ana
        5 - Voto Nulo | 6 - Voto em Branco | 7 - Sair
        ```
    * **Entrada do Usuário:** O programa solicita que o usuário "Digite o número do seu voto: ".
    * **Tratamento de Erro (`try-except ValueError`):** Garante que o usuário insira um número inteiro. Se uma entrada não numérica for fornecida, uma mensagem de erro é exibida e o loop continua.
    * **Condição de Saída:** Se o usuário digitar `7`, o comando `break` encerra o loop de votação.
    * **Validação do Voto:** Verifica se o número digitado está entre 1 e 6 (inclusive). Se o voto for inválido (menor que 1 ou maior que 7, sendo 7 a saída), uma mensagem "Número inválido." é exibida, e o loop continua.
    * **Contabilização do Voto:** Se o voto for válido (1 a 6), o contador correspondente na lista `votes` é incrementado (`votes[voto] += 1`), e o `total` de votos também é incrementado.

3.  **Apuração e Exibição dos Resultados:**
    * Após a saída do loop de votação, a mensagem "\nResultados da Eleição:" é exibida.
    * **Votos por Candidato:** Um loop `for` itera de 1 a 4 para exibir o nome de cada candidato (de `candidatos[i]`) e o total de votos que recebeu (`votes[i]`).
    * **Votos Nulos e em Branco:** O total de votos nulos (`votes[5]`) e em branco (`votes[6]`) é exibido.
    * **Cálculo de Percentuais (se `total > 0`):**
        * Para evitar divisão por zero, os percentuais só são calculados se houver pelo menos um voto.
        * Percentual de Votos Nulos: `(votes[5] / total) * 100`, arredondado para 2 casas decimais.
        * Percentual de Votos em Branco: `(votes[6] / total) * 100`, arredondado para 2 casas decimais.
    * **Determinação do Vencedor (se `total > 0`):**
        * `highestValue = max(votes)`: Encontra o maior número de votos entre todas as opções (incluindo nulos e brancos, embora estes geralmente não sejam considerados para vitória).
        * `empate = [i for i, v in enumerate(votes) if v == highestValue]`: Cria uma lista com os índices de todos os candidatos/opções que alcançaram o `highestValue`.
        * **Verificação de Empate:**
            * Se `len(empate) > 1` (mais de uma opção com o maior número de votos), o programa informa que houve empate e lista os nomes e a quantidade de votos de cada um dos empatados.
            * Caso contrário (sem empate), `winner = empate[0]` (o primeiro e único índice na lista `empate`) é considerado o vencedor. O nome do vencedor (`candidatos[winner]`) e seus votos (`votes[winner]`) são exibidos.
    * **Nenhum Voto:** Se `total == 0` (nenhum voto foi computado), a mensagem "Nenhum voto foi computado." é exibida.

## Como Executar o Código

1.  **Pré-requisitos:**
    * Ter o Python 3 instalado no seu sistema.

2.  **Passos para Execução:**
    * Salve o código em um arquivo com a extensão `.py` (por exemplo, `sistema_eleitoral.py`).
    * Abra um terminal ou prompt de comando.
    * Navegue até o diretório onde você salvou o arquivo.
    * Execute o script usando o comando:
        ```bash
        python sistema_eleitoral.py
        ```
    * Siga as instruções exibidas no console para inserir os votos. Digite o número correspondente à sua escolha e pressione Enter.
    * Para finalizar a votação e visualizar os resultados, digite `7` e pressione Enter.

## Exemplo de Uso

ELEIÇÕES PRESIDENCIAIS - 2025

Os números de cada candidato são:
1 - José | 2 - Maria | 3 - João | 4 - Ana
5 - Voto Nulo | 6 - Voto em Branco | 7 - Sair

Digite o número do seu voto: 1

Os números de cada candidato são:
1 - José | 2 - Maria | 3 - João | 4 - Ana
5 - Voto Nulo | 6 - Voto em Branco | 7 - Sair

Digite o número do seu voto: 2

Os números de cada candidato são:
1 - José | 2 - Maria | 3 - João | 4 - Ana
5 - Voto Nulo | 6 - Voto em Branco | 7 - Sair

Digite o número do seu voto: 1

Os números de cada candidato são:
1 - José | 2 - Maria | 3 - João | 4 - Ana
5 - Voto Nulo | 6 - Voto em Branco | 7 - Sair

Digite o número do seu voto: 5

Os números de cada candidato são:
1 - José | 2 - Maria | 3 - João | 4 - Ana
5 - Voto Nulo | 6 - Voto em Branco | 7 - Sair

Digite o número do seu voto: 6

Os números de cada candidato são:
1 - José | 2 - Maria | 3 - João | 4 - Ana
5 - Voto Nulo | 6 - Voto em Branco | 7 - Sair

Digite o número do seu voto: 7

Resultados da Eleição:
- José obteve: 2 votos
- Maria obteve: 1 votos
- João obteve: 0 votos
- Ana obteve: 0 votos
- Total de Votos Nulo: 1
- Total de Votos em Branco: 1
- Porcentagem de Votos Nulo: 20.0%
- Porcentagem de Votos em Branco: 20.0%

O vencedor foi José com 2 votos

## Arthur de Oliveira Marson

Este código foi derivado de um trabalho acadêmico da Graduação de Engenharia de Software da UNIUBE.
