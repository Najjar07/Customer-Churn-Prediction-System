import streamlit as st
import pandas as pd
import joblib


# Load Model & Scaler
model_path = "churn_model.pkl"
scaler_path = "churn_scaler.pkl"
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

st.set_page_config(page_title="Customer Churn Risk System", layout="centered")

st.title("📉 Customer Churn Risk Prediction")
st.write("This system evaluates **churn risk level** using probability and recommends business actions.")

# User Inputs
st.subheader("Enter Customer Details")

years = st.number_input("Years as Customer", min_value=0.0, step=0.5)
purchases = st.number_input("Number of Purchases", min_value=0)
avg_amount = st.number_input("Average Transaction Amount", min_value=0.0)
returns = st.number_input("Number of Returns", min_value=0)
satisfaction = st.slider("Satisfaction Score (1–5)", 1, 5, 3)
days_last = st.number_input("Days Since Last Purchase", min_value=0)


# Prediction Button
if st.button("🔍 Assess Churn Risk"):

    # Create DataFrame 
    input_df = pd.DataFrame([{
        "Years_as_Customer": years,
        "Num_of_Purchases": purchases,
        "Average_Transaction_Amount": avg_amount,
        "Num_of_Returns": returns,
        "Satisfaction_Score": satisfaction,
        "Days_Since_Last_Purchase": days_last
    }])

    # Scale input
    scaled_input = scaler.transform(input_df)

    #churn probability 
    churn_index = list(model.classes_).index(1)
    prob = model.predict_proba(scaled_input)[0][churn_index]

    
    # Risk Classification
    if prob < 0.30:
        risk = "🟢 LOW CHURN RISK"
        action = "No action needed. Maintain normal engagement."

    elif prob < 0.60:
        risk = "🟡 MEDIUM CHURN RISK"
        action = "Send engagement message (email or sms), loyalty reminder, or promotion."

    else:
        risk = "🔴 HIGH CHURN RISK"
        action = "Offer discount, retention campaign, or personal follow-up."


    # Display Results
    st.subheader("📊 Churn Risk Result")
    st.markdown(f"### **{risk}**")
    st.write(f"**Churn Probability:** {prob * 100:.2f}%")
    st.write(f"**Recommended Action:** {action}")

    # Visual emphasis
    st.progress(int(prob * 100))


    # Save Prediction to CSV
    log_data = input_df.copy()
    log_data["Churn_Probability"] = prob
    log_data["Risk_Level"] = risk
    log_data["Recommended_Action"] = action

    file_name = "churn_predictions_log.csv"

    try:
        existing = pd.read_csv(file_name)
        updated = pd.concat([existing, log_data], ignore_index=True)
    except FileNotFoundError:
        updated = log_data

    updated.to_csv(file_name, index=False)

    st.success("✅ Prediction saved successfully!")


