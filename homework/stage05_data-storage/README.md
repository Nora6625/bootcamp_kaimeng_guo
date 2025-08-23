## Data Storage

**Folder Structure:**
- `data/raw/` — stores raw CSV files
- `data/processed/` — stores processed Parquet files

**Formats Used:**
- CSV: human-readable, easy to inspect
- Parquet: columnar, efficient for analytics

**Code Implementation:**
- Paths are read from `.env` using `DATA_DIR_RAW` and `DATA_DIR_PROCESSED`
- `write_df` and `read_df` handle CSV/Parquet automatically
- Missing directories are created automatically
- Parquet engine absence is handled with a clear message
