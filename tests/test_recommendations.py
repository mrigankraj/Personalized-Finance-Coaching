import unittest
import pandas as pd
from src.recommendations import generate_recommendations

class TestRecommendations(unittest.TestCase):
    
    def test_generate_recommendations(self):
        data = {'user_id': [1, 1, 2], 'date': ['2024-01-01', '2024-01-03', '2024-01-02'], 'category': ['Groceries', 'Entertainment', 'Groceries'], 'amount': [50, 200, 60]}
        df = pd.DataFrame(data)
        recommendations = generate_recommendations(df)
        self.assertIn(1, recommendations)
        self.assertIn(2, recommendations)

if __name__ == '__main__':
    unittest.main()
