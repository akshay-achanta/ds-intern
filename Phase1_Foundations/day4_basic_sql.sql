-- Day 4: Basic SQL Exercises
-- These queries are designed to be run against a database containing sales data.

-- 1. SELECT and LIMIT: Retrieve the first 10 orders to inspect the data structure
SELECT * 
FROM sales 
LIMIT 10;

-- 2. DISTINCT: Find all unique categories available in the store
SELECT DISTINCT category 
FROM sales;

-- 3. WHERE and ORDER BY: Retrieve all delivered orders in the West region, sorted by date
SELECT order_id, order_date, customer_name, total_amount
FROM sales
WHERE status = 'Delivered' AND region = 'West'
ORDER BY order_date DESC;

-- 4. MIN and MAX: Find the cheapest and most expensive unit prices
SELECT 
    MIN(unit_price) AS lowest_price,
    MAX(unit_price) AS highest_price
FROM sales;

-- 5. COUNT and SUM: Calculate total number of orders and total revenue
SELECT 
    COUNT(order_id) AS total_orders,
    SUM(total_amount) AS total_revenue
FROM sales;

-- 6. AVG: Calculate the average discount given and average total amount per order
SELECT 
    AVG(discount_pct) AS avg_discount,
    AVG(total_amount) AS avg_order_value
FROM sales;

-- 7. GROUP BY and ORDER BY: Find total revenue per region, sorted highest to lowest
SELECT 
    region, 
    SUM(total_amount) AS regional_revenue
FROM sales
GROUP BY region
ORDER BY regional_revenue DESC;

-- 8. HAVING: Find product categories that have generated more than 500,000 in revenue
SELECT 
    category, 
    SUM(total_amount) AS category_revenue
FROM sales
GROUP BY category
HAVING SUM(total_amount) > 500000;

-- 9. INNER JOIN: Assuming a 'customers' table exists, get customer details for orders
-- Note: As we only have one table right now, this is a theoretical query for demonstration.
SELECT 
    s.order_id, 
    s.order_date, 
    c.customer_name, 
    c.email, 
    s.total_amount
FROM sales s
INNER JOIN customers c ON s.customer_name = c.customer_name;

-- 10. LEFT JOIN: Find all orders and their associated salespersons (even if unassigned)
-- Note: Assuming a 'salespersons' table exists.
SELECT 
    s.order_id, 
    s.total_amount, 
    sp.salesperson_name,
    sp.department
FROM sales s
LEFT JOIN salespersons sp ON s.salesperson = sp.salesperson_name;
