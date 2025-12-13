import pandas as pd
from config import RAW_DATA_PATH

# Function load dataset
def load_dataset(file_name: str) -> pd.DataFrame:
    path = RAW_DATA_PATH / f'{file_name}.csv'
    df = pd.read_csv(path)
    return df
