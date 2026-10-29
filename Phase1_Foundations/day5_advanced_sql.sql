-- Day 5: Advanced SQL Analytical Queries

-- 1. Subqueries & CTEs: Find customers who have spent more than the average customer.
-- Business Purpose: Identify high-value customers for VIP marketing campaigns.
WITH CustomerTotals AS (
    SELECT customer_name, SUM(total_amount) AS customer_total
    FROM sales
    GROUP BY customer_name
),
AverageSpend AS (
    SELECT AVG(customer_total) AS avg_spend
    FROM CustomerTotals
)
SELECT customer_name, customer_total
FROM CustomerTotals
WHERE customer_total > (SELECT avg_spend FROM AverageSpend)
ORDER BY customer_total DESC;


-- 2. ROW_NUMBER() & Ranking: Find the top 3 most expensive orders per region.
-- Business Purpose: Understand what drives the highest revenue in each geographical area.
WITH RankedOrders AS (
    SELECT 
        region,
        order_id,
        total_amount,
        ROW_NUMBER() OVER(PARTITION BY region ORDER BY total_amount DESC) as rank
    FROM sales
)
SELECT region, order_id, total_amount, rank
FROM RankedOrders
WHERE rank <= 3;


-- 3. RANK(): Rank salespersons by total revenue generated.
-- Business Purpose: Determine performance bonuses and identify top-performing sales staff.
SELECT 
    salesperson,
    SUM(total_amount) AS total_revenue,
    RANK() OVER(ORDER BY SUM(total_amount) DESC) as sales_rank
FROM sales
WHERE salesperson != 'Unassigned'
GROUP BY salesperson;


-- 4. LAG() & Month-over-Month Analysis: Calculate month-over-month revenue growth.
-- Business Purpose: Track the overall growth trajectory of the business and spot seasonal trends.
WITH MonthlyRevenue AS (
    SELECT 
        STRFTIME('%Y-%m', order_date) AS order_month,
        SUM(total_amount) AS revenue
    FROM sales
    WHERE order_date IS NOT NULL
    GROUP BY STRFTIME('%Y-%m', order_date)
),
RevenueWithLag AS (
    SELECT 
        order_month,
        revenue,
        LAG(revenue) OVER(ORDER BY order_month) AS prev_month_revenue
    FROM MonthlyRevenue
)
SELECT 
    order_month,
    revenue,
    prev_month_revenue,
    CASE 
        WHEN prev_month_revenue IS NULL THEN 0
        ELSE ((revenue - prev_month_revenue) / prev_month_revenue) * 100 
    END AS mom_growth_pct
FROM RevenueWithLag;


-- 5. Running Totals & LEAD(): Calculate cumulative revenue over time and days until next order.
-- Business Purpose: Monitor how quickly we reach revenue milestones throughout the year.
SELECT 
    order_date,
    total_amount,
    SUM(total_amount) OVER(ORDER BY order_date) AS running_total_revenue,
    LEAD(order_date) OVER(ORDER BY order_date) AS next_order_date
FROM sales
WHERE order_date IS NOT NULL
ORDER BY order_date;
