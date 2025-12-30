import streamlit as st
import joblib
import pandas as pd
import numpy as np

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Deal Intelligence System",
    page_icon="⚖️",
    layout="centered"
)

# -------------------------------------------------
# LOAD MODEL (CACHED)
# -------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load("final_lasso_model.joblib")

model = load_model()

# -------------------------------------------------
# TITLE & INTRO
# -------------------------------------------------
st.title("⚖️ Price Fairness & Deal Intelligence System")
st.markdown(
    """
    Enter the **brand** and **current listed price** to check:
    - Price fairness  
    - Deal alert  
    - Re-sell (flip) potential  
    - Smart pricing suggestions  

    *The system uses an ML model internally. Predicted prices are not shown to avoid bias.*
    """
)

st.divider()

# -------------------------------------------------
# TRAINED BRANDS (SAFE LIST)
# -------------------------------------------------
BRANDS = [
    "Essence",
    "Glamour Beauty",
    "Velvet Touch",
    "Chic Cosmetics",
    "Nail Couture"
]

# -------------------------------------------------
# USER INPUTS (ONLY WHAT USER KNOWS)
# -------------------------------------------------
st.subheader("🧾 Enter Listing Details")

brand = st.selectbox("Brand", BRANDS)

listed_price = st.number_input(
    "Listed Price (₹)",
    min_value=1.0,
    step=10.0,
    value=1000.0
)

# -------------------------------------------------
# BUTTON ACTION
# -------------------------------------------------
if st.button("🔍 Check Price Fairness"):

    # ---------------------------------------------
    # INTERNAL FEATURE CONSTRUCTION (HIDDEN)
    # ---------------------------------------------
    brand_features = {f"brand_{b}": 0 for b in BRANDS}
    brand_features[f"brand_{brand}"] = 1

    model_input = pd.DataFrame([brand_features])

    # Align with model feature order
    for col in model.feature_names_in_:
        if col not in model_input.columns:
            model_input[col] = 0

    model_input = model_input[model.feature_names_in_]

    # ---------------------------------------------
    # MODEL PREDICTION (HIDDEN)
    # ---------------------------------------------
    predicted_price = model.predict(model_input)[0]

    price_gap = listed_price - predicted_price
    gap_percent = (price_gap / predicted_price) * 100

    # ---------------------------------------------
    # PRICE FAIRNESS OUTPUT
    # ---------------------------------------------
    st.divider()
    st.subheader("📊 Price Fairness Result")

    if gap_percent <= -15:
        st.success("🟢 UNDERPRICED! GO GRAB IT NOW!!")
        st.caption("The listed price is significantly below expected market value.")
    elif -15 < gap_percent < 15:
        st.info("🔵 FAIRLY PRICED")
        st.caption("The listed price is close to the expected market value.")
    else:
        st.error("🔴 OVERPRICED")
        st.caption("The listed price is higher than expected for similar items.")

    # ---------------------------------------------
    # SMART INSIGHTS (ADDITIONAL FEATURES)
    # ---------------------------------------------
    st.divider()
    st.subheader("💡 Smart Insights")

    # 🚨 DEAL ALERT
    if gap_percent <= -20:
        st.success("🔥 STEAL DEAL ALERT")
        st.caption("This item is well below market expectations.")
    elif -20 < gap_percent <= -10:
        st.info("✅ Good Deal")
    else:
        st.warning("❌ Not a Deal")

    # 📉 PRICE DROP SUGGESTION (ONLY IF OVERPRICED)
    if gap_percent > 15:
        drop_low = int(listed_price * 0.85)
        drop_high = int(listed_price * 0.90)

        st.error("📉 Price Drop Suggested")
        st.caption(
            f"Reducing the price to around ₹{drop_low} – ₹{drop_high} "
            "may help sell the item faster."
        )

    # 💸 RE-SELL / FLIP PROFIT ESTIMATION
    platform_fee = 0.10 * predicted_price
    estimated_profit = predicted_price - listed_price - platform_fee

    if estimated_profit > 0:
        st.success("💸 Flip Opportunity Detected")
        st.caption(
            f"Estimated resale profit could be approximately "
            f"₹{int(estimated_profit * 0.8)} – ₹{int(estimated_profit * 1.2)} "
            "after platform fees."
        )
    else:
        st.info("ℹ️ Limited resale profit potential at this price.")

    # 🔐 CONFIDENCE INDICATOR
    st.divider()
    if 700 <= predicted_price <= 2600:
        st.success("🔐 High Confidence Assessment")
    else:
        st.warning("⚠️ Medium / Low Confidence (Limited comparable data)")

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.divider()
st.caption(
    "ML-based Deal Intelligence System | "
    "Predicted prices are used internally and not displayed to users."
)
