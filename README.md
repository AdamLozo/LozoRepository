# LozoRepository

A Python data science project with comprehensive dependency management and best practices.

## 🚀 Quick Start

**New to Python? Start here:** **[GETTING_STARTED.md](GETTING_STARTED.md)**

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 4. Launch Jupyter Lab
jupyter lab
```

## 📊 Project Overview

This project is configured for data science and machine learning work with:
- ✅ **Excel integration** - Read/write .xlsx and .xls files (openpyxl, xlsxwriter)
- ✅ **Database connections** - SQL Server, PostgreSQL, MongoDB support
- ✅ **Power BI compatibility** - Data export and integration ready
- ✅ **Machine learning** - scikit-learn for ML algorithms
- ✅ **Data visualization** - matplotlib, seaborn, plotly
- ✅ **Jupyter notebooks** - Interactive analysis environment

### Project Structure

```
LozoRepository/
├── data/                  # Data files
│   ├── raw/              # Original data (never modify)
│   └── processed/        # Cleaned data
├── notebooks/             # Jupyter notebooks
├── scripts/               # Python scripts
│   ├── example_excel_reader.py
│   └── example_database_connection.py
├── src/                   # Your Python modules
├── outputs/               # Generated reports
├── requirements.txt       # Production dependencies
└── requirements-dev.txt   # Development dependencies
```

## Dependency Management

This repository includes complete documentation for managing dependencies securely and efficiently:

### Core Documentation

- **[DEPENDENCY_AUDIT_REPORT.md](DEPENDENCY_AUDIT_REPORT.md)** - Comprehensive audit report and recommendations
- **[DEPENDENCY_GUIDELINES.md](DEPENDENCY_GUIDELINES.md)** - Detailed guidelines for dependency management
- **[DEPENDENCY_QUICK_REFERENCE.md](DEPENDENCY_QUICK_REFERENCE.md)** - Quick reference cheat sheet for common tasks
- **[DEPENDENCIES.md](DEPENDENCIES.md)** - Tracking document for all project dependencies

### Automation

- **[.github/dependabot.yml](.github/dependabot.yml)** - Dependabot configuration for automated updates
- **[.github/workflows/](.github/workflows/)** - Example CI/CD workflows for security scanning

### Security & Maintenance

Run regular security audits:
```bash
pip-audit              # Check for security vulnerabilities
pip list --outdated    # Check for outdated packages
safety check           # Additional security check
```

**Automated security scanning** runs weekly via GitHub Actions.
**Dependabot** is configured for automatic dependency updates.

## 📚 Learning Resources

- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Complete setup guide and tutorials
- **[DEPENDENCY_QUICK_REFERENCE.md](DEPENDENCY_QUICK_REFERENCE.md)** - Common commands cheat sheet
- **scripts/** - Example scripts for Excel and database operations

### Example Code

**Read Excel File:**
```python
import pandas as pd
df = pd.read_excel('data/raw/your_file.xlsx')
print(df.head())
```

**Connect to Database:**
```python
from sqlalchemy import create_engine
engine = create_engine('mssql+pymssql://server/database')
df = pd.read_sql("SELECT * FROM table", engine)
```

## 🔒 Security Best Practices

1. **Never commit credentials** - Use `.env` file (see `.env.example`)
2. **Run security audits** - Use `pip-audit` before commits
3. **Keep dependencies updated** - Review Dependabot PRs weekly
4. **Review changes** - Check [DEPENDENCIES.md](DEPENDENCIES.md) for all packages

## Contributing

When adding dependencies:
1. Follow the checklist in [DEPENDENCY_GUIDELINES.md](DEPENDENCY_GUIDELINES.md)
2. Update [DEPENDENCIES.md](DEPENDENCIES.md) with the new dependency
3. Ensure all security checks pass in CI/CD

## License

This repository and its documentation are provided as-is for dependency management best practices.