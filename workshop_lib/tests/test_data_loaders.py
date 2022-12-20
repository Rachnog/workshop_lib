"""
Testing data loaders
"""
import os
import unittest

from wwlib.data_loaders.data_loaders import StandardParquetDataLoader


class TestDataLoaders(unittest.TestCase):
    """
    Test data loaders
    """

    def setUp(self):
        project_path = os.path.dirname(__file__)
        path = os.path.join(project_path, "test_data")
        self.data_loader = StandardParquetDataLoader(path)
        self.data = self.data_loader.get_data()

    def test_missing_values(self):
        self.assertAlmostEqual(self.data.isnull().sum().sum(), 0)

    # def test_duplicate_rows(self):
    #     self.assertAlmostEqual(self.data.duplicated().sum(),  0)


if __name__ == "__main__":
    unittest.main()
