import pandas as pd


def fill_age_by_sex_median(df: pd.DataFrame):
    """
    Preenche valores ausentes da coluna Age com a mediana calculada por sexo.
    """

    df['Age'] = (df.groupby('Sex')['Age']
                 .transform(lambda x: x.fillna(x.median()))
                 )
    
    return df
    
    
def fill_embarked_value_frequent(df: pd.DataFrame):
    
    """
    Preenche os valores ausentes da coluna Embarked pelo mais frequente (moda)
    Como o fillna espera apenas um valor escalar, vou calcular a moda antes e depois atribuir esse valor a coluna
    """
    
    most_freq = df['Embarked'].mode()[0]

    df['Embarked'] = df['Embarked'].fillna(most_freq)
    
    
    return df