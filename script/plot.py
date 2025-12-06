import seaborn as sns
import matplotlib.pyplot as plt

class Plot:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_box_plot(self, col_name:str):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=self.df[col_name])
        plt.title(f"Box Plot of {col_name}")
        plt.show()