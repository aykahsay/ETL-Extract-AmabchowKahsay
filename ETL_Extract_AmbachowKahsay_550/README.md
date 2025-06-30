# 📊 ETL Extract Lab

**Course**: DSA 2040A – Data Warehousing and Mining
---

### 📘 Description

This project demonstrates **Full Extraction**, **Incremental Extraction**, **Data Transformation**, and **Data Loading** as part of an ETL pipeline using a retail sales dataset. It's designed to help reinforce practical data engineering concepts across ETL stages.

---

### 🔧 Tools Used

* Python
* pandas
* Jupyter Notebook
* SQLite
* Parquet (optional)

---

### 📁 Project Folder Structure

```
ETL_Extract_AmbachowKahsay_550/
├── custom_data.csv                # Raw dataset
├── etl_extract.ipynb             # Full & Incremental Extraction
├── etl_load.ipynb                # Data Loading (Lab 5)
├── transformed_full.csv          # Transformed full dataset
├── transformed_incremental.csv   # Transformed incremental dataset
├── last_extraction.txt           # Timestamp for incremental logic
├── .gitignore                    # Files to exclude in GitHub
├── README.md                     # Project documentation
└── loaded_data/
    ├── full_data.db              # Full dataset in SQLite
    ├── incremental_data.db       # Incremental dataset in SQLite
```

---

## 🔍 Dataset

* **Name**: Retail Sales Dataset
* **Source**: [Kaggle – Mohammad Talib786](https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset)
* **Description**: Contains simulated retail transactions including fields like `Transaction ID`, `Date`, `Customer ID`, `Gender`, `Age`, `Product Category`, `Quantity`,and  `Price per Unit`.

---

## 🔄 Lab 3 – Extraction

* **Full Extraction**: Loads the entire dataset and prints structure + summary.
* **Incremental Extraction**: Extracts only records newer than the timestamp saved in `last_extraction.txt`.
* **Timestamp Update**: Automatically updates after successful incremental extraction.

️✅ Output: Preview of data, extraction logs, and filtered results.

---

## 🔁 Lab 4 – Transformation

Applied **3+ transformations** on both full and incremental data:

### ✅ Cleaning

* Removed duplicate rows
* Handled missing and inconsistent values
* Standardized column formats

### ✅ Enrichment

* Added `Total Amount = Quantity × Price per Unit`
* Categorized `Age` into groups (e.g., 18–25, 26–35, etc.)

### ✅ Structural

* Converted `Date` column to datetime format
* Renamed or formatted columns for clarity

️✅ Output:

* `transformed_full.csv`
* `transformed_incremental.csv`

---

## 📂 Lab 5 – Load

Data was loaded into structured formats:

### ✅ SQLite

* Full data → `loaded_data/full_data.db`
* Incremental data → `loaded_data/incremental_data.db`

### ✅ Example Schema

```sql
CREATE TABLE data (
    Transaction_ID INTEGER,
    Date TEXT,
    Customer_ID TEXT,
    Gender TEXT,
    Age INTEGER,
    Product_Category TEXT,
    Quantity INTEGER,
    Price_per_Unit REAL,
    Total_Amount REAL
);
```

---

## ▶️ How to Run

1. Install requirements:

   ```bash
   pip install pandas
   ```

2. Run extraction:

   ```bash
   jupyter notebook etl_extract.ipynb
   ```

3. Run loading:

   ```bash
   jupyter notebook etl_load.ipynb
   ```

---

## 📆 .gitignore Example

```
.ipynb_checkpoints/
__pycache__/
*.log
*.db
*.parquet
last_extraction.txt
loaded_data/
```

---
