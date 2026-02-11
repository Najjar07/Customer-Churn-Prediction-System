# 📉 Customer Churn Risk Prediction System

## 📌 Overview

The **Customer Churn Risk Prediction System** is a Machine Learning web application built with **Python** and **Streamlit** that predicts the likelihood of a customer leaving a business (churn). The system evaluates customer behavior data, calculates churn probability, classifies risk level, and recommends appropriate business actions for customer retention.

This project demonstrates how Machine Learning can support business decision-making by identifying at-risk customers early and enabling proactive engagement strategies.

---

## 🚀 Features

* ✅ Customer churn probability prediction
* ✅ Risk classification (Low, Medium, High)
* ✅ Business action recommendations
* ✅ Real-time prediction using Streamlit
* ✅ Data scaling using trained scaler
* ✅ Automatic logging of predictions to CSV
* ✅ Interactive probability visualization

---

## 🧠 Machine Learning Workflow

The system follows a standard ML pipeline:

1. User inputs customer behavioral data
2. Input data is converted into a structured format
3. Features are scaled using a trained scaler
4. Machine Learning model predicts churn probability
5. Risk level is determined based on probability thresholds
6. Recommended business action is displayed
7. Prediction is saved for future analysis

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Streamlit

---

## 📂 Project Structure

```
customer-churn-risk-system/
│
├── app.py
├── churn_model.pkl
├── churn_scaler.pkl
├── churn_predictions_log.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/customer-churn-risk-system.git
cd customer-churn-risk-system
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the Streamlit app using:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📊 Input Features

The model evaluates churn risk using the following inputs:

* Years as Customer
* Number of Purchases
* Average Transaction Amount
* Number of Returns
* Satisfaction Score (1–5)
* Days Since Last Purchase

---

## 📈 Output

The system provides:

* Churn Probability (%)
* Risk Level Classification
* Recommended Business Action
* Visual Probability Indicator

All predictions are automatically saved in:

```
churn_predictions_log.csv
```

---

## 📈 Future Improvements

* Model performance dashboard
* Feature importance visualization
* API deployment
* Cloud deployment (Streamlit Cloud / AWS / Render)
* Real-time customer database integration

---

## 👨‍💻 Author

**Najari Umar Jibril**
Machine Learning Engineer
Focused on building practical AI solutions for business and real-world applications.

---

## 📜 License

This project is open-source and available under the MIT License.

