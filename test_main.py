import unittest
from unittest.mock import patch
import pandas as pd
import main  # Assuming main.py is in the same directory


class TestMainMethods(unittest.TestCase):

    def setUp(self):
        self.data = main.load_data('data.csv')

    def test_load_data(self):
        data = main.load_data('data.csv')
        self.assertTrue(isinstance(data, pd.DataFrame))
        # Check if the columns are as expected
        self.assertListEqual(list(data.columns), ['Age', 'Salary', 'Score'])

    def test_generate_summary_statistics(self):
        # Since this function just prints, we can capture print outputs and verify
        with patch("builtins.print") as mock_print:
            main.generate_summary_statistics(self.data)
            self.assertEqual(mock_print.call_count, 4)  # Ensure print was called four times

    @patch("matplotlib.pyplot.show")
    @patch("matplotlib.pyplot.ylabel")
    @patch("matplotlib.pyplot.xlabel")
    @patch("matplotlib.pyplot.title")
    @patch.object(pd.Series, "plot")
    def test_create_visualization(self, mock_plot, mock_title, mock_xlabel, mock_ylabel, mock_show):
        main.create_visualization(self.data)
        mock_plot.assert_called_once()
        mock_title.assert_called_once_with('Salary Distribution')
        mock_xlabel.assert_called_once_with('Index')
        mock_ylabel.assert_called_once_with('Salary')
        mock_show.assert_called_once()


if __name__ == '__main__':
    unittest.main()
