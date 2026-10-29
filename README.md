# Data Science & Analytics Engineering Internship Portfolio

![Python](https://img.shields.io/badge/Python-3.14-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-3.0-green.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive%20Apps-FF4B4B.svg)
![Status](https://img.shields.io/badge/Status-Complete-success.svg)

A comprehensive repository housing all technical artifacts, production data pipelines, analytical SQL models, Jupyter notebooks, interactive Streamlit dashboards, and executive documentation produced during the 30-Day Data Science & Engineering Internship program.

---

## 📑 Program Curriculum & Directory Structure

```
ds-intern_1/
├── Data/
│   ├── Databases/                 # Production SQLite databases (sales.db, operations.db)
│   ├── Processed/                 # Cleaned, transformed datasets ready for modeling
│   └── Raw/                       # Raw extracted CSVs and payload logs
├── Phase1_Foundations/            # Python, Pandas, EDA, and basic & advanced SQL
│   ├── day1.ipynb                 # Pandas DataFrame operations & wrangling
│   ├── day2.ipynb                 # Data cleaning workflow
│   ├── day2_cleaned_dataset.csv   # Cleaned dataset artifact
│   ├── day3_eda.ipynb             # Exploratory Data Analysis with visualizations
│   ├── day4_basic_sql.sql         # 10 fundamental SQL queries (JOINs, aggregations)
│   └── day5_advanced_sql.sql      # 5 advanced analytical SQL queries (CTEs, Window Functions)
├── Phase2_DataEngineering/        # Automated ETL & Data Engineering pipelines
│   ├── day6_etl_elt.md            # Conceptual comparison of ETL vs. ELT architectures
│   ├── day6_pipeline_architecture.png # End-to-end data pipeline flow diagram
│   ├── day7_extract.py            # Extraction from CSV and REST API endpoints
│   ├── day8_transform.py          # Data cleansing and normalization routines
│   ├── day9_load.py               # Idempotent database loading to SQLite
│   └── day10_etl_pipeline.py      # Automated orchestrator script
├── Phase3_MiniProject1_Sales/     # Commercial Sales Analytics Project
│   ├── README.md                  # Project brief and KPI definitions
│   ├── sql/sales_analytics.sql    # 10 core commercial SQL queries
│   └── dashboard/                 # Sales dashboard specifications & drafts
├── Phase4_AnalyticsDeepDive/      # Advanced analytical modeling
│   ├── day16_advanced_pandas.ipynb # Pivot tables, melt, multi-indexing
│   ├── day17_visualization_showcase.ipynb # Publication-ready charts
│   ├── day18_cohort_analysis.ipynb# User retention cohort matrix
│   ├── day19_funnel_analysis.ipynb# Multi-stage conversion funnel analysis
│   └── day20_metrics_framework.md # North star metrics & KPI architecture
├── Phase5_Dashboarding/           # Business Intelligence & Web Apps
│   ├── day21_bi_report/           # BI reporting framework
│   ├── day22_dashboard_redesign/  # Before & after dashboard UX audit
│   ├── day23_streamlit_app/app.py # Interactive Streamlit sales dashboard
│   ├── day24_insight_deck/        # 5-slide commercial insight deck
│   └── day25_revised_dashboard/   # Iterated dashboard and presentation assets
├── Phase6_MiniProject2_Operations/# Supply Chain & Logistics Analytics Project
│   ├── README.md                  # Project scoping doc
│   ├── pipeline/etl.py            # Automated operations ETL pipeline
│   ├── notebooks/analysis.ipynb   # Logistics EDA & carrier delay analysis
│   ├── sql/operations_analytics.sql # 6 logistics analytical queries
│   ├── dashboard/app.py           # Streamlit logistics dashboard application
│   └── presentation/final.md      # 10-slide capstone showcase deck
├── Phase7_WrapUp/                 # Capstone documentation & Data Dictionary
│   ├── data_dictionary.md         # Full schema dictionary for sales and operations
│   ├── pipeline_documentation.md  # Data pipeline architecture documentation
│   └── project_documentation.md   # Overall internship capstone summary
└── internship_tracker.csv         # Complete 30-day artifact tracking matrix
```

---

## 🚀 Key Projects Overview

### Mini Project 1: Commercial Sales Analytics
- **Objective:** Ingest, clean, model, and analyze retail transactions to evaluate regional revenue contribution, category return rates, and discount elasticities.
- **Key Insight:** The West and North regions generate over 65% of sales, while discounting beyond 15% yields diminishing returns on Average Order Value (AOV).
- **Interactive App:** `streamlit run Phase5_Dashboarding/day23_streamlit_app/app.py`

### Mini Project 2: Supply Chain & Logistics Analytics
- **Objective:** Track order fulfillment, warehouse transit durations, and carrier compliance against agreed delivery SLAs.
- **Key Insight:** FedEx leads on-time delivery compliance at 88%, while Houston and Chicago distribution hubs account for 62% of all fulfillment delays.
- **Interactive App:** `streamlit run Phase6_MiniProject2_Operations/dashboard/app.py`

---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/akshay-achanta/ds-intern.git
cd ds-intern
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install pandas numpy matplotlib seaborn plotly streamlit jupyter nbclient
```

### 3. Run the Streamlit Interactive Dashboards
```bash
# Sales Analytics Dashboard
streamlit run Phase5_Dashboarding/day23_streamlit_app/app.py

# Operations & Logistics Dashboard
streamlit run Phase6_MiniProject2_Operations/dashboard/app.py
```

### 4. Run the Automated ETL Pipelines
```bash
# Run Sales Pipeline
python Phase2_DataEngineering/day10_etl_pipeline.py

# Run Operations Pipeline
python Phase6_MiniProject2_Operations/pipeline/etl.py
```
