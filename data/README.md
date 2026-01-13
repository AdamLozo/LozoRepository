# Data Directory

## Structure

- `raw/` - Original, immutable data files
- `processed/` - Cleaned and transformed data ready for analysis

## Guidelines

1. **Never modify raw data** - Keep original files intact
2. **Document transformations** - Keep notes on how processed data was created
3. **Use version control carefully** - Large data files may need .gitignore
4. **Consider data privacy** - Don't commit sensitive data to git

## Supported Formats

- Excel (.xlsx, .xls) via openpyxl/xlrd
- CSV files via pandas
- JSON files via pandas/json
- Database exports via SQLAlchemy
- Parquet files via pandas (recommended for large datasets)
