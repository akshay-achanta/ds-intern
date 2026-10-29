# Sales Dashboard - Draft Version

## Overview
This document serves as the structural plan and draft layout for the Mini Project 1 Sales Dashboard, to be built in a BI tool (Looker Studio / Power BI).

## Data Source
- **Database:** SQLite (`sales.db`)
- **Table:** `sales_data` (cleaned data)

## Draft Layout

### Top Section (KPIs)
- **Total Revenue:** [Sum of total_amount where status = Delivered]
- **Total Orders:** [Count of order_id]
- **Average Order Value:** [Revenue / Orders]

### Middle Section (Core Charts)
1. **Monthly Revenue Trend (Line Chart)**
   - X-Axis: order_date (Month-Year)
   - Y-Axis: total_amount

2. **Revenue by Region (Bar Chart or Map)**
   - Category: region
   - Metric: total_amount

3. **Top 5 Categories (Bar Chart)**
   - Category: category
   - Metric: total_amount

### Bottom Section (Filters)
- Date Range Filter
- Region Filter
- Category Filter
