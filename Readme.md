# Análise de Dados – Titanic

## Objetivo
Projeto de análise de dados utilizando Python e Pandas para explorar o dataset do Titanic.

## Dataset
Fonte: Kaggle – Titanic: Machine Learning from Disaster.
- **train.csv** – dados principais para análise exploratória
- **test.csv** – dados para possível modelagem futura

## Tecnologias
- Python
- Pandas
- NumPy
- Matplotlib

## Estrutura do Projeto
Projeto estruturado utilizando scripts Python, sem o uso de notebooks.

## Análise de Valores Ausentes

Após a inspeção inicial do dataset, foram identificados os seguintes valores ausentes:

- **Age**: 177 valores ausentes (20%)
- **Cabin**: 687 valores ausentes (77%)
- **Embarked**: 2 valores ausentes

## Estratégia de Limpeza de Dados

### Coluna Age
- Variável  relevante para a análise de sobrevivência
- Os valores ausentes foram preenchidos utilizando a **mediana da idade por sexo**
- A mediana foi escolhida por ser mais resistentes a variações

### Coluna Embarked
- Possui apenas 2 valores ausentes
- Os valores ausentes foram preenchidos com o **valor mais frequente (moda)** da coluna


### Coluna Cabin
- Não foi realizada a limpeza da coluna
- A coluna será utilizada posteriormente para **criação de variáveis categóricas**

## Transformações e Feature Engineering

As transformações serão realizadas no arquivo `transform_data.py`, incluindo:

- Criação de variáveis categóricas a partir da coluna `Cabin`
- Criação de variáveis derivadas relacionadas à estrutura familiar
- Conversão de tipos quando necessário para análise

## Status

Em desenvolvimento.

## Execução do Projeto

Para executar o pipeline principal:

```bash
python src/main.py



