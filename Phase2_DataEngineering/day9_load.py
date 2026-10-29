import pandas as pd
import sqlite3
import logging
import os

# --- Configuration ---
INPUT_FILE = 'day8_transformed_data.csv'
DB_NAME = '../mini-project-1-sales/database/sales.db'
TABLE_NAME = 'sales_data'
LOG_FILE = 'load.log'

# --- Setup Logging ---
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_database_dir():
    """Ensure database directory exists."""
    db_dir = os.path.dirname(DB_NAME)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
        logging.info(f"Created database directory: {db_dir}")

def load_to_sqlite(df):
    """Load dataframe to SQLite database."""
    logging.info(f"Connecting to database: {DB_NAME}")
    
    try:
        conn = sqlite3.connect(DB_NAME)
        
        # Load data
        # if_exists='replace' will drop the table if it exists and recreate it.
        # For an incremental ETL, 'append' is better, but 'replace' is fine for this exercise
        df.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)
        logging.info(f"Successfully loaded {len(df)} rows into table '{TABLE_NAME}'.")
        
        # Validation
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
        count = cursor.fetchone()[0]
        
        if count == len(df):
            logging.info(f"Validation successful: DB count ({count}) matches dataframe count.")
        else:
            logging.warning(f"Validation failed: DB count ({count}) != dataframe count ({len(df)}).")
            
        conn.close()
        
    except sqlite3.Error as e:
        logging.error(f"SQLite error occurred: {e}")
    except Exception as e:
        logging.error(f"Unexpected error loading to database: {e}")

def main():
    logging.info("--- Starting Load Process ---")
    
    create_database_dir()
    
    if not os.path.exists(INPUT_FILE):
        logging.error(f"Input file not found: {INPUT_FILE}")
        return
        
    try:
        df = pd.read_csv(INPUT_FILE)
        logging.info(f"Read {len(df)} rows from {INPUT_FILE}")
        
        load_to_sqlite(df)
        
    except Exception as e:
        logging.error(f"Failed to read input file: {e}")
        
    logging.info("--- Load Process Completed ---")

if __name__ == "__main__":
    main()
