import pandas as pd


class EDA:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def LR_analysis(self, col_name: str):
        new_df = self.df.groupby(col_name)

        total_claim = new_df['TotalClaims'].sum()
        total_premim = new_df['TotalPremium'].sum()
        overall_loss_ratio = (total_claim / total_premim) * 100

        analysis = pd.DataFrame({
            'Total Claims': total_claim,
            'Total Premium': total_premim,
            'Loss Ratio (%)': overall_loss_ratio
        })

        analysis = analysis.sort_values(by='Loss Ratio (%)', ascending=False)

        print(f"{col_name} overall Loss Ratio (TotalClaims / TotalPremium)")
        print("\n")
        print(analysis)
