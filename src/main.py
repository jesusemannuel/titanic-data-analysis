from load_data import load_dataset
from analysis import show_shape, show_head, show_missing_values

def main():
    
    df_train = load_dataset("train")

    show_shape(df_train)
    show_head(df_train)
    show_missing_values(df_train)



    

if __name__ == "__main__":
    main()