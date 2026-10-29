# Mini Project 1 Data Cleaning Decisions

This document outlines the decisions made when transforming the messy sales dataset into `cleaned_sales.csv`.

1.  **Column Names:** All columns were converted to lowercase with spaces replaced by underscores for standard SQL and Pandas accessibility.
2.  **Duplicates:** Exact duplicate rows were dropped.
3.  **Data Types:** `unit_price` contained string artifacts like 'Rs.' which were stripped out before converting to float. `order_date` was properly parsed as datetime.
4.  **Negative Values:** Any negative `quantity` or `unit_price` was converted to its absolute value assuming data entry errors.
5.  **Category Inconsistencies:** Categories like 'clothings' and 'clothing' were standardized to 'Clothing'.
6.  **Null Values:** 
    *   Missing categorical values like `customer_name` and `city` were replaced with 'Unknown...'. 
    *   Missing `discount_pct` was assumed to be `0.0`.
    *   Rows missing critical identifiers (`order_id`, `order_date`) were dropped.
    *   Remaining numeric nulls were imputed with the column median.
7.  **Data Validation:** `total_amount` was recalculated where missing or invalid (<=0) based on `quantity`, `unit_price`, and `discount_pct`.
8.  **Returns:** Orders with `status` == 'Returned' are kept in the dataset. Analytics queries will filter these out or analyze them specifically based on the business question.
