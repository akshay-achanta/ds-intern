# Enterprise Data Dictionary

## 1. Overview
This document provides a comprehensive data dictionary for all transactional datasets, clean tables, and analytical views across **Mini Project 1 (Sales & Commercial Analytics)** and **Mini Project 2 (Operations & Supply Chain Logistics)**.

---

## 2. Mini Project 1: Sales Domain (`sales.db` & `cleaned_sales.csv`)

### Table: `sales_data` / File: `cleaned_sales.csv`
Contains granular customer transactional order records for retail and commercial sales.

| Column Name | Data Type | Nullable | Primary Key | Description | Example Values | Validation / Business Rules |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| `order_id` | `VARCHAR(50)` | No | Yes | Unique identifier for each customer transaction. | `ORD-10024`, `ORD-10025` | Must match regex `ORD-\d+`. Deduplicated during ETL. |
| `order_date` | `DATE` | No | No | Date on which the customer placed the order. | `2024-03-15` | ISO 8601 format (`YYYY-MM-DD`). |
| `customer_name`| `VARCHAR(100)`| No | No | Full name of the purchasing customer. | `John Doe`, `Alice Smith` | Nulls coalesced to `'Unknown Customer'` during cleaning. |
| `city` | `VARCHAR(100)`| No | No | City of delivery / customer residence. | `Austin`, `Seattle`, `New York` | Cleaned of leading/trailing whitespaces. |
| `region` | `VARCHAR(50)` | No | No | Geographical sales region for territory analysis. | `North`, `South`, `East`, `West` | Restricted to 4 standard operating territories. |
| `salesperson` | `VARCHAR(100)`| Yes | No | Internal sales representative handling the deal. | `Sarah Jenkins`, `Michael Scott` | Optional for online self-serve orders. |
| `category` | `VARCHAR(50)` | No | No | Broad classification of the purchased item. | `Electronics`, `Furniture`, `Apparel`| High-level taxonomy grouping. |
| `product` | `VARCHAR(150)`| No | No | Specific item description / SKU name. | `Wireless Mouse`, `Standing Desk` | Cleaned and standardized names. |
| `quantity` | `INTEGER` | No | No | Number of units purchased in the order line. | `1`, `4`, `10` | Must be strictly positive integer (`> 0`). |
| `unit_price` | `NUMERIC(10,2)`| No | No | Base selling price per unit before discounts ($). | `49.99`, `299.00` | Floating-point currency value (`>= 0.00`). |
| `discount_pct`| `NUMERIC(4,2)` | No | No | Percentage discount applied at checkout (0.00-1.00).| `0.00`, `0.10`, `0.25` | Bounded between 0.00 and 0.50 (max 50% discount). |
| `total_amount`| `NUMERIC(10,2)`| No | No | Net billed amount: `quantity * unit_price * (1 - discount_pct)`.| `44.99`, `538.20` | Computed net revenue. |
| `payment_mode`| `VARCHAR(50)` | No | No | Customer payment instrument used. | `Credit Card`, `UPI`, `Net Banking` | Standardized category labels. |
| `status` | `VARCHAR(30)` | No | No | Fulfillment lifecycle status of the transaction. | `Delivered`, `Returned`, `Cancelled`| Revenue analytics filtered where `status = 'Delivered'`. |
| `etl_timestamp`| `TIMESTAMP` | No | No | System timestamp when record was transformed and loaded.| `2026-08-20 21:28:50` | Automatically injected during automated ETL pipeline. |

---

## 3. Mini Project 2: Operations Domain (`operations.db` & `raw_operations.csv`)

### Table: `shipments`
Contains fulfillment, carrier transit, and logistics dispatch records across national warehouses.

| Column Name | Data Type | Nullable | Primary Key | Description | Example Values | Validation / Business Rules |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| `shipment_id` | `INTEGER` | No | Yes | Sequential identifier for dispatch manifest. | `1`, `2`, `150` | Primary key sequence. |
| `warehouse` | `VARCHAR(50)` | No | No | Regional fulfillment center originating the parcel.| `Chicago`, `Houston`, `New York`, `Dallas` | Categorical fulfillment hub location. |
| `carrier` | `VARCHAR(50)` | No | No | Third-party logistics (3PL) delivery partner. | `FedEx`, `UPS`, `USPS`, `DHL` | Logistics carrier vendor. |
| `shipping_cost`| `NUMERIC(8,2)`| No | No | Billed transportation and handling fee ($). | `18.50`, `45.20`, `95.00` | Cost in USD. Monitored for contractual SLA variances. |
| `estimated_days`| `INTEGER` | No | No | Target SLA transit duration agreed with customer. | `3`, `5`, `7` | Projected days from dispatch to delivery. |
| `actual_days` | `INTEGER` | No | No | Actual elapsed transit time from ship to delivery. | `2`, `5`, `9` | Realized duration recorded upon proof-of-delivery. |
| `delay_days` | `INTEGER` | No | No | Transit overshoot: `MAX(0, actual_days - estimated_days)`. | `0`, `1`, `4` | Zero if on-time or early; positive integer if late. |
| `status` | `VARCHAR(30)` | No | No | SLA compliance status classification. | `On Time`, `Delayed` | Derived from `actual_days <= estimated_days`. |

---

## 4. Derived & Analytical Metrics Definitions

| Metric Name | Formula / SQL Logic | Business Significance |
| :--- | :--- | :--- |
| **Gross Revenue** | `SUM(total_amount)` | Total top-line billed revenue across all non-cancelled orders. |
| **Net Realized Revenue** | `SUM(total_amount) WHERE status = 'Delivered'` | Actual cash collected, excluding returns and cancellations. |
| **Average Order Value (AOV)** | `SUM(total_amount) / COUNT(order_id)` | Average basket size per purchasing transaction. |
| **Return Rate (%)** | `COUNT(order_id WHERE status='Returned') / COUNT(order_id) * 100` | Indicator of product quality, description accuracy, and satisfaction. |
| **On-Time Delivery Rate (%)**| `COUNT(shipment_id WHERE status='On Time') / COUNT(shipment_id) * 100`| Core logistics efficiency KPI measuring customer fulfillment SLA. |
| **Average Delay (Days)** | `AVG(delay_days) WHERE delay_days > 0` | Average severity of fulfillment delivery delays for late shipments. |
