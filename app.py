import streamlit as st
import pandas as pd
import numpy as np
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

# Function to generate comprehensive demo data for each investment type
def generate_demo_data():
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
    return pd.DataFrame(deals)

# Function to create average price chart
def create_average_price_chart(data):
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X("Investment Type:N", title="Investment Type"),
        y=alt.Y("mean(Price):Q", title="Average Price"),
        color=alt.Color("Investment Type:N", legend=None),
        tooltip=["mean(Price)"],
    ).properties(width=800, height=400)
    return chart

# Function to create distribution chart
def create_distribution_chart(data, x_column, title):
    chart = alt.Chart(data).mark_bar().encode(
        alt.X(f"{x_column}:Q", bin=True, title=f"{title}"),
        y="count()",
        color=alt.Color("Investment Type:N", legend=None),
        tooltip=["count()"],
    ).properties(width=800, height=400)
    return chart

# Function to create heatmap
def create_heatmap(data):
    heatmap = alt.Chart(data).mark_rect().encode(
        x=alt.X("Bedrooms:O", title="Bedrooms"),
        y=alt.Y("Bathrooms:O", title="Bathrooms"),
        color=alt.Color("mean(Price):Q", scale=alt.Scale(scheme="reds")),
        tooltip=["mean(Price)"],
    ).properties(width=400, height=400)
    return heatmap

# Function to create line chart
def create_line_chart(data):
    line_chart = alt.Chart(data).mark_line().encode(
        x=alt.X("Year Built:O", title="Year Built"),
        y=alt.Y("mean(ROI (%)):Q", title="Average ROI (%)"),
        color=alt.Color("Investment Type:N", legend=None),
        tooltip=["mean(ROI (%))"],
    ).properties(width=800, height=400)
    return line_chart

# Streamlit app
def main():
    st.set_page_config(
        page_title="Real Estate Investment Deals Explorer",
        page_icon="🏡",
        layout="wide",
    )

    st.title("Real Estate Investment Deals Explorer")
    st.write(
        "Explore different types of real estate investment deals with interactive charts and details."
    )

    # Generate and display demo data
    df = generate_demo_data()

    # Sidebar with investment type selection
    selected_investment_type = st.sidebar.selectbox("Select Investment Type", investment_types)

    # Filter deals based on the selected investment type
    filtered_deals = df[df["Investment Type"] == selected_investment_type]

    # Display the selected investment type and deals
    st.sidebar.subheader(f"{selected_investment_type} Details")
    st.sidebar.dataframe(filtered_deals)

    # Show average price per investment type
    st.subheader("Average Price by Investment Type")
    st.altair_chart(create_average_price_chart(df))

    # Show distribution of property sizes
    st.subheader("Distribution of Property Sizes")
    st.altair_chart(create_distribution_chart(df, "Square Feet", "Property Size (Square Feet)"))

    # Show condition distribution
    st.subheader("Condition Distribution")
    st.altair_chart(create_distribution_chart(df, "Condition", "Property Condition"))

    # Add a map showing property locations
    st.subheader("Property Locations")
    st.map(filtered_deals, use_container_width=True)

    # Add a scatter plot for ROI vs. Price
    st.subheader("ROI vs. Price")
    scatter_chart = alt.Chart(df).mark_circle().encode(
        x=alt.X("Price:Q", title="Property Price"),
        y=alt.Y("ROI (%):Q", title="Return on Investment (%)"),
        color=alt.Color("Investment Type:N", legend=None),
        tooltip=["Deal ID", "Price", "ROI (%)", "Investment Type"],
    ).properties(width=800, height=400)
    st.altair_chart(scatter_chart)

    # Additional Charts
    st.subheader("Bedroom and Bathroom Distribution")
    st.altair_chart(create_heatmap(df))

    st.subheader("Property Condition Distribution")
    st.altair_chart(create_distribution_chart(df, "Condition", "Property Condition"))

    st.subheader("ROI Trends Over the Years")
    st.altair_chart(create_line_chart(df))

if __name__ == "__main__":
    main()

