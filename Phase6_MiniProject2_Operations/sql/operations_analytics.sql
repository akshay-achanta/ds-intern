-- Mini Project 2: Operations & Logistics Analytics
-- Database: operations.db
-- Table: shipments (shipment_id, warehouse, carrier, shipping_cost, estimated_days, actual_days, status, delay_days)

-- 1. Overall On-Time Delivery Rate & Fulfillment Summary
-- Measures the proportion of shipments meeting or exceeding the delivery SLA.
SELECT 
    COUNT(shipment_id) AS total_shipments,
    SUM(CASE WHEN status = 'On Time' THEN 1 ELSE 0 END) AS on_time_shipments,
    SUM(CASE WHEN status = 'Delayed' THEN 1 ELSE 0 END) AS delayed_shipments,
    ROUND(100.0 * SUM(CASE WHEN status = 'On Time' THEN 1 ELSE 0 END) / COUNT(shipment_id), 2) AS on_time_delivery_rate_pct,
    ROUND(AVG(actual_days), 2) AS avg_actual_days,
    ROUND(AVG(shipping_cost), 2) AS avg_shipping_cost
FROM shipments;

-- 2. Carrier Performance: Cost vs. Speed vs. Reliability
-- Compares major carriers (e.g., UPS, FedEx, USPS, DHL) on cost, average transit time, and delay frequency.
SELECT 
    carrier,
    COUNT(shipment_id) AS shipment_count,
    ROUND(AVG(shipping_cost), 2) AS avg_cost,
    ROUND(AVG(actual_days), 2) AS avg_delivery_days,
    ROUND(AVG(delay_days), 2) AS avg_delay_days,
    ROUND(100.0 * SUM(CASE WHEN status = 'On Time' THEN 1 ELSE 0 END) / COUNT(shipment_id), 2) AS on_time_pct
FROM shipments
GROUP BY carrier
ORDER BY on_time_pct DESC, avg_cost ASC;

-- 3. Warehouse Efficiency & Dispatch Bottlenecks
-- Identifies fulfillment centers with highest average transit times and delay rates.
SELECT 
    warehouse,
    COUNT(shipment_id) AS total_orders_fulfilled,
    ROUND(AVG(actual_days), 2) AS avg_fulfillment_days,
    ROUND(AVG(delay_days), 2) AS avg_delay_days,
    SUM(CASE WHEN delay_days > 0 THEN 1 ELSE 0 END) AS delayed_orders,
    ROUND(100.0 * SUM(CASE WHEN delay_days > 0 THEN 1 ELSE 0 END) / COUNT(shipment_id), 2) AS delay_rate_pct,
    ROUND(SUM(shipping_cost), 2) AS total_spend
FROM shipments
GROUP BY warehouse
ORDER BY delay_rate_pct DESC;

-- 4. Route & Carrier Synergy (Warehouse x Carrier Matrix)
-- Evaluates which carrier performs best for specific warehouse origins to optimize routing assignments.
SELECT 
    warehouse,
    carrier,
    COUNT(shipment_id) AS total_shipments,
    ROUND(AVG(shipping_cost), 2) AS avg_cost,
    ROUND(AVG(delay_days), 2) AS avg_delay,
    ROUND(100.0 * SUM(CASE WHEN status = 'On Time' THEN 1 ELSE 0 END) / COUNT(shipment_id), 2) AS on_time_pct
FROM shipments
GROUP BY warehouse, carrier
HAVING COUNT(shipment_id) >= 5
ORDER BY warehouse ASC, on_time_pct DESC;

-- 5. Outlier Detection: High-Cost Shipments (Above 90th Percentile or 1.5x Avg Cost)
-- Flags anomalous shipping costs that require contract re-negotiation or carrier auditing.
WITH CostStats AS (
    SELECT 
        AVG(shipping_cost) AS overall_avg_cost
    FROM shipments
)
SELECT 
    s.shipment_id,
    s.warehouse,
    s.carrier,
    s.shipping_cost,
    ROUND(cs.overall_avg_cost, 2) AS benchmark_avg_cost,
    ROUND(s.shipping_cost - cs.overall_avg_cost, 2) AS cost_variance,
    s.status,
    s.actual_days
FROM shipments s
CROSS JOIN CostStats cs
WHERE s.shipping_cost > (cs.overall_avg_cost * 1.5)
ORDER BY s.shipping_cost DESC
LIMIT 15;

-- 6. Carrier SLA Ranking with Window Functions
-- Ranks carriers within each warehouse based on lowest average delay and best reliability.
WITH WarehouseCarrierStats AS (
    SELECT 
        warehouse,
        carrier,
        COUNT(shipment_id) AS total_volume,
        ROUND(AVG(delay_days), 2) AS avg_delay,
        ROUND(100.0 * SUM(CASE WHEN status = 'On Time' THEN 1 ELSE 0 END) / COUNT(shipment_id), 2) AS on_time_rate
    FROM shipments
    GROUP BY warehouse, carrier
)
SELECT 
    warehouse,
    carrier,
    total_volume,
    avg_delay,
    on_time_rate,
    RANK() OVER (PARTITION BY warehouse ORDER BY on_time_rate DESC, avg_delay ASC) AS carrier_rank
FROM WarehouseCarrierStats
ORDER BY warehouse, carrier_rank;
