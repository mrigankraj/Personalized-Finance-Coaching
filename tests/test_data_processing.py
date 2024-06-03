import unittest
import pandas as pd
from src.data_processing import preprocess_data

class TestDataProcessing(unittest.TestCase):
    
    def test_preprocess_data(self):
        data = {'date': ['2024-01-01', '2024-01-02'], 'category': ['Groceries', 'Rent'], 'amount': [50, 700]}
        df = pd.DataFrame(data)
        df = preprocess_data(df)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(df['date']))

if __name__ == '__main__':
    unittest.main()
