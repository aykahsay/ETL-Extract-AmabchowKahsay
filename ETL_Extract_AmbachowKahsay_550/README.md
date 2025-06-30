# ETL Extract Lab

---

### 📘 Description

This project demonstrates **Full Extraction** and **Incremental Extraction** in the context of ETL (Extract, Transform, Load) using a retail sales dataset. The lab is designed for **DSA 2040A – Data Warehousing and Data Mining**, and helps reinforce the practical aspects of extraction within the ETL pipeline.

---

### 🔧 Tools Used

- Python
- pandas
- Jupyter Notebook

---
## 📁 Project Folder Structure

**Folder**: `ETL_Extract_AmbachowKahsay_550`

| File/Folder Name              | Description                                             |
|-------------------------------|---------------------------------------------------------|
| `etl_extract.ipynb`           | Main notebook with Full and Incremental extraction logic |
| `etl_load.ipynb`              | Lab 5 notebook to load transformed data                 |
| `custom_data.csv`             | Source dataset (realistic sales data)                   |
| `transformed_full.csv`        | Transformed full dataset (cleaned, enriched)            |
| `transformed_incremental.csv` | Transformed incremental dataset                         |
| `last_extraction.txt`         | Stores the last extraction timestamp                    |
| `README.md`                   | This documentation file                                 |
| `.gitignore`                  | Excludes unnecessary or large files                     |
| `loaded_data/`                | Output folder for databases and Parquet files           |
| ├── `full_data.db`            | SQLite database for full dataset                        |
| ├── `incremental_data.db`     | SQLite database for incremental dataset                 |
| └── `full_data.parquet`       | Parquet file containing full dataset                    |

---

---

## 🔍 Dataset

- **Filename**: `custom_data.csv`  
- **Description**: Simulated retail transactions  
- **Source**: [Download here](https://github.com/aykahsay/ETL-Extract-AmabchowKahsay/raw/main/custom_data.csv)

---

## 🔄 Lab 3 – Extraction

**Features:**

- **Full Extraction**: Loads the entire dataset and shows summary stats.
- **Incremental Extraction**: Filters new rows based on a saved timestamp (`last_extraction.txt`).
- **Timestamp Update**: Automatically updates the extraction time after each run.

---

## 🔁 Lab 4 – Transformation

**Three Key Transformations:**

1. **Cleaning**:
   - Removed duplicate records
   - Filled missing values in `Quantity` and `Price per Unit`

2. **Enrichment**:
   - Created a new `Total Price` column = `Quantity × Price per Unit`

3. **Structural**:
   - Standardized `Date` column to proper datetime format

**Outputs:**

- `transformed_full.csv`
- `transformed_incremental.csv`

---

## 📦 Lab 5 – Load

**Goal**: Load transformed datasets into a structured database (SQLite)

**SQLite Output Files:**

- `loaded_data/full_data.db`
- `loaded_data/incremental_data.db`

**Example Table Schema**:

```sql
CREATE TABLE data (
    Transaction_ID INTEGER,
    Date TEXT,
    Customer_ID TEXT,
    Gender TEXT,
    Age INTEGER,
    Product_Category TEXT,
    Quantity INTEGER,
    Price_per_Unit INTEGER,
    Total_Amount INTEGER
);
```
---

## How to Run
1. Ensure Python and Jupyter are installed
2. Install required packages: `pip install pandas`
3. Open the notebook: `jupyter notebook etl_extract.ipynb`
4. Run all cells sequentially

### 🧪 How to Reproduce

1. Clone the repository:
   ```bash
   git clone https://github.com/aykahsay/ETL-Extract-AmabchowKahsay.git
   cd ETL-Extract-AmabchowKahsay
   Source: Downloaded from Kaggle
