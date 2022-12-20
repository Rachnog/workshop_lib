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
        """Generates sample matrix depending on the type
        >>> import pandas as pd
        >>> data = pd.DataFrame().from_dict({'A': [1,2,3,4,5], 'B': [5,4,3,2,1]})
        >>> cov_estimator = CovarianceMatrixEstimator(data, returns=False)
        >>> cov_matrix = cov_estimator.generate_cov_matrix()
        >>> cov_matrix['A']['B']
        0.0357638888888889
        """
        if method == "sample":
            return self.data.cov()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
