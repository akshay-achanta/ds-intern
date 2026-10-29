import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import os

st.set_page_config(page_title="Operations & Logistics Dashboard", layout="wide")

st.title("Supply Chain & Logistics Operations Dashboard")
st.markdown("Monitor carrier performance, fulfillment delays, and warehouse logistics efficiency in real-time.")

@st.cache_data
def load_operations_data():
    db_paths = [
        "Data/Databases/operations.db",
        "../Data/Databases/operations.db",
        "../../Data/Databases/operations.db"
    ]
    db_path = next((p for p in db_paths if os.path.exists(p)), "Data/Databases/operations.db")
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM shipments", conn)
    conn.close()
    return df

try:
    df = load_operations_data()

    # Sidebar Filters
    st.sidebar.header("Filter Criteria")
    warehouses = st.sidebar.multiselect("Select Warehouse(s)", options=df['warehouse'].unique(), default=df['warehouse'].unique())
    carriers = st.sidebar.multiselect("Select Carrier(s)", options=df['carrier'].unique(), default=df['carrier'].unique())

    filtered_df = df[(df['warehouse'].isin(warehouses)) & (df['carrier'].isin(carriers))]

    # Metric Scorecards
    col1, col2, col3, col4 = st.columns(4)
    total_shipments = len(filtered_df)
    on_time_pct = (filtered_df['status'] == 'On Time').mean() * 100 if total_shipments > 0 else 0
    avg_actual_days = filtered_df['actual_days'].mean() if total_shipments > 0 else 0
    avg_cost = filtered_df['shipping_cost'].mean() if total_shipments > 0 else 0

    col1.metric("Total Shipments", f"{total_shipments:,}")
    col2.metric("On-Time Rate", f"{on_time_pct:.1f}%", delta=f"{on_time_pct - 80:.1f}% vs 80% SLA")
    col3.metric("Avg Transit Time", f"{avg_actual_days:.1f} Days")
    col4.metric("Avg Cost per Order", f"${avg_cost:.2f}")

    st.markdown("---")

    # Visualizations
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.subheader("On-Time Rate by Carrier")
        carrier_perf = filtered_df.groupby('carrier').agg(
            on_time_rate=('status', lambda s: (s == 'On Time').mean() * 100)
        ).reset_index()
        fig_carrier = px.bar(
            carrier_perf, x='carrier', y='on_time_rate',
            labels={'on_time_rate': 'On-Time Rate (%)', 'carrier': 'Carrier'},
            color='on_time_rate', color_continuous_scale='Blues'
        )
        st.plotly_chart(fig_carrier, use_container_width=True)

    with chart_col2:
        st.subheader("Average Delivery Delay by Warehouse")
        wh_delay = filtered_df.groupby('warehouse')['delay_days'].mean().reset_index()
        fig_wh = px.bar(
            wh_delay, x='warehouse', y='delay_days',
            labels={'delay_days': 'Average Delay (Days)', 'warehouse': 'Warehouse Origin'},
            color='delay_days', color_continuous_scale='Reds'
        )
        st.plotly_chart(fig_wh, use_container_width=True)

    # Detailed Dispatch Log Table
    st.markdown("---")
    st.subheader("Shipment Dispatch Records")
    st.dataframe(filtered_df[['shipment_id', 'warehouse', 'carrier', 'shipping_cost', 'estimated_days', 'actual_days', 'delay_days', 'status']], use_container_width=True)

except Exception as e:
    st.error(f"Error loading operations data: {e}")
