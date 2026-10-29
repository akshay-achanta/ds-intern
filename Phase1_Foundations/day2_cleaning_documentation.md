# Day 2 Data Cleaning Documentation

This document explains the steps taken to clean `sales-messy.csv` and generate `day2_cleaned_dataset.csv`.

## 1. Column Renaming & Standardization
- All column names were stripped of leading/trailing whitespace.
- Converted to lowercase.
- Spaces were replaced with underscores `_` to make them SQL and Pandas friendly.

## 2. Duplicate Removal
- Removed 4 exact duplicate rows to prevent double-counting revenue and metrics.

## 3. Data Type Corrections & Invalid-Value Handling
- **Unit Price**: Found string values (e.g., `Rs. 2303.18`). Stripped out the `Rs.` and commas, then converted to numeric float.
- **Order Date**: Standardized to datetime format, parsing with `dayfirst=True` to handle variations like `25/02/2023`. Invalid dates were coerced to `NaT`.
- **Negative Values**: Applied `.abs()` to `quantity` and `unit_price` to convert accidental negative entries into positive values.

## 4. Null Handling
- Replaced missing values in `customer_name`, `city`, and `salesperson` with "Unknown Customer", "Unknown City", and "Unassigned" respectively.
- Replaced missing `discount_pct` with `0.0`.
- Dropped rows where critical fields (`order_id` or `order_date`) were missing.
- Imputed remaining numeric nulls with the median of their respective columns.
- Imputed remaining object/string nulls with "Unknown".

## 5. Basic Validation
- Calculated an expected total amount: `quantity * unit_price * (1 - discount_pct/100)`.
- If the original `total_amount` was missing or zero, it was replaced with the calculated total amount to ensure data validity.
