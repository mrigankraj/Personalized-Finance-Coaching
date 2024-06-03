import pandas as pd

def generate_recommendations(df):
    recommendations = {}
    for user_id in df['user_id'].unique():
        user_data = df[df['user_id'] == user_id]
        total_spending = user_data.groupby('category')['amount'].sum()
        
        recs = []
        if total_spending['Entertainment'] > 0.2 * total_spending.sum():
            recs.append("Consider reducing your entertainment expenses.")
        
        if total_spending['Groceries'] > 0.3 * total_spending.sum():
            recs.append("Consider looking for discounts or cheaper grocery alternatives.")
        
        recommendations[user_id] = recs
    
    return recommendations

if __name__ == "__main__":
    df = pd.read_csv('../data/processed_data.csv')
    recommendations = generate_recommendations(df)
    for user, recs in recommendations.items():
        print(f"User {user}:")
        for rec in recs:
            print(f"  - {rec}")
