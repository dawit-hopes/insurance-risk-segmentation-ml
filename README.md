## 🚗 End-to-End Insurance Risk Analytics & Predictive Modeling

This repository, is a comprehensive data science project aimed at solving a critical business problem for **AlphaCare Insurance Solutions (ACIS)** in South Africa: **optimizing car insurance pricing and marketing by identifying low-risk client segments.**

---

## 💡 What This Project Does

The project functions as an **End-to-End Risk Analytics and Predictive Modeling pipeline** using historical car insurance claim data (Feb 2014 – Aug 2015).

Its core purpose is to transform raw policy data into **actionable business strategies** through the following sequential steps:

### 1. Risk and Profitability Analysis (EDA & Statistics)
* **Identifies key drivers of risk** by analyzing the **Loss Ratio** and performing **A/B Hypothesis Testing** on major factors like **Province**, **Zip Code**, and **Gender**.
* **Goal:** Statistically validates which demographic, geographic, or vehicle features lead to significant differences in **Claim Frequency**, **Claim Severity**, and **Profit Margin**.

### 2. Auditable Data Pipeline (DVC)
* **Ensures reproducibility** for auditing and regulatory compliance (essential in the financial sector) by implementing **Data Version Control (DVC)**.
* **Goal:** Rigorously tracks and versions the large historical dataset alongside the code, allowing any analysis or model result to be recreated precisely.

### 3. Predictive Pricing Models (Machine Learning)
* **Develops advanced machine learning models** (including **XGBoost** and **Random Forests**) to forecast the financial liability associated with an insured policy.
* **Modeling Focus:** Building a **Claim Severity Model** (predicting `TotalClaims`) that can be integrated into a formula to recommend **optimal, risk-based premium values**.

### 4. Model Interpretability
* **Provides business context** for the predictive models using techniques like **SHAP** (SHapley Additive exPlanations).
* **Goal:** Explains *why* the model makes certain predictions and identifies the **top 5-10 most influential features** (e.g., how vehicle age quantitatively impacts claim cost), enabling ACIS to confidently refine its pricing rules.

The final output is a set of **concrete, data-backed recommendations** for adjusting premiums and targeting low-risk clients to improve profitability and market share.

---

## ⚙️ Configuration

The project environment and dependencies are managed using **Conda**, ensuring a reproducible setup for all statistical and machine learning tasks.
