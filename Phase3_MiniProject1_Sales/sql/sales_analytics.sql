-- Mini Project 1: Sales Analytics

-- 1. Total Revenue
SELECT 
    SUM(total_amount) AS total_revenue
FROM raw_sales
WHERE status = 'Delivered';

-- 2. Monthly Revenue Trends
SELECT 
    STRFTIME('%Y-%m', order_date) AS month,
    SUM(total_amount) AS monthly_revenue
FROM raw_sales
WHERE status = 'Delivered' AND order_date IS NOT NULL
GROUP BY STRFTIME('%Y-%m', order_date)
ORDER BY month ASC;

-- 3. Top Products by Revenue
SELECT 
    product,
    SUM(quantity) AS total_quantity_sold,
    SUM(total_amount) AS total_revenue
FROM raw_sales
WHERE status = 'Delivered'
GROUP BY product
ORDER BY total_revenue DESC
LIMIT 5;

-- 4. Top Customers by Revenue
SELECT 
    customer_name,
    COUNT(order_id) AS total_orders,
    SUM(total_amount) AS total_revenue
FROM raw_sales
WHERE status = 'Delivered' AND customer_name != 'Unknown Customer'
GROUP BY customer_name
ORDER BY total_revenue DESC
LIMIT 10;

-- 5. Regional Performance
SELECT 
    region,
    COUNT(order_id) AS order_count,
    SUM(total_amount) AS total_revenue
FROM raw_sales
WHERE status = 'Delivered'
GROUP BY region
ORDER BY total_revenue DESC;

-- 6. Category Performance
SELECT 
    category,
    SUM(quantity) AS total_quantity,
    SUM(total_amount) AS category_revenue
FROM raw_sales
WHERE status = 'Delivered'
GROUP BY category
ORDER BY category_revenue DESC;

-- 7. Average Order Value (AOV)
SELECT 
    COUNT(order_id) AS total_orders,
    SUM(total_amount) AS total_revenue,
    SUM(total_amount) / COUNT(order_id) AS average_order_value
FROM raw_sales
WHERE status = 'Delivered';

-- 8. Return Analysis
SELECT 
    status,
    COUNT(order_id) AS order_count,
    SUM(total_amount) AS potential_revenue_lost
FROM raw_sales
GROUP BY status;

-- 9. Month-over-Month Growth (MoM)
WITH MonthlyRevenue AS (
    SELECT 
        STRFTIME('%Y-%m', order_date) AS month,
        SUM(total_amount) AS revenue
    FROM raw_sales
    WHERE status = 'Delivered' AND order_date IS NOT NULL
    GROUP BY STRFTIME('%Y-%m', order_date)
)
SELECT 
    month,
    revenue,
    LAG(revenue) OVER(ORDER BY month) AS prev_month_revenue,
    ROUND(((revenue - LAG(revenue) OVER(ORDER BY month)) / LAG(revenue) OVER(ORDER BY month)) * 100, 2) AS mom_growth_pct
FROM MonthlyRevenue;

-- 10. Regional Ranking by Revenue
SELECT 
    region,
    SUM(total_amount) AS total_revenue,
    RANK() OVER(ORDER BY SUM(total_amount) DESC) AS revenue_rank
FROM raw_sales
WHERE status = 'Delivered'
GROUP BY region;
