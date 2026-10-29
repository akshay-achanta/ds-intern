# Sales Dashboard - Final Version

## Overview
This document describes the final, polished interactive Sales Dashboard for Mini Project 1.

## Final Layout & Features

### 1. Global Filters (Left Sidebar or Top Bar)
- **Date Range Picker:** Allows dynamic filtering of all charts by `order_date`.
- **Region Dropdown:** Multi-select for filtering by specific regions.
- **Category Dropdown:** Multi-select for product categories.

### 2. High-Level KPI Scorecards (Top Row)
- **Total Revenue:** Displays total revenue with a YoY comparison indicator (green/red arrow).
- **Total Orders:** Displays order count.
- **Average Order Value (AOV):** Displays AOV.
- **Return Rate:** Displays the percentage of returned orders (returned orders / total orders).

### 3. Interactive Visualizations
- **Revenue Trend Analysis (Area Chart):** Shows cumulative or monthly revenue over time.
- **Regional Performance (Geographic Map):** Highlights regions by revenue intensity. Hover tooltips show exact revenue and order count.
- **Top 5 Products vs Bottom 5 Products (Horizontal Bar Charts):** Quickly identifies best and worst performers.
- **Revenue by Category (Donut Chart):** Shows the proportional contribution of each product category to total revenue.

### 4. Details Table (Bottom)
- A paginated table showing order-level details (`order_id`, `date`, `customer_name`, `product`, `total_amount`, `status`) for deep-dive investigation.

---
*Note: This architecture is ready to be implemented and deployed via Power BI or Looker Studio, connecting directly to the SQLite database.*
