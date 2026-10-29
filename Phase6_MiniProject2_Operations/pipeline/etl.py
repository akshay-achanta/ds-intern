import pandas as pd
import sqlite3
import os

def run_etl():
    print("Extracting operations data...")
    # Simulated extraction
    df = pd.read_csv('../Data/Raw/raw_operations.csv')
    
    print("Transforming operations data...")
    df['delay_days'] = df['actual_days'] - df['estimated_days']
    df['delay_days'] = df['delay_days'].apply(lambda x: x if x > 0 else 0)
    
    print("Loading into database...")
    db_path = '../Data/Databases/operations.db'
    conn = sqlite3.connect(db_path)
    df.to_sql('shipments', conn, if_exists='replace', index=False)
    conn.close()
    print("ETL Complete.")

if __name__ == '__main__':
    run_etl()
