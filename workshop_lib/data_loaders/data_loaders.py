"""
Data loader class
"""

import os
import pandas as pd


class StandardParquetDataLoader:
    """
    Loading parquet data in a standard format and preparing it for work
    """

    def __init__(self, path, file="mktDataTest.parquet"):
        # Load the market data close prices
        self.hist_market_data = pd.read_parquet(os.path.join(path, file))

    def get_data(self, pivot=True):
        if pivot:
            return self.hist_market_data.reset_index().pivot(
                index="Date", columns="ticker", values="fg_price"
            )
        else:
            return self.hist_market_data
