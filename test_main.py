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

    def test_display_salary_larger_than_60000(self):
        data = self.data[self.data['Salary'] > 60000]
        self.assertEqual(len(data), 2)  # Ensure the output only contains 2 entries
        # Ensure the output contains the entry with a salary of 65000
        self.assertTrue(65000 in data['Salary'].values)
        self.assertTrue(70000 in data['Salary'].values)

        # Ensure the output does not contain entries with a salary less than or equal to 60000
        self.assertFalse(50000 in data['Salary'].values)
        self.assertFalse(55000 in data['Salary'].values)
        self.assertFalse(60000 in data['Salary'].values)

if __name__ == '__main__':
    unittest.main()
