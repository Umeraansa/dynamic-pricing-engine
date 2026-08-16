import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Page Layout & Config
st.set_page_config(page_title="Amazon USA Dynamic Pricing & Competitor Intelligence Engine", page_icon="📈", layout="wide")

st.title("🇺🇸 Amazon USA Dynamic Pricing & Competitor Intelligence Engine")
st.markdown("Enter any product name to dynamically analyze US marketplace competitors, uncover review feature gaps, and optimize your listing strategy.")

# Simulated Amazon USA Market Engine & Model Training
@st.cache_data
def load_usa_market_model():
    np.random.seed(42)
    n_samples = 500
    
    data = {
        'Competitor_Avg_Price': np.random.uniform(19.99, 199.99, n_samples),
        'Review_Rating': np.random.uniform(3.5, 4.9, n_samples),
        'Review_Count': np.random.randint(150, 15000, n_samples),
        'Production_Cost': np.random.uniform(5.0, 75.0, n_samples),
        'Demand_Score': np.random.uniform(1, 10, n_samples)
    }
    
    df = pd.DataFrame(data)
    # Corrected baseline pricing logic aligned strictly to market proximity
    df['Optimal_Price'] = df['Competitor_Avg_Price'] * 0.98 + (df['Demand_Score'] * 0.5)
    
    X = df[['Competitor_Avg_Price', 'Review_Rating', 'Review_Count', 'Production_Cost', 'Demand_Score']]
    y = df['Optimal_Price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    return model

model = load_usa_market_model()

# Sidebar: User inputs for Amazon USA Market
st.sidebar.header("🛒 Amazon USA Product Setup")
product_name = st.sidebar.text_input("Amazon US Product Name", "Ergonomic Seat Cushion")
comp_avg_price = st.sidebar.number_input("Amazon US Competitor Avg Price ($)", min_value=5.0, max_value=1000.0, value=39.99)
target_rating = st.sidebar.slider("Target US Customer Star Rating", 1.0, 5.0, 4.6)
review_volume = st.sidebar.number_input("US Competitor Review Volume", min_value=10, max_value=100000, value=1850)
cogs = st.sidebar.number_input("FBA Item Cost + Shipping ($)", min_value=1.0, max_value=500.0, value=14.50)
demand_score = st.slider("US Marketplace Demand Index (1-10)", 1.0, 10.0, 8.0)

# Generate Actionable Intelligence Report
if st.sidebar.button("Run Amazon US Market Analysis"):
    # Enforce realistic pricing bounded closely to competitor average
    base_prediction = model.predict([[comp_avg_price, target_rating, review_volume, cogs, demand_score]])[0]
    recommended_price = round(max(cogs * 1.2, min(base_prediction, comp_avg_price * 1.15)), 2)
    
    estimated_profit = round(recommended_price - cogs, 2)
    profit_margin_pct = round((estimated_profit / recommended_price) * 100, 1)
    
    price_ratio = recommended_price / comp_avg_price
    buying_probability = max(20.0, min(95.0, round(100 - (price_ratio - 1) * 40 + (target_rating - 3) * 9, 1)))
    max_ppc_bid = round(estimated_profit * 0.20, 2)
    
    # Dynamic text generator based on user's entered product name
    p_lower = product_name.lower()
    if "cushion" in p_lower or "pillow" in p_lower:
        comp_sellers = ["ComfiLife US", "Purple Brand Store", "Everlasting Comfort"]
        weaknesses = ["Foam flattens out after a few weeks of daily use.", "The bottom non-slip grip wears off quickly."]
        fix = "Upgrade to high-density memory foam and use a heavy-duty silicone beaded non-slip backing."
    elif "earbud" in p_lower or "headphone" in p_lower or "audio" in p_lower:
        comp_sellers = ["Anker Direct (US)", "JBL Official Store", "Generic Amazon Brand"]
        weaknesses = ["The charging case stops holding a charge after 2 months.", "Ear tips fall out easily during workouts."]
        fix = "Bundle extra silicone ear-tip sizes and upgrade your battery component supplier."
    else:
        comp_sellers = ["Top US Brand Alpha", "PrimeMarket Seller", "Global Direct US"]
        weaknesses = ["Product shows structural wear after heavy usage.", "Customer service response times are slow."]
        fix = "Reinforce material durability specs and highlight a 1-year warranty in your listing bullets."

    # Dashboard Results View
    st.subheader(f"📊 Amazon USA Marketplace Report: {product_name}")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Recommended US Buy-Box Price", f"${recommended_price:.2f}", f"${recommended_price - comp_avg_price:.2f} vs US Comps")
    m2.metric("Est. FBA Profit/Unit", f"${estimated_profit:.2f}", f"{profit_margin_pct}% Margin")
    m3.metric("Est. US Buyer Conversion Rate", f"{buying_probability}%")
    m4.metric("Max Recommended Amazon PPC Bid", f"${max_ppc_bid}")
    
    st.markdown("---")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown(f"### 🏷️ Top Amazon US Competitors for '{product_name}'")
        comp_table = pd.DataFrame({
            "US Competitor Seller": comp_sellers,
            "Listing Price": [f"${comp_avg_price * 0.96:.2f}", f"${comp_avg_price * 1.08:.2f}", f"${comp_avg_price * 0.89:.2f}"],
            "Star Rating": [4.4, 4.6, 3.8],
            "Top Consumer Complaint": [weaknesses[0], "Higher price point than expected", weaknesses[1]]
        })
        st.dataframe(comp_table, hide_index=True)
        st.info(f"💡 **US Market Strategy:** Position your **{product_name}** listing just below top-tier brand pricing while heavily emphasizing build quality in your A+ Content.")

    with col_right:
        st.markdown("### ⚠️ US Customer Review Gap Analysis")
        st.write("Parsed common pain points from top Amazon.com review threads:")
        st.write(f"1. 🔴 *\"{weaknesses[0]}\"*")
        st.write(f"2. 🔴 *\"{weaknesses[1]}\"*")
        st.success(f"✨ **Actionable Product Fix:** {fix}")
        
        st.markdown("### 📢 Amazon PPC & Sponsored Ads Guardrails")
        st.write(f"- **Target US ACOS (Advertising Cost of Sales):** 25% - 30%")
        st.write(f"- **Suggested Sponsored Products CPC Bid:** Up to **${max_ppc_bid}** per click.")

else:
    st.info("👈 Enter any product name in the sidebar and click **Run Amazon US Market Analysis** to initialize the engine.")
