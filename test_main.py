"""
Test goes here

"""

# test_main.py

import unittest
import pandas as pd
import main  # Assuming main.py is in the same directory

class TestMainMethods(unittest.TestCase):

    def setUp(self):
        # This method will be executed before each test method, setting up the data for the tests
        self.data = pd.DataFrame({
            'Age': [25, 30, 35, 40, 45],
            'Salary': [50000, 55000, 60000, 65000, 70000],
            'Score': [85, 89, 78, 90, 82]
        })

    def test_load_data(self):
        data = main.load_data('data.csv')
        self.assertTrue(isinstance(data, pd.DataFrame))  # Check if data is a DataFrame
        self.assertNotEqual(len(data), 0)  # Check if DataFrame is not empty

    def test_display_median(self):
        medians = {
            'Age': 35.0,
            'Salary': 60000.0,
            'Score': 85.0
        }
        for column in self.data.columns:
            self.assertEqual(self.data[column].median(), medians[column])

if __name__ == '__main__':
    unittest.main()
