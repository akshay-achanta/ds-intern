import pandas as pd
import numpy as np
import logging
import os
import glob
from datetime import datetime

# --- Configuration ---
RAW_DATA_DIR = 'raw-data'
OUTPUT_FILE = 'day8_transformed_data.csv'
LOG_FILE = 'transform.log'

# --- Setup Logging ---
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_latest_file(directory, pattern):
    """Find the most recently created file matching the pattern."""
    files = glob.glob(os.path.join(directory, pattern))
    if not files:
        return None
    latest_file = max(files, key=os.path.getctime)
    return latest_file

def transform_sales_data(df):
    """Apply cleaning and transformation rules."""
    logging.info(f"Initial shape: {df.shape}")
    
    # 1. Standardization & Column Transformation
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    # 2. Duplicate Removal
    initial_count = len(df)
    df = df.drop_duplicates()
    logging.info(f"Removed {initial_count - len(df)} duplicate rows.")
    
    # 3. Type Conversion & Invalid Value Handling
    if 'unit_price' in df.columns:
        df['unit_price'] = df['unit_price'].astype(str).str.replace('Rs.', '', regex=False).str.replace(',', '').str.strip()
        df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
        
    if 'order_date' in df.columns:
        df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
        
    if 'quantity' in df.columns:
        df['quantity'] = df['quantity'].abs()
    if 'unit_price' in df.columns:
        df['unit_price'] = df['unit_price'].abs()

    # 4. Null Handling
    df['customer_name'] = df['customer_name'].fillna('Unknown Customer')
    df['city'] = df['city'].fillna('Unknown City')
    df['salesperson'] = df['salesperson'].fillna('Unassigned')
    
    if 'discount_pct' in df.columns:
        df['discount_pct'] = df['discount_pct'].fillna(0.0)

    # Drop critical nulls
    df = df.dropna(subset=['order_id', 'order_date'])
    
    # Impute metrics
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    object_cols = df.select_dtypes(include=['object']).columns
    for col in object_cols:
        df[col] = df[col].fillna('Unknown')
        
    # 5. Data Validation & Feature Engineering
    calculated_total = df['quantity'] * df['unit_price'] * (1 - df['discount_pct'] / 100)
    df['total_amount'] = np.where(df['total_amount'].isna() | (df['total_amount'] <= 0), calculated_total, df['total_amount'])
    
    # Add extraction date as metadata
    df['etl_timestamp'] = datetime.now()
    
    logging.info(f"Final shape: {df.shape}")
    return df

def main():
    logging.info("--- Starting Transformation Process ---")
    
    latest_sales_file = get_latest_file(RAW_DATA_DIR, 'raw_sales_*.csv')
    
    if not latest_sales_file:
        logging.error("No raw sales data found to transform.")
        return
        
    logging.info(f"Transforming data from {latest_sales_file}")
    
    try:
        raw_df = pd.read_csv(latest_sales_file)
        transformed_df = transform_sales_data(raw_df)
        
        transformed_df.to_csv(OUTPUT_FILE, index=False)
        logging.info(f"Successfully saved transformed data to {OUTPUT_FILE}")
        
    except Exception as e:
        logging.error(f"Transformation failed: {e}")
        
    logging.info("--- Transformation Process Completed ---")

if __name__ == "__main__":
    main()
