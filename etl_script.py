# ETL Extract Lab - DSA 2040A
# Author: Austin Odera
# Student ID: YOUR_STUDENT_ID

import pandas as pd
from datetime import datetime
import logging
from pathlib import Path

# -------------------------------
# Configuration
# -------------------------------
DATA_PATH = Path('retail_sales_dataset.csv')
TIMESTAMP_PATH = Path('last_extraction.txt')
TIMESTAMP_COLUMN = 'date'  # Change to your datetime column name
REQUIRED_COLUMNS = [TIMESTAMP_COLUMN]  # Add other required columns

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# -------------------------------
# Section 1: Full Extraction
# -------------------------------
def full_extraction():
    """Perform full dataset extraction with validation"""
    logger.info("🔄 Full Extraction in Progress...")
    
    try:
        # Load with explicit dtype specification if needed
        df_full = pd.read_csv(DATA_PATH)
        
        # Data validation
        if not all(col in df_full.columns for col in REQUIRED_COLUMNS):
            missing = set(REQUIRED_COLUMNS) - set(df_full.columns)
            raise ValueError(f"Missing required columns: {missing}")
            
        # Convert timestamp column
        df_full[TIMESTAMP_COLUMN] = pd.to_datetime(df_full[TIMESTAMP_COLUMN])
        
        logger.info(f"✅ Extracted {len(df_full)} rows fully.")
        logger.info(f"📊 Dataset shape: {df_full.shape}")
        logger.info("🔍 First 5 rows:")
        logger.info(df_full.head().to_string())
        
        return df_full
        
    except Exception as e:
        logger.error(f"❌ Full extraction failed: {str(e)}")
        raise

# -------------------------------
# Section 2: Incremental Extraction
# -------------------------------
def incremental_extraction(df_full):
    """Perform incremental extraction based on last timestamp"""
    logger.info("\n🔄 Incremental Extraction in Progress...")
    
    try:
        # Load last extraction time
        if TIMESTAMP_PATH.exists():
            with open(TIMESTAMP_PATH, 'r') as f:
                last_extraction = datetime.strptime(
                    f.read().strip(), 
                    '%Y-%m-%d %H:%M:%S'
                )
        else:
            last_extraction = pd.Timestamp.min
            logger.warning("⚠️ No previous extraction found. Extracting all data.")
        
        # Filter for new records
        df_incremental = df_full[
            df_full[TIMESTAMP_COLUMN] > last_extraction
        ].copy()
        
        logger.info(
            f"✅ Extracted {len(df_incremental)} rows incrementally "
            f"since last check on {last_extraction}."
        )
        
        if not df_incremental.empty:
            logger.info("🔍 New rows:")
            logger.info(df_incremental.head().to_string())
        
        return df_incremental
        
    except Exception as e:
        logger.error(f"❌ Incremental extraction failed: {str(e)}")
        raise

# -------------------------------
# Section 3: Save New Timestamp
# -------------------------------
def update_timestamp(df_incremental):
    """Update extraction timestamp if new data exists"""
    try:
        if not df_incremental.empty:
            latest_time = df_incremental[TIMESTAMP_COLUMN].max()
            with open(TIMESTAMP_PATH, 'w') as f:
                f.write(latest_time.strftime('%Y-%m-%d %H:%M:%S'))
            logger.info(f"🕒 Updated last_extraction.txt to: {latest_time}")
        else:
            logger.info("ℹ️ No new data found. Timestamp not updated.")
    except Exception as e:
        logger.error(f"❌ Timestamp update failed: {str(e)}")
        raise

# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    try:
        # Full extraction
        df_full = full_extraction()
        
        # Incremental extraction
        df_incremental = incremental_extraction(df_full)
        
        # Update timestamp
        update_timestamp(df_incremental)
        
        logger.info("✨ ETL process completed successfully!")
        
    except Exception as e:
        logger.error(f"🔥 ETL process failed: {str(e)}")
