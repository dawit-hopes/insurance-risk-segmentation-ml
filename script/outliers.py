import pandas as pd

class Outliers:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def remove_outliers(self, col_name: str, threshold: float = 1.5):
        iqr = self.df[col_name].quantile(0.75) - self.df[col_name].quantile(0.25)
        lower_bound = self.df[col_name].quantile(0.25) - (iqr * threshold)
        upper_bound = self.df[col_name].quantile(0.75) + (iqr * threshold)

        self.df[col_name] = self.df[col_name].clip(lower=lower_bound, upper=upper_bound)
        return self.df