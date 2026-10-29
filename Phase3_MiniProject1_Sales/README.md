# Mini Project 1: Sales Analytics & Business Intelligence

## Business Problem
The executive team lacks visibility into overall sales performance. They need a comprehensive, interactive dashboard and underlying analytics infrastructure to understand revenue trends, customer behavior, and product performance in order to make data-driven decisions on marketing spend and inventory management.

## Dataset
The dataset contains transactional sales data, including order details, customer information, product categories, quantities, unit prices, discounts, and order statuses (e.g., Delivered, Returned). The data covers multiple regions and payment methods.

## Scope
This project focuses on building an end-to-end data pipeline to ingest, clean, and analyze the sales data. The final output is an interactive BI dashboard that answers key business questions.

## Business Questions
- What is total revenue?
- What are the monthly sales trends?
- Which products perform best?
- Which customers generate the most revenue?
- Which regions perform best?
- What is the average order value (AOV)?
- How are returns affecting revenue?
- What is the YoY and Month-over-Month growth?

## KPIs
1. **Total Revenue:** Sum of all delivered and non-returned total amounts.
2. **Total Orders:** Count of unique delivered orders.
3. **Average Order Value (AOV):** Total Revenue / Total Orders.
4. **Return Rate:** Percentage of orders marked as 'Returned'.

## Expected Outputs
- A SQLite database containing raw and cleaned sales data.
- SQL queries addressing the business questions.
- An interactive dashboard (Streamlit/Power BI) visualizing the KPIs and trends.
- A final presentation deck summarizing the insights.

## Technology Stack
- **Languages:** Python, SQL
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Streamlit, Plotly
- **Database:** SQLite
- **Tools:** Jupyter Notebooks, GitHub
