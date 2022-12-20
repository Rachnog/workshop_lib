"""
Different covariance matrices estimators and routines
"""

import pandas as pd
import numpy as np


class CovarianceMatrixEstimator:
    """
    Estimating covariance matrices
    """

    def __init__(self, data, returns=True):
        if returns:
            self.data = data
        else:
            self.data = data.pct_change()

    def generate_cov_matrix(self, method="sample"):
        """Generates sample matrix depending on the type"""
        if method == "sample":
            return self.data.cov()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
