import pandas as pd
from data_processing import load_data, preprocess_data
from analytics import get_monthly_spending, get_total_spending
from recommendations import generate_recommendations

def main():
    df = load_data('../data/sample_data.csv')
    df = preprocess_data(df)
    
    monthly_spending = get_monthly_spending(df)
    total_spending = get_total_spending(df)
    
    recommendations = generate_recommendations(df)
    
    print("Monthly Spending:")
    print(monthly_spending)
    print("\nTotal Spending:")
    print(total_spending)
    print("\nRecommendations:")
    for user, recs in recommendations.items():
        print(f"User {user}:")
        for rec in recs:
            print(f"  - {rec}")

if __name__ == "__main__":
    main()
