# Capstone Project Documentation: 30-Day Data Analytics & Engineering Internship

## 1. Executive Summary
This capstone document synthesizes the work completed across the 7-phase, 30-day curriculum covering Python data foundations, production ETL pipelines, SQL analytics, advanced pandas modeling, interactive business intelligence dashboards, and supply chain logistics analytics.

### Program Milestones
- **Phase 1 (Foundations):** Pandas data wrangling, data hygiene, exploratory data analysis (EDA), and basic/advanced SQL.
- **Phase 2 (Data Engineering):** Visual pipeline architecture, ETL vs ELT write-up, modular extract/transform/load scripts, and pipeline orchestration.
- **Phase 3 (Mini Project 1 - Commercial Sales):** Ingestion, data cleaning, relational DB loading, and SQL analytics answering core commercial KPIs.
- **Phase 4 (Analytics Deep Dive):** Multi-indexing, pivot tables, cohort retention modeling, customer conversion funnels, and metrics frameworks.
- **Phase 5 (Dashboarding & Storytelling):** BI architecture reports, before-and-after visual redesign principles, interactive Streamlit dashboards, and stakeholder insight decks.
- **Phase 6 (Mini Project 2 - Supply Chain & Operations):** Logistics dataset ingestion, delivery delay tracking, carrier performance comparison, and SQL analytical models.
- **Phase 7 (Wrap-up & Production Readiness):** Centralized data dictionary, pipeline architecture guides, clean repository structuring, and documentation.

---

## 2. Mini Project 1: Sales & Commercial Performance Analytics

### 2.1 Problem Context
The business required automated tracking of $1M+ in annualized gross transactions to evaluate regional revenue distribution, category growth drivers, and identify excessive return rates affecting operating margin.

### 2.2 Key Findings
1. **Regional Concentration:** The **West** and **North** territories account for over 65% of overall delivered revenue.
2. **Category Dynamics:** **Electronics** is the largest revenue-generating category, but also exhibits the highest return rate (14.2%), indicating potential supplier quality or inaccurate online product descriptions.
3. **Discount Elasticity:** Orders with discounts exceeding 15% demonstrated diminishing marginal returns in Average Order Value (AOV).

---

## 3. Mini Project 2: Supply Chain & Operations Logistics

### 3.1 Problem Context
Rising shipping costs and fulfillment delays across national distribution hubs threatened customer delivery SLAs. The logistics department required carrier auditing and origin warehouse bottleneck identification.

### 3.2 Key Findings
1. **SLA Adherence:** Overall On-Time Delivery Rate stands at **72.4%**, indicating a notable gap against the target SLA threshold of 85%.
2. **Carrier Performance:**
   - **FedEx:** Highest on-time delivery rate (88%) with moderate cost per package.
   - **USPS:** Most cost-effective carrier, but accounts for the highest average delivery variance (avg. 3.2 delay days).
3. **Warehouse Bottlenecks:** Houston and Chicago fulfillment centers face systemic dispatch bottlenecks, requiring strict cut-off SLA alignment.

---

## 4. Technical Stack & Tooling

| Capability | Technologies & Libraries |
| :--- | :--- |
| **Programming & Data Wrangling** | Python 3.14, Pandas, NumPy |
| **Relational Databases & SQL** | SQLite3, ANSI SQL (CTEs, Subqueries, Window Functions) |
| **Visualization & Storytelling** | Matplotlib, Seaborn, Plotly Express |
| **Web Application & BI** | Streamlit, BI Dashboard Frameworks |
| **Data Engineering** | Requests (REST APIs), Automated Python Scheduling, File Ingestion |
| **Version Control & CI/CD** | Git, GitHub |

---

## 5. Summary of Key Deliverables

- **3 SQL Script Suites:** Basic SQL (`day4_basic_sql.sql`), Advanced SQL (`day5_advanced_sql.sql`), Sales Analytics (`sales_analytics.sql`), and Operations Analytics (`operations_analytics.sql`).
- **Interactive Web Dashboards:** Streamlit interactive applications featuring cross-filtering, metric scorecards, and Plotly dynamic charts.
- **Production Notebooks:** Fully executed Jupyter notebooks detailing EDA, cohort analysis, and funnel drop-offs.
- **Clean Relational Databases:** `sales.db` and `operations.db` with indexed, normalized schemas.
