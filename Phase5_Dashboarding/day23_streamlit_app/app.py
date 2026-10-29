import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Interactive Sales Dashboard")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('../../Data/Processed/cleaned_sales.csv')
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df

try:
    df = load_data()
    
    # Sidebar Filters
    st.sidebar.header("Filters")
    regions = st.sidebar.multiselect("Select Region", options=df['region'].unique(), default=df['region'].unique())
    
    filtered_df = df[df['region'].isin(regions)]
    
    # KPIs
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric(label="Total Revenue", value=f"${filtered_df['total_amount'].sum():,.2f}")
    kpi2.metric(label="Total Orders", value=f"{len(filtered_df):,}")
    kpi3.metric(label="Average Order Value", value=f"${filtered_df['total_amount'].mean():,.2f}")
    
    # Charts
    st.markdown("### Revenue by Category")
    cat_df = filtered_df.groupby('category')['total_amount'].sum().reset_index()
    fig1 = px.bar(cat_df, x='category', y='total_amount', color='category')
    st.plotly_chart(fig1, use_container_width=True)
    
except Exception as e:
    st.error(f"Error loading data: {e}")
