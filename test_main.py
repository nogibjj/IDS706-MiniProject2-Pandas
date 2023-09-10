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

        # Creating a sample CSV for testing
        self.data.to_csv('test_data.csv', index=False)

    def test_load_data(self):
        data = main.load_data('test_data.csv')
        self.assertTrue(isinstance(data, pd.DataFrame))  # Check if data is a DataFrame
        self.assertNotEqual(len(data), 0)  # Check if DataFrame is not empty

    def test_display_data(self):
        # Testing display_data function by capturing printed output
        from io import StringIO
        import sys

        backup = sys.stdout

        # Switch stdout to capture printed output
        sys.stdout = StringIO()
        main.display_data(self.data)
        output = sys.stdout.getvalue()

        sys.stdout = backup  # Restore original stdout
        self.assertIn("Data preview:", output)
        self.assertIn("25", output)

    def test_display_basic_statistics(self):
        # Similar to test_display_data, capture output and check if required data is printed
        from io import StringIO
        import sys

        backup = sys.stdout

        sys.stdout = StringIO()
        main.display_basic_statistics(self.data)
        output = sys.stdout.getvalue()

        sys.stdout = backup
        self.assertIn("Basic Descriptive Statistics:", output)
        self.assertIn("mean", output)

    def test_display_median(self):
        # Again, capture output and verify
        from io import StringIO
        import sys

        backup = sys.stdout

        sys.stdout = StringIO()
        main.display_median(self.data)
        output = sys.stdout.getvalue()

        sys.stdout = backup
        self.assertIn("Median of Age: 35.0", output)

    def test_display_mode(self):
        # Similarly, capture output and verify for mode
        from io import StringIO
        import sys

        backup = sys.stdout

        sys.stdout = StringIO()
        main.display_mode(self.data)
        output = sys.stdout.getvalue()

        sys.stdout = backup
        self.assertIn("Mode of Age: 25", output)

    def tearDown(self):
        # This method will be executed after each test method
        # Deleting the test CSV file after tests
        import os
        os.remove('test_data.csv')


if __name__ == '__main__':
    unittest.main()
