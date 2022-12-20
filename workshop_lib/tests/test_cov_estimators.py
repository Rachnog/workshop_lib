"""
Testing cov matrices
"""
import os
import unittest

from workshop_lib.data_loaders.data_loaders import StandardParquetDataLoader
from workshop_lib.cov_estimators.cov_estimators import CovarianceMatrixEstimator


class TestCovMatrixEstimators(unittest.TestCase):
    """
    Test cov matrix estimators
    """

    def setUp(self):
        project_path = os.path.dirname(__file__)
        path = os.path.join(project_path, "test_data")
        self.data_loader = StandardParquetDataLoader(path)
        self.data = self.data_loader.get_data()
        self.cov_estimator = CovarianceMatrixEstimator(self.data)
        self.cov_matrix_sample = self.cov_estimator.generate_cov_matrix()

    def test_covariance_matrix_shape(self):
        self.assertAlmostEqual(
            self.cov_matrix_sample.shape[0], self.cov_matrix_sample.shape[1]
        )
