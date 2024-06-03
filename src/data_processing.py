import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    df['date'] = pd.to_datetime(df['date'])
    return df

if __name__ == "__main__":
    df = load_data('../data/sample_data.csv')
    df = preprocess_data(df)
    df.to_csv('../data/processed_data.csv', index=False)
