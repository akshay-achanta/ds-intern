import logging
import schedule
import time
from datetime import datetime
import day7_extract
import day8_transform
import day9_load

# --- Setup Logging ---
LOG_FILE = 'pipeline.log'
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - ETL PIPELINE - %(message)s'
)

def run_etl_pipeline():
    """Execute the full Extract, Transform, Load pipeline."""
    logging.info("="*50)
    logging.info(f"Starting ETL Pipeline Run at {datetime.now()}")
    
    try:
        # --- EXTRACT ---
        logging.info("STAGE 1: EXTRACT")
        day7_extract.setup_directories()
        
        # We focus on the CSV extraction for the main pipeline flow
        raw_df = day7_extract.extract_from_csv(day7_extract.CSV_FILE_PATH)
        if raw_df is None or raw_df.empty:
            raise ValueError("Extraction failed or returned empty data.")
        
        # Save raw extraction
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        day7_extract.save_raw_data(raw_df, f'pipeline_raw_sales_{timestamp}.csv')
        
        # --- TRANSFORM ---
        logging.info("STAGE 2: TRANSFORM")
        transformed_df = day8_transform.transform_sales_data(raw_df)
        if transformed_df is None or transformed_df.empty:
            raise ValueError("Transformation failed or returned empty data.")
            
        # Save transformed state
        transformed_df.to_csv(day8_transform.OUTPUT_FILE, index=False)
        
        # --- LOAD ---
        logging.info("STAGE 3: LOAD")
        day9_load.create_database_dir()
        day9_load.load_to_sqlite(transformed_df)
        
        logging.info("ETL Pipeline Run Completed Successfully!")
        print(f"[{datetime.now()}] ETL Pipeline Success")
        
    except Exception as e:
        logging.error(f"ETL PIPELINE FAILED: {str(e)}")
        print(f"[{datetime.now()}] ETL Pipeline Failed: {str(e)}")
    finally:
        logging.info("="*50)

def main():
    """Main execution block with basic scheduling demonstration."""
    print("Starting Automated ETL Pipeline...")
    
    # Run once immediately
    run_etl_pipeline()
    
    # Schedule to run every day at 2:00 AM
    schedule.every().day.at("02:00").do(run_etl_pipeline)
    
    print("Pipeline scheduled. Press Ctrl+C to exit.")
    
    # Keep the script running to execute scheduled jobs
    # (Uncomment the loop below to run in background continuously)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)

if __name__ == "__main__":
    main()
