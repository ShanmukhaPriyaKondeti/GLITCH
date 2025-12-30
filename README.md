## 🚀 GLITCH – ML-Based Price Fairness & Deal Intelligence System
📌 Problem Statement

Resale and online marketplaces lack a reliable system to evaluate whether a listed product price is fair, underpriced, or overpriced. Users often rely on intuition without understanding true market value, resale potential, or deal quality.

GLITCH addresses this gap by using machine learning to analyze historical data and provide price fairness decisions and deal intelligence, without exposing raw predicted prices to users.

🎯 Project Objective

The goal of this project is to:

Evaluate price fairness of a product listing

Identify genuine deals (Deal Alerts)

Provide price drop suggestions

Estimate resale (flip) profit potential

Maintain transparency and reproducibility using ML

🧠 Solution Overview

The system uses a trained regression model (LassoCV) to internally estimate the fair market value of a product.
Instead of displaying the predicted price directly, the application converts the prediction into actionable insights such as:

UNDERPRICED / FAIR / OVERPRICED

Deal Alert (Steal / Good Deal / Not a Deal)

Price Drop Recommendation

Estimated Resale Profit Range

Confidence Indicator

🗂️ Dataset Description

The project uses a real dataset collected via an online API, stored as CSV files.

Key Features:

brand

category

price

rating

(engineered features for modeling)

Data Handling:

Numerical missing values handled using mean imputation

Categorical variables encoded using One-Hot Encoding

Data prepared and saved as clean CSV files for reproducibility

⚙️ Machine Learning Approach

Problem Type: Regression

Target Variable: Price

Model Used: Lasso Regression with Cross-Validation (LassoCV)

Why LassoCV?

Handles multicollinearity well

Performs implicit feature selection

Prevents overfitting on small datasets

Provides stable and interpretable results

Evaluation Metric:

RMSE (Root Mean Squared Error)

Multiple models were tested (Linear, Ridge, Lasso, Tree-based), and LassoCV was selected based on performance and stability.

🧩 Feature Engineering & Logic

Additional intelligence layers were built on top of the ML model:

🚨 Deal Alert System

Triggers alerts when the listed price is significantly lower than the internal market estimate.

📉 Price Drop Suggestion

Recommends an optimal price range for faster selling if the item is overpriced.

💸 Resale (Flip) Profit Estimation

Estimates potential profit after considering platform fees.

🔐 Confidence Indicator

Confidence is based on whether the prediction lies within stable training ranges.

🖥️ Application Interface (Streamlit)

The project is deployed as a Streamlit web application.

User Inputs:

Brand

Listed Price

User Outputs:

Price Fairness Classification

Deal Alert

Price Drop Suggestion

Resale Profit Insight

Confidence Indicator

🔒 The predicted market price is not shown to users to avoid bias.

🧪 Reproducibility & Environment

Python: 3.13.1

scikit-learn: 1.8.0

joblib: 1.5.3

All dependencies are listed in requirements.txt.
The trained model is saved using joblib for reuse.


<img width="736" height="408" alt="image" src="https://github.com/user-attachments/assets/7dc3938e-9c2c-430a-a6cc-6d778c36d276" />


▶️ How to Run the Project
pip install -r requirements.txt
streamlit run app.py

🏁 Conclusion

GLITCH demonstrates how machine learning can be used not just for prediction, but for decision-making and deal intelligence.
By combining ML with explainable business logic, the system helps users make smarter pricing and purchasing decisions in resale markets.

👤 Author
Shanmukha Priya Kondeti
