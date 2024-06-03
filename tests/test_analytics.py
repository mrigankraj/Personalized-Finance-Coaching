import unittest
import pandas as pd
from src.analytics import get_monthly_spending, get_total_spending

class TestAnalytics(unittest.TestCase):
    
    def test_get_monthly_spending(self):
        data = {'user_id': [1, 1, 2], 'date': ['2024-01-01', '2024-01-03', '2024-01-02'], 'category': ['Groceries', 'Rent', 'Groceries'], 'amount': [50, 700, 60]}
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        monthly_spending = get_monthly_spending(df)
        self.assertEqual(len(monthly_spending), 3)
        
    def test_get_total_spending(self):
        data = {'user_id': [1, 1, 2], 'date': ['2024-01-01', '2024-01-03', '2024-01-02'], 'category': ['Groceries', 'Rent', 'Groceries'], 'amount': [50, 700, 60]}
        df = pd.DataFrame(data)
        total_spending = get_total_spending(df)
        self.assertEqual(len(total_spending), 3)

if __name__ == '__main__':
    unittest.main()
