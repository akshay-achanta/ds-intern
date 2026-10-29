# BI Tool Sample Report

## Overview
This report simulates a dashboard built in Looker Studio or Power BI.

## Page 1: Executive Summary
- **KPIs:** Total Revenue ($1.2M), Total Orders (5,000), AOV ($240)
- **Primary Chart:** Area chart showing monthly revenue trend.
- **Filters:** Date range selector set to 'Year to Date'.

## Page 2: Product Performance
- **Matrix Table:** Product Name, Category, Units Sold, Revenue, Profit Margin.
- **Calculated Field:** `Profit Margin = (Revenue - COGS) / Revenue`
- **Interactive Element:** Cross-filtering (clicking a category on the pie chart filters the matrix table).
