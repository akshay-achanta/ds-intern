import pandas as pd
import requests
import logging
import os
import json
from datetime import datetime

# --- Configuration ---
CSV_FILE_PATH = '../resources/sales-messy.csv'
API_URL = 'https://jsonplaceholder.typicode.com/users'
OUTPUT_DIR = 'raw-data'
LOG_FILE = 'extract.log'

# --- Setup Logging ---
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def setup_directories():
    """Ensure output directories exist."""
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        logging.info(f"Directory '{OUTPUT_DIR}' is ready.")
    except Exception as e:
        logging.error(f"Failed to create directory '{OUTPUT_DIR}': {e}")
        raise

def extract_from_csv(file_path):
    """Extract data from a CSV file."""
    logging.info(f"Starting extraction from CSV: {file_path}")
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Successfully extracted {len(df)} rows from CSV.")
        return df
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        logging.error(f"File is empty: {file_path}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error extracting CSV: {e}")
        return None

def extract_from_api(url):
    """Extract data from a public API."""
    logging.info(f"Starting extraction from API: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Raise exception for HTTP errors
        data = response.json()
        logging.info(f"Successfully extracted data from API.")
        return data
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        logging.error(f"Timeout error occurred: {timeout_err}")
    except Exception as e:
        logging.error(f"Unexpected error extracting from API: {e}")
    return None

def save_raw_data(data, filename, is_json=False):
    """Save extracted raw data to the output directory."""
    file_path = os.path.join(OUTPUT_DIR, filename)
    try:
        if is_json:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
        else:
            data.to_csv(file_path, index=False)
        logging.info(f"Successfully saved raw data to {file_path}")
    except Exception as e:
        logging.error(f"Failed to save data to {file_path}: {e}")

def main():
    logging.info("--- Starting Extraction Process ---")
    setup_directories()
    
    # Extract
    csv_data = extract_from_csv(CSV_FILE_PATH)
    api_data = extract_from_api(API_URL)
    
    # Save
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if csv_data is not None:
        save_raw_data(csv_data, f'raw_sales_{timestamp}.csv')
        
    if api_data is not None:
        save_raw_data(api_data, f'raw_users_{timestamp}.json', is_json=True)
        
    logging.info("--- Extraction Process Completed ---")

if __name__ == "__main__":
    main()
