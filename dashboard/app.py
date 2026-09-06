import streamlit as st
import pandas as pd
import plotly.express as px


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Used Car Price Analysis",
    page_icon="🚗",
    layout="wide"
)


# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv("/home/mohammed/Documents/Volunteering/GDG/Data Science 26/cleaned_car_data.csv")


# =========================================================
# TITLE
# =========================================================

st.title("🚗 Used Car Price Analysis")
st.markdown(
    "Explore used car prices, vehicle characteristics, "
    "and market patterns through interactive visualizations."
)


# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("🔎 Filters")


selected_fuel = st.sidebar.multiselect(
    "Fuel Type",
    options=sorted(df["fuel"].unique()),
    default=sorted(df["fuel"].unique())
)


selected_transmission = st.sidebar.multiselect(
    "Transmission",
    options=sorted(df["transmission"].unique()),
    default=sorted(df["transmission"].unique())
)


selected_seller = st.sidebar.multiselect(
    "Seller Type",
    options=sorted(df["seller_type"].unique()),
    default=sorted(df["seller_type"].unique())
)


selected_owner = st.sidebar.multiselect(
    "Owner Type",
    options=sorted(df["owner"].unique()),
    default=sorted(df["owner"].unique())
)


# =========================================================
# FILTER DATA
# =========================================================

filtered_df = df[
    (df["fuel"].isin(selected_fuel)) &
    (df["transmission"].isin(selected_transmission)) &
    (df["seller_type"].isin(selected_seller)) &
    (df["owner"].isin(selected_owner))
]


# =========================================================
# KPI SECTION
# =========================================================

st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Cars",
    f"{len(filtered_df):,}"
)

col2.metric(
    "Average Selling Price",
    f"{filtered_df['selling_price'].mean():,.0f}"
)

col3.metric(
    "Average Mileage",
    f"{filtered_df['km_driven'].mean():,.0f}"
)

col4.metric(
    "Average Car Age",
    f"{filtered_df['car_age'].mean():.1f} years"
)


st.divider()


# =========================================================
# PRICE ANALYSIS
# =========================================================

st.header("💰 Price Analysis")

col1, col2 = st.columns(2)


with col1:

    fig_price = px.histogram(
        filtered_df,
        x="selling_price",
        nbins=40,
        title="Selling Price Distribution"
    )

    st.plotly_chart(
        fig_price,
        use_container_width=True
    )


with col2:

    fig_age = px.scatter(
        filtered_df,
        x="car_age",
        y="selling_price",
        color="fuel",
        hover_data=["name", "year"],
        title="Selling Price vs Car Age"
    )

    st.plotly_chart(
        fig_age,
        use_container_width=True
    )


# =========================================================
# MILEAGE ANALYSIS
# =========================================================

st.header("🛣️ Mileage Analysis")

fig_mileage = px.scatter(
    filtered_df,
    x="km_driven",
    y="selling_price",
    color="transmission",
    hover_data=["name", "year"],
    title="Selling Price vs Kilometers Driven"
)

st.plotly_chart(
    fig_mileage,
    use_container_width=True
)


# =========================================================
# CATEGORY ANALYSIS
# =========================================================

st.header("⛽ Vehicle Category Analysis")

col1, col2 = st.columns(2)


with col1:

    fuel_price = (
        filtered_df
        .groupby("fuel", as_index=False)["selling_price"]
        .mean()
        .sort_values("selling_price", ascending=False)
    )

    fig_fuel = px.bar(
        fuel_price,
        x="fuel",
        y="selling_price",
        title="Average Selling Price by Fuel Type"
    )

    st.plotly_chart(
        fig_fuel,
        use_container_width=True
    )


with col2:

    fig_transmission = px.box(
        filtered_df,
        x="transmission",
        y="selling_price",
        title="Selling Price by Transmission"
    )

    st.plotly_chart(
        fig_transmission,
        use_container_width=True
    )


# =========================================================
# OWNER & SELLER ANALYSIS
# =========================================================

st.header("👤 Ownership & Seller Analysis")

col1, col2 = st.columns(2)


with col1:

    owner_price = (
        filtered_df
        .groupby("owner", as_index=False)["selling_price"]
        .mean()
        .sort_values("selling_price", ascending=False)
    )

    fig_owner = px.bar(
        owner_price,
        x="owner",
        y="selling_price",
        title="Average Selling Price by Owner Type"
    )

    st.plotly_chart(
        fig_owner,
        use_container_width=True
    )


with col2:

    seller_price = (
        filtered_df
        .groupby("seller_type", as_index=False)["selling_price"]
        .mean()
        .sort_values("selling_price", ascending=False)
    )

    fig_seller = px.bar(
        seller_price,
        x="seller_type",
        y="selling_price",
        title="Average Selling Price by Seller Type"
    )

    st.plotly_chart(
        fig_seller,
        use_container_width=True
    )


# =========================================================
# BRAND ANALYSIS
# =========================================================

st.header("🏷️ Brand Analysis")

brand_stats = (
    filtered_df
    .groupby("brand")
    .agg(
        car_count=("selling_price", "count"),
        average_price=("selling_price", "mean")
    )
    .query("car_count >= 20")
    .sort_values("average_price", ascending=False)
    .head(15)
    .reset_index()
)


fig_brand = px.bar(
    brand_stats,
    x="average_price",
    y="brand",
    orientation="h",
    title="Top Brands by Average Selling Price",
    hover_data=["car_count"]
)

st.plotly_chart(
    fig_brand,
    use_container_width=True
)


# =========================================================
# DATA PREVIEW
# =========================================================

st.header("📋 Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)