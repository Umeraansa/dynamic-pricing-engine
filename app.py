"US Competitor Seller": ["Anker Direct (US)", "JBL Official Store", "Generic Amazon Brand"],
            "Listing Price": [f"${comp_avg_price * 0.96:.2f}", f"${comp_avg_price * 1.08:.2f}", f"${comp_avg_price * 0.89:.2f}"],
            "Star Rating": [4.4, 4.6, 3.8],
            "Top Consumer Complaint": ["Case hinge feels weak", "High price point", "Short Bluetooth range"]
        })
        st.dataframe(comp_table, hide_index=True)
        st.info("💡 US Market Strategy: Position your listing just below top-tier brand pricing while heavily emphasizing build durability in your A+ Content to capture dissatisfied competitor traffic.")

    with col_right:
        st.markdown("### ⚠️ US Customer Review Gap Analysis")
        st.write("Parsed common pain points from top Amazon.com review threads:")
        st.write("1. 🔴 *\"The charging case stops holding a charge after 2 months of use.\"*")
        st.write("2. 🔴 *\"Ear tips fall out easily during workouts or running.\"*")
        st.success("✨ Actionable Product Fix: Bundle extra silicone ear-tip sizes and upgrade your battery component supplier to explicitly answer these US customer reviews.")
        
        st.markdown("### 📢 Amazon PPC & Sponsored Ads Guardrails")
        st.write(f"- Target US ACOS (Advertising Cost of Sales): 25% - 30%")
        st.write(f"- Suggested Sponsored Products CPC Bid: Up to ${max_ppc_bid} per click.")

else:
    st.info("👈 Enter your Amazon USA product details in the sidebar and click Run Amazon US Market Analysis to initialize the engine.")
