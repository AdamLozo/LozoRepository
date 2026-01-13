# Getting Started with Python Data Science

Welcome! This guide will help you set up your Python environment and start working with data science and machine learning.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Quick Start](#quick-start)
5. [Working with Excel](#working-with-excel)
6. [Database Connections](#database-connections)
7. [Power BI Integration](#power-bi-integration)
8. [Next Steps](#next-steps)

## Prerequisites

### Install Python

**Windows:**
1. Download Python from https://www.python.org/downloads/ (version 3.11 or higher)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Verify installation: Open Command Prompt and type `python --version`

**Mac:**
```bash
# Using Homebrew (recommended)
brew install python@3.11
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.11 python3-pip python3-venv
```

### Install Git (if not already installed)

Download from: https://git-scm.com/downloads

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AdamLozo/LozoRepository.git
cd LozoRepository
```

### 2. Create a Virtual Environment

A virtual environment keeps your project dependencies isolated from other Python projects.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt when activated.

### 3. Install Dependencies

```bash
# Install production dependencies
pip install -r requirements.txt

# Install development dependencies (includes Jupyter)
pip install -r requirements-dev.txt
```

### 4. Verify Installation

```bash
# Check installed packages
pip list

# Test Python
python -c "import pandas; print(pandas.__version__)"
```

## Project Structure

```
LozoRepository/
├── data/                      # Data files
│   ├── raw/                  # Original data (never modify)
│   └── processed/            # Cleaned/transformed data
├── notebooks/                # Jupyter notebooks for exploration
├── scripts/                  # Python scripts
│   ├── example_excel_reader.py
│   └── example_database_connection.py
├── src/                      # Your Python modules
├── outputs/                  # Generated reports/files
├── tests/                    # Unit tests
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development dependencies
└── .env                      # Environment variables (create from .env.example)
```

## Quick Start

### Option 1: Jupyter Notebook (Recommended for Beginners)

Jupyter provides an interactive environment perfect for learning and exploration.

```bash
# Launch Jupyter Lab
jupyter lab
```

Your browser will open with Jupyter Lab. Navigate to the `notebooks/` folder and create a new notebook.

**Try this in a new notebook:**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [1000, 1500, 1200, 1800, 2000]
}

df = pd.DataFrame(data)

# Display data
print(df)

# Create a simple plot
df.plot(x='Month', y='Sales', kind='bar')
plt.title('Monthly Sales')
plt.show()
```

### Option 2: Python Scripts

Run the example scripts:

```bash
# Excel reader example
python scripts/example_excel_reader.py

# Database connection example
python scripts/example_database_connection.py
```

## Working with Excel

### Reading Excel Files

```python
import pandas as pd

# Read Excel file
df = pd.read_excel('data/raw/your_file.xlsx')

# View first few rows
print(df.head())

# Get column names
print(df.columns)

# Basic statistics
print(df.describe())
```

### Writing to Excel

```python
# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 92, 78]
})

# Save to Excel
df.to_excel('data/processed/results.xlsx', index=False)

# Multiple sheets
with pd.ExcelWriter('data/processed/report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Scores', index=False)
    df.describe().to_excel(writer, sheet_name='Statistics')
```

### Advanced Excel Operations

```python
import openpyxl
from openpyxl.styles import Font, PatternFill

# Create workbook
wb = openpyxl.Workbook()
ws = wb.active

# Add data
ws['A1'] = 'Report Title'
ws['A1'].font = Font(size=14, bold=True)
ws['A1'].fill = PatternFill(start_color="FFFF00", fill_type="solid")

# Save
wb.save('data/processed/formatted_report.xlsx')
```

## Database Connections

### SQL Server

```python
from sqlalchemy import create_engine
import pandas as pd

# Connect (Windows Authentication)
engine = create_engine('mssql+pymssql://server_name/database_name')

# Query data
query = "SELECT * FROM table_name WHERE date >= '2024-01-01'"
df = pd.read_sql(query, engine)

print(df.head())
```

### PostgreSQL

```python
from sqlalchemy import create_engine
import pandas as pd

# Connect
engine = create_engine('postgresql+psycopg2://user:password@localhost/dbname')

# Query data
df = pd.read_sql("SELECT * FROM customers", engine)
```

### Using Environment Variables (Secure)

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your actual credentials

3. Use in your code:
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()

   db_server = os.getenv('DB_SERVER')
   db_database = os.getenv('DB_DATABASE')
   ```

## Power BI Integration

### Export Data for Power BI

```python
import pandas as pd

# Your data processing
df = pd.read_sql("SELECT * FROM sales", engine)

# Clean and transform
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

# Export to Excel for Power BI
df.to_excel('outputs/powerbi_data.xlsx', index=False)
```

### Use Python in Power BI

Power BI can run Python scripts directly:

1. In Power BI Desktop, go to **Get Data** > **Python script**
2. Paste your Python code:
   ```python
   import pandas as pd

   # Your code here
   df = pd.read_excel('data.xlsx')

   # Power BI will import 'df'
   ```

## Common Tasks

### Load CSV File

```python
df = pd.read_csv('data/raw/data.csv')
```

### Filter Data

```python
# Filter rows where sales > 1000
filtered = df[df['sales'] > 1000]

# Multiple conditions
filtered = df[(df['sales'] > 1000) & (df['region'] == 'North')]
```

### Group and Aggregate

```python
# Group by region and sum sales
summary = df.groupby('region')['sales'].sum()

# Multiple aggregations
summary = df.groupby('region').agg({
    'sales': 'sum',
    'quantity': 'mean',
    'customer': 'count'
})
```

### Merge DataFrames

```python
# Like Excel VLOOKUP
merged = pd.merge(df1, df2, on='customer_id', how='left')
```

### Create Visualizations

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Bar chart
df.plot(x='month', y='sales', kind='bar')
plt.show()

# Line chart
df.plot(x='date', y='sales', kind='line')
plt.show()

# Scatter plot with seaborn
sns.scatterplot(data=df, x='advertising', y='sales')
plt.show()
```

## Best Practices

### 1. Use Virtual Environments

Always activate your virtual environment before working:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 2. Keep Dependencies Updated

```bash
# Check for security issues
pip-audit

# Update a package
pip install --upgrade pandas
```

### 3. Never Commit Sensitive Data

- Use `.env` for credentials (already in `.gitignore`)
- Don't commit large data files
- Use `.gitignore` for data folders if needed

### 4. Document Your Work

- Add comments to your code
- Use Jupyter markdown cells
- Keep a notebook of your analysis steps

### 5. Test Your Code

```python
# Simple assertion tests
assert len(df) > 0, "DataFrame is empty"
assert 'sales' in df.columns, "Sales column missing"
```

## Troubleshooting

### "Module not found" Error

```bash
# Make sure virtual environment is activated
# Then reinstall requirements
pip install -r requirements.txt
```

### Excel File Won't Open

```python
# Try different engines
df = pd.read_excel('file.xlsx', engine='openpyxl')  # .xlsx
df = pd.read_excel('file.xls', engine='xlrd')      # .xls
```

### Database Connection Fails

1. Check credentials in `.env`
2. Verify database server is running
3. Check firewall settings
4. Test with a simple SQL query first

### Import Errors in Jupyter

```python
# Restart the kernel: Kernel -> Restart Kernel
# Or reload modules
%load_ext autoreload
%autoreload 2
```

## Next Steps

### Learning Resources

**Python Basics:**
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)

**Pandas (Data Manipulation):**
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

**Data Visualization:**
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

**Machine Learning:**
- [Scikit-learn Tutorial](https://scikit-learn.org/stable/tutorial/index.html)
- [Kaggle Learn](https://www.kaggle.com/learn)

### Suggested Projects

1. **Excel Report Automation**: Automate your weekly Excel reports
2. **Database to Power BI Pipeline**: Create automated data exports
3. **Sales Analysis**: Analyze sales trends and create visualizations
4. **Data Cleaning**: Clean and standardize messy data
5. **Prediction Model**: Build a simple ML model for forecasting

## Getting Help

- Check [DEPENDENCY_QUICK_REFERENCE.md](DEPENDENCY_QUICK_REFERENCE.md) for common commands
- Review [DEPENDENCY_GUIDELINES.md](DEPENDENCY_GUIDELINES.md) for best practices
- Search [Stack Overflow](https://stackoverflow.com/questions/tagged/python) for specific issues
- Check package documentation

## Security Reminders

```bash
# Regular security checks
pip-audit

# Keep dependencies updated
pip list --outdated
```

---

**Ready to start?** Open Jupyter Lab and create your first notebook:

```bash
jupyter lab
```

Happy coding! 🐍📊
