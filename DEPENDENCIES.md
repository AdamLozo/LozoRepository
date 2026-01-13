# Dependencies

This file tracks all dependencies used in this project, their purpose, and rationale for inclusion.

## Production Dependencies

### Core Data Science Stack

#### numpy (1.26.4)
- **Purpose**: Foundation for numerical computing in Python, provides fast array operations
- **Alternatives Considered**: None - industry standard
- **Size Impact**: ~30MB installed
- **Security**: Mature project with active security monitoring
- **Last Reviewed**: 2026-01-13
- **Maintainer Notes**: Required by pandas, scipy, and most ML libraries

#### pandas (2.2.0)
- **Purpose**: Primary library for data manipulation and analysis, Excel-like operations
- **Alternatives Considered**: Polars (faster but less mature), Dask (for very large data)
- **Size Impact**: ~45MB installed
- **Security**: Well-maintained, large community
- **Last Reviewed**: 2026-01-13
- **Maintainer Notes**: Essential for data science work

#### scipy (1.12.0)
- **Purpose**: Scientific computing and advanced mathematical functions
- **Alternatives Considered**: None for scientific computing needs
- **Size Impact**: ~40MB installed
- **Last Reviewed**: 2026-01-13

### Visualization

#### matplotlib (3.8.2)
- **Purpose**: Core plotting library for data visualization
- **Alternatives Considered**: None - foundation for other viz libraries
- **Last Reviewed**: 2026-01-13

#### seaborn (0.13.1)
- **Purpose**: Statistical visualizations built on matplotlib
- **Alternatives Considered**: plotly for interactive (included both)
- **Last Reviewed**: 2026-01-13

#### plotly (5.18.0)
- **Purpose**: Interactive visualizations for web and dashboards
- **Alternatives Considered**: bokeh (less popular)
- **Last Reviewed**: 2026-01-13

### Machine Learning

#### scikit-learn (1.4.0)
- **Purpose**: Machine learning algorithms and tools
- **Alternatives Considered**: TensorFlow/PyTorch for deep learning (can be added later)
- **Size Impact**: ~35MB installed
- **Last Reviewed**: 2026-01-13
- **Maintainer Notes**: Best for traditional ML algorithms

### Excel and File Handling

#### openpyxl (3.1.2)
- **Purpose**: Read and write Excel 2010+ files (.xlsx)
- **Alternatives Considered**: xlsxwriter (write-only), xlwings (requires Excel installed)
- **Last Reviewed**: 2026-01-13
- **Maintainer Notes**: Required for pandas Excel operations

#### xlsxwriter (3.1.9)
- **Purpose**: Advanced Excel file creation with formatting
- **Alternatives Considered**: openpyxl (included both for different use cases)
- **Last Reviewed**: 2026-01-13

#### xlrd (2.0.1)
- **Purpose**: Read legacy Excel files (.xls)
- **Last Reviewed**: 2026-01-13
- **Maintainer Notes**: Only for old .xls files, use openpyxl for .xlsx

### Database Connections

#### sqlalchemy (2.0.25)
- **Purpose**: SQL toolkit and ORM for database operations
- **Alternatives Considered**: Direct drivers (less abstraction)
- **Last Reviewed**: 2026-01-13
- **Maintainer Notes**: Works with pandas for easy data loading

#### psycopg2-binary (2.9.9)
- **Purpose**: PostgreSQL database adapter
- **Alternatives Considered**: psycopg3 (newer, less stable)
- **Last Reviewed**: 2026-01-13

#### pymssql (2.2.11)
- **Purpose**: Microsoft SQL Server adapter
- **Alternatives Considered**: pyodbc (more complex setup)
- **Last Reviewed**: 2026-01-13
- **Maintainer Notes**: Good for SQL Server connections

#### pymongo (4.6.1)
- **Purpose**: MongoDB driver
- **Last Reviewed**: 2026-01-13

### HTTP and APIs

#### requests (2.31.0)
- **Purpose**: HTTP library for API calls
- **Alternatives Considered**: httpx (async), urllib (built-in but less friendly)
- **Last Reviewed**: 2026-01-13
- **Maintainer Notes**: Industry standard for HTTP requests

#### urllib3 (2.1.0)
- **Purpose**: HTTP client, dependency of requests
- **Last Reviewed**: 2026-01-13

### Data Validation

#### pydantic (2.5.3)
- **Purpose**: Data validation using Python type hints
- **Alternatives Considered**: marshmallow (less modern)
- **Last Reviewed**: 2026-01-13

### Utilities

