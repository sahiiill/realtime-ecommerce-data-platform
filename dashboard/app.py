import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Real-Time E-Commerce Analytics",
    layout="wide"
)

st.title("Real-Time E-Commerce Analytics Dashboard")


PROCESSED_FILE = Path(
    "storage/processed/processed_events.jsonl"
)


@st.cache_data
def load_data():

    records = []

    if not PROCESSED_FILE.exists():
        return pd.DataFrame()

    with open(PROCESSED_FILE, "r", encoding="utf-8") as file:

        for line in file:
            records.append(json.loads(line))

    return pd.DataFrame(records)


df = load_data()


if df.empty:

    st.warning("No processed data found.")
    st.stop()


# =========================
# KPIs
# =========================

total_events = len(df)

total_revenue = round(df["total_price"].sum(), 2)

purchase_count = len(
    df[df["event_type"] == "purchase"]
)

avg_order_value = round(
    df["total_price"].mean(),
    2
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Events", total_events)

col2.metric("Total Revenue", f"€{total_revenue}")

col3.metric("Purchases", purchase_count)

col4.metric("Average Order Value", f"€{avg_order_value}")


st.divider()


# =========================
# Revenue by Product
# =========================

revenue_by_product = (
    df.groupby("product_name")["total_price"]
    .sum()
    .reset_index()
)

fig_products = px.bar(
    revenue_by_product,
    x="product_name",
    y="total_price",
    title="Revenue by Product"
)

st.plotly_chart(
    fig_products,
    use_container_width=True
)


# =========================
# Events by Device
# =========================

device_counts = (
    df["device_type"]
    .value_counts()
    .reset_index()
)

device_counts.columns = [
    "device_type",
    "count"
]

fig_devices = px.pie(
    device_counts,
    names="device_type",
    values="count",
    title="Events by Device Type"
)

st.plotly_chart(
    fig_devices,
    use_container_width=True
)


# =========================
# Top Countries
# =========================

country_revenue = (
    df.groupby("user_country")["total_price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_countries = px.bar(
    country_revenue,
    x="user_country",
    y="total_price",
    title="Top Countries by Revenue"
)

st.plotly_chart(
    fig_countries,
    use_container_width=True
)