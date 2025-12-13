import pandas as pd

def show_shape(df: pd.DataFrame) -> None:
    print('Analisar as dimensões do dataset:')
    print(df.shape)


def show_head(df: pd.DataFrame, n = 5):
    print(f'Primeiras {n} linhas:')
    print(df.head(n))


def show_missing_values(df: pd.DataFrame) -> None:
    print(f'Valores ausentes por colunas:')
    print(df.isna().sum())