#### python-dotenv (1.0.1)
- **Purpose**: Load environment variables from .env file
- **Last Reviewed**: 2026-01-13
- **Maintainer Notes**: Essential for secure credential management

#### tqdm (4.66.1)
- **Purpose**: Progress bars for loops and operations
- **Last Reviewed**: 2026-01-13

<!-- Template for adding production dependencies:

### package-name (version)
- **Purpose**: Description of why this package is used and what problem it solves
- **Alternatives Considered**: Other packages that were evaluated
- **Size Impact**: Bundle size or installation size (if applicable)
- **Security**: Link to security policy or known issues
- **Last Reviewed**: YYYY-MM-DD
- **Maintainer Notes**: Any special considerations or known limitations

-->

## Development Dependencies

### Testing

#### pytest (7.4.4)
- **Purpose**: Testing framework for Python
- **Scope**: Unit and integration testing
- **Last Reviewed**: 2026-01-13

#### pytest-cov (4.1.0)
- **Purpose**: Test coverage reporting
- **Scope**: Measure code coverage during testing
- **Last Reviewed**: 2026-01-13

### Code Quality

#### black (24.1.1)
- **Purpose**: Automatic code formatter
- **Scope**: Code formatting and style consistency
- **Last Reviewed**: 2026-01-13

#### flake8 (7.0.0)
- **Purpose**: Linting and style checking
- **Scope**: Code quality checks
- **Last Reviewed**: 2026-01-13

#### pylint (3.0.3)
- **Purpose**: Comprehensive code analysis
- **Scope**: Code quality and best practices
- **Last Reviewed**: 2026-01-13

#### mypy (1.8.0)
- **Purpose**: Static type checking
- **Scope**: Type hint validation
- **Last Reviewed**: 2026-01-13

### Security

#### pip-audit (2.7.0)
- **Purpose**: Scan for security vulnerabilities in dependencies
- **Scope**: Security auditing
- **Last Reviewed**: 2026-01-13

#### safety (3.0.1)
- **Purpose**: Check dependencies against known security vulnerabilities
- **Scope**: Security checking
- **Last Reviewed**: 2026-01-13

#### bandit (1.7.6)
- **Purpose**: Security linting for Python code
- **Scope**: Find common security issues in code
- **Last Reviewed**: 2026-01-13

### Documentation

#### sphinx (7.2.6)
- **Purpose**: Documentation generator
- **Scope**: Create project documentation
- **Last Reviewed**: 2026-01-13

### Jupyter

#### jupyter (1.0.0)
- **Purpose**: Jupyter notebook environment
- **Scope**: Interactive data analysis and exploration
- **Last Reviewed**: 2026-01-13

#### ipykernel (6.29.0)
- **Purpose**: IPython kernel for Jupyter
- **Scope**: Jupyter notebook backend
- **Last Reviewed**: 2026-01-13

#### jupyterlab (4.0.11)
- **Purpose**: Modern Jupyter interface
- **Scope**: Enhanced notebook environment
- **Last Reviewed**: 2026-01-13

### Development Tools

#### ipython (8.20.0)
- **Purpose**: Enhanced interactive Python shell
- **Scope**: Development and debugging
- **Last Reviewed**: 2026-01-13

<!-- Template for adding development dependencies:

### package-name (version)
- **Purpose**: Description of development/testing purpose
- **Scope**: Which part of development process (testing, building, linting, etc.)
- **Last Reviewed**: YYYY-MM-DD

-->

## Dependency Decision Log

This section tracks major decisions about dependencies.

### 2026-01-13: Initial Data Science Stack

**Decision**: Added comprehensive Python data science stack
**Reason**: Project requirements include data science, ML, Excel integration, and database connections for Power BI reporting
**Alternatives**:
- Considered minimal setup, but comprehensive stack better for learning and growth
- Evaluated TensorFlow/PyTorch but deferred to keep initial setup manageable
**Impact**:
- ~250MB total installation size
- Complete environment for data analysis, ML, Excel, and database work
- All tools needed for Excel and Power BI integration
- Beginner-friendly with Jupyter notebooks

### Key Dependencies Rationale

**pandas + numpy**: Non-negotiable for data science
**scikit-learn**: Standard ML library, perfect for learning
**openpyxl + xlsxwriter**: Excel integration (read/write)
**sqlalchemy + database drivers**: Multi-database support
**matplotlib + seaborn + plotly**: Comprehensive visualization options
**jupyter**: Essential for interactive learning and exploration

---

**Note:** This file should be updated whenever dependencies are added, removed, or significantly updated. Review this file quarterly as part of the dependency audit process.

**Last Updated:** 2026-01-13
