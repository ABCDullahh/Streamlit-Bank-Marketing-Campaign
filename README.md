# 🏦 Bank Marketing Campaign Prediction Streamlit Dashboard

This project provides an interactive dashboard built with **Streamlit** to predict customer subscription to term deposits using **machine learning**. Leveraging **LightGBM**, this model aims to identify which bank customers are most likely to subscribe based on demographic, financial, and campaign-related features. The project supports both **single prediction** and **bulk prediction** with visualization tools for better insights and decision-making.

## 📌 Features

- **Single Prediction:** Interactive user inputs to generate predictions for individual customers.
- **Bulk Prediction:** Upload a CSV or Excel file to predict multiple customer outcomes at once.
- **Data Visualization:** Visualizations to explore feature importance, customer demographic insights, and economic indicators.
- **Customizable Interface:** Modern, user-friendly interface with intuitive controls and data inputs.
  
## 🚀 How to Use

1. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

2. **Single Prediction:**
   - Enter customer information manually via sliders and dropdowns.
   - Click on the "Generate Prediction" button to get real-time predictions.

3. **Bulk Prediction:**
   - Upload a `.csv` or `.xlsx` file with the required features (refer to "Feature Description" below).
   - Review predictions, view distribution plots, and download results.

4. **Feature Importance Analysis:**
   - Analyze which features impact customer subscription decisions the most.
   - Leverage insights for business strategies and targeted campaigns.

## 📊 Feature Descriptions

Below are the features used for prediction and their descriptions:

| Feature             | Description                                                                                       |
|---------------------|---------------------------------------------------------------------------------------------------|
| **age**             | Age of the client                                                                                 |
| **job**             | Type of job, categorized into job classes (e.g., blue-collar, white-collar, service)             |
| **marital**         | Marital status (single, married, divorced)                                                        |
| **education**       | Education level (e.g., university degree, high school, professional course)                       |
| **default**         | Whether the client has credit in default (yes, no, unknown)                                       |
| **housing**         | Whether the client has a housing loan (yes, no, unknown)                                          |
| **loan**            | Whether the client has a personal loan (yes, no, unknown)                                         |
| **contact**         | Last contact communication type (cellular, telephone)                                             |
| **month**           | Last contact month of the year (mar, apr, may, etc.)                                              |
| **day_of_week**     | Day of the last contact in the week (mon, tue, wed, thu, fri)                                     |
| **campaign**        | Number of contacts performed during this campaign                                                 |
| **previous**        | Number of contacts performed before this campaign                                                 |
| **pdays**           | Days since the client was last contacted in a previous campaign                                   |
| **poutcome**        | Outcome of the previous campaign (success, failure, nonexistent)                                  |
| **emp.var.rate**    | Employment variation rate (quarterly indicator)                                                   |
| **cons.price.idx**  | Consumer price index (monthly indicator)                                                          |
| **cons.conf.idx**   | Consumer confidence index (monthly indicator)                                                     |
| **euribor3m**       | 3-month Euribor rate                                                                              |
| **nr.employed**     | Number of employees (quarterly indicator)                                                         |


## ⚙️ Model Details

- **Model:** LightGBM Classifier
- **Performance Metric:** F2 Score
- **Version:** 1.0.0

The model has been trained on the Bank Marketing dataset to predict the likelihood of customers subscribing to a term deposit, achieving a balanced F2 score of 0.5651 on test data.

## 📚 Resources

- [Documentation](https://github.com/ABCDullahh/Purwadhika-Final-Project-Bank-Marketing-Campaign)
- [Report Issues](mailto:faizal2jz@gmail.com)

## 📅 Last Update

**Date:** `datetime.now().strftime('%Y-%m-%d')`

## 👥 Contributors

- Faizal Lutfi Yoga Triadi
- Taufiqurrahman

## 🔍 Business Insights

Based on feature importance analysis, the following strategies are recommended:
- **Targeting Strategy:** Focus on clients with higher education levels and older age groups.
- **Campaign Optimization:** Optimize contact frequency and channel selection to improve engagement.
- **Product Development:** Develop personalized offers based on client profiles and economic indicators.
