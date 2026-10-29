# Data Engineering & ETL Pipeline Documentation

## 1. Architecture Overview
This project establishes automated, reliable, and auditable Extract, Transform, Load (ETL) data pipelines feeding production-grade analytical databases for commercial retail and supply chain logistics operations.

```
+-------------------------------------------------------------------------------+
|                             DATA SOURCES                                      |
|   +-----------------------+              +--------------------------------+   |
|   |  Flat Files (CSV)     |              |  REST APIs (Mock/Production)   |   |
|   |  - sales-messy.csv    |              |  - DummyJSON / JSONPlaceholder |   |
|   |  - raw_operations.csv |              |  - User metadata & enrichment  |   |
|   +-----------+-----------+              +---------------+----------------+   |
+---------------|------------------------------------------|--------------------+
                |                                          |
                +--------------------+---------------------+
                                     |
                                     v
+-------------------------------------------------------------------------------+
|                       PHASE 2: EXTRACT LAYER (day7_extract.py)                |
|  - Incremental & snapshot data ingestion with file hashing                    |
|  - API error handling with status code checks & fallback defaults             |
|  - Raw payload persistence in `Phase2_DataEngineering/raw-data/`              |
+------------------------------------+------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------------+
|                     TRANSFORMATION LAYER (day8_transform.py)                  |
|  - Schema enforcement and type casting (Dates -> ISO 8601, Numeric types)     |
|  - Null value handling: imputation and coalescing ('Unknown Customer')        |
|  - Deduplication: ID and composite key deduplication                          |
|  - Metric computation: Net amounts, delay durations, SLA compliance           |
|  - Data anomaly flagging: Return loss analysis, negative quantity filters     |
+------------------------------------+------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------------+
|                         LOAD LAYER (day9_load.py)                             |
|  - Relational loading into SQLite / PostgreSQL databases                      |
|  - Idempotent upserts (`if_exists='replace'` or staging-merge pattern)         |
|  - Audit trail logging: `etl_timestamp` injected per loaded row              |
|  - Database targets: `Data/Databases/sales.db` & `operations.db`              |
+------------------------------------+------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------------+
|             ORCHESTRATION & AUTOMATION (day10_etl_pipeline.py)                |
|  - Unified pipeline runner executing Extract -> Transform -> Load sequentially|
|  - Automated scheduling options (Python `schedule` library / Cron daemon)     |
|  - Execution status logging and exception notifications                       |
+-------------------------------------------------------------------------------+
```

---

## 2. Pipeline Components

### 2.1 Extraction (`day7_extract.py`)
- **CSV Ingestion:** Ingests local transactional feeds with validation of headers and encodings.
- **REST API Enrichment:** Queries user and product profile endpoints via `requests`, parsing JSON payloads into structured tabular format.
- **Raw Storage:** Writes point-in-time timestamped artifacts (e.g. `raw_sales_YYYYMMDD_HHMMSS.csv`) ensuring data lineage and replayability.

### 2.2 Transformation (`day8_transform.py` & `Phase6_MiniProject2_Operations/pipeline/etl.py`)
- **Sales Data Transformation:**
  - Converts string date representations into standard `pd.to_datetime`.
  - Normalizes categorical string casings (`title()` / `upper()`).
  - Calculates `total_amount = quantity * unit_price * (1 - discount_pct)`.
  - Handles missing customer identities with defensive defaults.
- **Operations Data Transformation:**
  - Calculates `delay_days = actual_days - estimated_days` with non-negative bounds `max(0, delay)`.
  - Classifies delivery `status` into `On Time` or `Delayed`.

### 2.3 Loading (`day9_load.py`)
- **Relational Storage:** Connects via standard `sqlite3` driver with transaction isolation.
- **Metadata Tagging:** Appends `etl_timestamp` for data freshness tracking.
- **Target Tables:**
  - `sales.db` -> `sales_data` (cleaned) and `raw_sales` (staging).
  - `operations.db` -> `shipments`.

### 2.4 Automation & Orchestration (`day10_etl_pipeline.py`)
- Coordinates the pipeline sequence with try-catch blocks and structured execution logging.
- Includes periodic execution hooks using Python timer loops or OS-level crontab triggers.

---

## 3. Data Quality & Validation Checks

1. **Uniqueness:** Primary keys (`order_id`, `shipment_id`) tested for duplicates; automated dropping of duplicate records.
2. **Value Boundaries:**
   - `quantity > 0`
   - `unit_price >= 0`
   - `discount_pct BETWEEN 0.00 AND 0.50`
   - `actual_days >= 0`
3. **Completeness:** Mandatory columns (`order_date`, `status`, `warehouse`, `carrier`) must be non-null.

---

## 4. Execution Instructions

### Running the Phase 2 Sales Pipeline
```bash
# Navigate to Phase 2 directory
cd Phase2_DataEngineering

# Execute end-to-end automated pipeline
python day10_etl_pipeline.py
```

### Running the Phase 6 Operations Pipeline
```bash
# Navigate to Phase 6 directory
cd Phase6_MiniProject2_Operations/pipeline

# Execute operations ETL
python etl.py
```
