from load_data import load_dataset
from analysis import show_shape, show_head, show_missing_values, show_types_values
from clean_data import fill_age_by_sex_median, fill_embarked_value_frequent

def main():
    df_train = load_dataset("train")

    # análise inicial
    show_shape(df_train)
    show_head(df_train)
    show_missing_values(df_train)
    show_types_values(df_train)

    # limpeza
    df_train = fill_age_by_sex_median(df_train)
    df_train = fill_embarked_value_frequent(df_train)

    # Checar novamente após a limpeza
    show_missing_values(df_train)

if __name__ == "__main__":
    main()
