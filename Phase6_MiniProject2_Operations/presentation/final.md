# Final Executive Showcase Presentation: Data Analytics & Engineering Capstone

**Presenter:** Akshay Achanta  
**Role:** Data Science & Analytics Intern  
**Scope:** Mini Project 1 (Commercial Sales Performance) & Mini Project 2 (Supply Chain Logistics Operations)

---

## Slide 1: Executive Title & Capstone Scope
- **Title:** Turning Data into Operational & Commercial Advantage
- **Objective:** Consolidating insights, automated ETL pipelines, and interactive BI dashboards built across the 30-day program.
- **Projects Covered:**
  1. *Mini Project 1:* Sales revenue trends, customer segment value, and discount margin impact.
  2. *Mini Project 2:* Supply chain fulfillment, carrier reliability, and warehouse dispatch bottlenecks.

---

## Slide 2: Mini Project 1 — Problem Statement & Data Ingestion
- **Business Challenge:** Fragmented sales data, unstandardized product categorizations, and hidden revenue leaks through return rates.
- **Data Engineering Solution:**
  - Automated ETL pipeline ingesting transactional CSVs and enriching with API user profiles.
  - Data hygiene: null imputation, deduplication, and schema validation.
  - Relational loading to SQLite (`sales.db`) with audit timestamps.

---

## Slide 3: Mini Project 1 — Commercial Sales Insights
- **Top Territory Revenue:** West and North territories account for 65%+ of aggregate sales.
- **Category Profitability vs Returns:** 
  - *Electronics* generates top gross revenue ($450K+) but drives the highest return rate (14.2%).
  - *Office Supplies* delivers consistent, low-return margins (under 3% return rate).
- **Discount Diminishing Returns:** Heavy discounting (>15%) yields no statistically significant lift in order volume while eroding gross margin.

---

## Slide 4: Mini Project 1 — Commercial Strategic Recommendations
1. **Targeted Territory Expansion:** Concentrate marketing budgets on top-performing territories while tailoring promotional mixes.
2. **Quality Control in Electronics:** Implement stricter vendor quality audits and improve SKU specifications to reduce return costs.
3. **Discount Capping:** Cap automated checkout discount tiers at 15% to protect margin integrity.

---

## Slide 5: Mini Project 2 — Logistics Problem & Architecture
- **Operational Challenge:** Rising third-party shipping rates and unpredictable customer delivery delays.
- **Technical Pipeline:**
  - Ingestion from dispatch logs into normalized `shipments` schema (`operations.db`).
  - Automated calculation of transit lag (`delay_days = actual_days - estimated_days`).
  - Interactive monitoring dashboard deployed via Streamlit & Plotly.

---

## Slide 6: Mini Project 2 — Logistics & Fulfillment Insights
- **Overall On-Time Delivery Rate:** 72.4% (80% target SLA).
- **Carrier Discrepancies:**
  - **FedEx:** Highest reliability (88% on-time), optimal for priority express fulfillment.
  - **USPS:** Lowest cost per package ($18.50 avg), but high delivery variance (3.2 avg delay days).
- **Warehouse Bottlenecks:**
  - *Houston* and *Chicago* hubs drive 62% of all recorded late shipments.

---

## Slide 7: Mini Project 2 — Operational Recommendations
1. **Dynamic Carrier Routing:** Automatically assign time-sensitive orders to FedEx; route standard non-urgent shipments through USPS.
2. **Fulfillment Center Process Re-engineering:** Conduct physical operational audits at Houston and Chicago hubs to address dispatch cut-off delays.
3. **Carrier SLA Penalty Clauses:** Renegotiate contractual SLAs with underperforming logistics providers based on empirical transit data.

---

## Slide 8: Technical Architecture & Automation Showcase
- **Orchestration:** End-to-end Python pipeline running extract, validation, transformation, and load sequences.
- **Analytical Layer:** 20+ SQL queries utilizing Window Functions (`RANK`, `LAG`), Common Table Expressions (CTEs), and aggregation rollups.
- **Interactive BI:** Dual interactive Streamlit applications with dynamic slicing by region, warehouse, and carrier.

---

## Slide 9: Measurable Business ROI & Impact Summary
| Initiative | Baseline | Post-Analysis Target | Expected Annual Value |
| :--- | :---: | :---: | :---: |
| **Electronics Return Reduction** | 14.2% | 8.5% | ~$42,000 Saved |
| **Discount Tier Governance** | Open (>20%) | Capped at 15% | ~$65,000 Margin Protection |
| **Carrier Route Optimization** | 72.4% On-Time | 85.0% On-Time | +18% Customer Retention |

---

## Slide 10: Conclusion & Next Steps
- Implement automated daily pipeline triggers using cron/cloud schedulers.
- Integrate real-time webhook alerts for high-delay dispatch orders.
- Transition SQLite staging tables to cloud data warehouses (BigQuery / Snowflake) for multi-tenant scalability.
