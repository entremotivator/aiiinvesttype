import streamlit as st
import pandas as pd
import random
import altair as alt

# Sample data for different real estate investment types
investment_types = [
    "Wholesale Real Estate",
    "Fix and Flip",
    "Subject To",
    "New Construction",
    "Buy and Hold",
    "Seller Financing",
    "Lease Options",
    "Short Sales",
    "Foreclosures",
    "Tax Liens",
    "REIT Investments",
    "Land Development",
    "Commercial Real Estate",
    "Triple Net Leases",
    "Airbnb/Vacation Rentals",
    "Easement Deals",
    "Joint Ventures",
    "HUD Homes",
    "Assumption of Mortgage",
    "Wraparound Mortgage",
    "Discounted Notes",
    "Hard Money Lending",
    "Tax-Deferred Exchanges (1031 Exchange)",
    "Mobile Home Investing",
    "Mixed-Use Properties",
]

# Generate comprehensive demo data for each investment type
deals = []
for investment_type in investment_types:
    for i in range(10):
        deal = {
            "Investment Type": investment_type,
            "Deal ID": f"{investment_type[:3]}_{i+1}",
            "Price": random.randint(100000, 1000000),
            "Square Feet": random.randint(1000, 5000),
            "Bedrooms": random.randint(2, 6),
            "Bathrooms": random.randint(1, 4),
            "Location": f"City_{i+1}",
            "Year Built": random.randint(1970, 2020),
            "Condition": random.choice(["Excellent", "Good", "Fair", "Needs Renovation"]),
            "ROI (%)": round(random.uniform(5, 15), 2),
            "Additional Details": f"Details for {investment_type} deal {i+1}. Lorem ipsum...",
            # Add more details as needed
        }
        deals.append(deal)

# Create a DataFrame
df = pd.DataFrame(deals)

# Streamlit app
st.title("Real Estate Investment Deals Explorer")

# Sidebar with investment type selection
selected_investment_type = st.sidebar.selectbox("Select Investment Type", investment_types)

# Filter deals based on the selected investment type
filtered_deals = df[df["Investment Type"] == selected_investment_type]

# Display the selected investment type and deals
st.subheader(f"Deals for {selected_investment_type}")
st.dataframe(filtered_deals)

# Create a chart for average price per investment type
average_price_chart = alt.Chart(df).mark_bar().encode(
    x=alt.X("Investment Type:N", title="Investment Type"),
    y=alt.Y("mean(Price):Q", title="Average Price"),
    color=alt.Color("Investment Type:N", legend=None),
    tooltip=["mean(Price)"]
).properties(width=600, height=400)

# Display the chart
st.subheader("Average Price by Investment Type")
st.altair_chart(average_price_chart)
