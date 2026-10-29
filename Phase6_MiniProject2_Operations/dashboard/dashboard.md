# Mini Project 2: Operations & Logistics Interactive Dashboard

## 1. Executive Summary
The Operations & Logistics Dashboard provides visibility into order fulfillment velocity, carrier compliance against agreed delivery SLAs, and regional warehouse dispatch bottlenecks.

Built using **Streamlit** and **Plotly**, the application directly queries the production SQLite database (`operations.db`).

---

## 2. Architecture & Tech Stack
- **Application Engine:** Streamlit (`Phase6_MiniProject2_Operations/dashboard/app.py`)
- **Visuals & Charts:** Plotly Express (`px.bar`)
- **Backend Data Source:** SQLite (`operations.db` -> table: `shipments`)
- **Deployment Command:**
  ```bash
  streamlit run Phase6_MiniProject2_Operations/dashboard/app.py
  ```

---

## 3. Key Dashboard Components & Layout

### Header & Top Scorecards (KPIs)
- **Total Shipments Fulfilled:** Tracks gross volume of orders dispatched.
- **On-Time Delivery Rate (%):** Primary operational SLA indicator (target: 80%+).
- **Average Transit Duration:** Mean elapsed days from dispatch to delivery.
- **Average Cost per Shipment ($):** Freight expenditure efficiency benchmark.

### Dynamic Interactive Filters (Sidebar)
- **Warehouse Selector:** Multi-select filtering for Chicago, Houston, New York, Dallas hubs.
- **Carrier Partner Selector:** Filter by 3PL logistics provider (FedEx, UPS, USPS, DHL).

### Visual Analytics
1. **Carrier Reliability Chart (Bar Chart):**
   - Compares on-time delivery percentages across carrier partners to identify reliable vendors.
2. **Warehouse Delay Analysis (Bar Chart):**
   - Highlights hubs with excessive transit delays to prioritize dispatch workflow audits.
3. **Dispatch Manifest Table:**
   - Granular record-level grid displaying shipment ID, routing, actual vs. estimated days, and delivery status.
