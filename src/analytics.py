import pandas as pd

def get_monthly_spending(df):
    df['month'] = df['date'].dt.to_period('M')
    return df.groupby(['user_id', 'month', 'category'])['amount'].sum().reset_index()

def get_total_spending(df):
    return df.groupby(['user_id', 'category'])['amount'].sum().reset_index()

if __name__ == "__main__":
    df = pd.read_csv('../data/processed_data.csv')
    monthly_spending = get_monthly_spending(df)
    total_spending = get_total_spending(df)
    print(monthly_spending)
    print(total_spending)
