import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class Plot:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_box_plot(self, col_name: str, show_points=True, log_scale=False):
        """
        Plot a clean boxplot with optional data points overlay and log scale.

        Args:
            col_name (str): Column to plot.
            show_points (bool): Overlay individual data points on boxplot.
            log_scale (bool): Use log scale for skewed distributions.
        """
        plt.figure(figsize=(10, 6))
        
        if show_points:
            sns.boxplot(x=self.df[col_name], showfliers=True)
            sns.stripplot(x=self.df[col_name], color='red', alpha=0.3, jitter=0.2)
        else:
            sns.boxplot(x=self.df[col_name], showfliers=True)
        
        if log_scale:
            plt.xscale('log')
        
        plt.title(f"Box Plot of {col_name}", fontsize=14)
        plt.xlabel(col_name, fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.6)
        plt.show()

    def plot_line_plot(self, series: pd.Series):
        """
        Plot a clean line plot.

        Args:
            series (pd.Series): Series to plot.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(series)
        plt.title(f"Line Plot of {series.name}", fontsize=14)
        plt.xlabel(series.name, fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.6)
        plt.show()


    def plot_bar_analysis(self, df_analysis: pd.DataFrame, title_col: str):
        """
        Plot a clean bar plot.

        Args:
            df_analysis (pd.DataFrame): DataFrame to plot.
            title_col (str): Column to use as title.
        """
        plt.figure(figsize=(10, 6))
        sns.barplot(x=df_analysis.index, y=df_analysis['Loss Ratio (%)'])
        
        plt.title(f"Loss Ratio by {title_col}", fontsize=14)
        plt.xlabel(title_col, fontsize=12)
        plt.ylabel('Loss Ratio (%)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.show()

    def plot_histo_gram(self, col_name: str, log_scale=False):
        """
        Plot a clean histogram with optional log scale.

        Args:
            col_name (str): Column to plot.
            log_scale (bool): Use log scale for skewed distributions.
        """
        plt.figure(figsize=(10, 6))
        
        if log_scale:
            plt.xscale('log')
        
        sns.histplot(self.df[col_name], kde=True)
        plt.title(f"Histogram of {col_name}", fontsize=14)
        plt.xlabel(col_name, fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.6)
        plt.show()
