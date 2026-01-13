"""
Example script: Connecting to databases and loading data

This script demonstrates how to:
- Connect to various databases (SQL Server, PostgreSQL, etc.)
- Query data into pandas DataFrames
- Export to Excel for Power BI
"""

import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


def connect_to_sql_server(server: str, database: str) -> 'Engine':
    """
    Connect to SQL Server database

    Args:
        server: Server name or IP
        database: Database name

    Returns:
        SQLAlchemy engine
    """
    # Using Windows Authentication
    connection_string = f"mssql+pymssql://{server}/{database}"

    # Or using username/password
    # username = os.getenv('DB_USERNAME')
    # password = os.getenv('DB_PASSWORD')
    # connection_string = f"mssql+pymssql://{username}:{password}@{server}/{database}"

    engine = create_engine(connection_string)
    return engine


def connect_to_postgresql(host: str, database: str, user: str, password: str) -> 'Engine':
    """
    Connect to PostgreSQL database

    Args:
        host: Database host
        database: Database name
        user: Username
        password: Password

    Returns:
        SQLAlchemy engine
    """
    connection_string = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"
    engine = create_engine(connection_string)
    return engine


def query_to_dataframe(engine: 'Engine', query: str) -> pd.DataFrame:
    """
    Execute SQL query and return results as DataFrame

    Args:
        engine: Database engine
        query: SQL query string

    Returns:
        DataFrame with query results
    """
    try:
        with engine.connect() as connection:
            df = pd.read_sql(text(query), connection)
        print(f"Query returned {len(df)} rows")
        return df
    except Exception as e:
        print(f"Error executing query: {e}")
        return pd.DataFrame()


def export_for_power_bi(df: pd.DataFrame, output_path: str):
    """
    Export data in format optimized for Power BI

    Args:
        df: DataFrame to export
        output_path: Output file path
    """
    try:
        # Export to Excel - compatible with Power BI
        df.to_excel(output_path, index=False, sheet_name='Data')
        print(f"Data exported to {output_path} for Power BI")

        # Alternative: Export to CSV (faster for large datasets)
        # csv_path = output_path.replace('.xlsx', '.csv')
        # df.to_csv(csv_path, index=False)

    except Exception as e:
        print(f"Error exporting data: {e}")


def main():
    """Main execution function"""

    # Example: SQL Server connection
    # server = "your-server-name"
    # database = "your-database"
    # engine = connect_to_sql_server(server, database)

    # Example: PostgreSQL connection
    # host = os.getenv('PG_HOST', 'localhost')
    # database = os.getenv('PG_DATABASE', 'mydb')
    # user = os.getenv('PG_USER', 'postgres')
    # password = os.getenv('PG_PASSWORD', '')
    # engine = connect_to_postgresql(host, database, user, password)

    # Example query
    # query = """
    # SELECT
    #     date,
    #     product,
    #     sales,
    #     quantity
    # FROM sales_data
    # WHERE date >= '2024-01-01'
    # ORDER BY date DESC
    # """

    # df = query_to_dataframe(engine, query)

    # if not df.empty:
    #     export_for_power_bi(df, "outputs/sales_data_for_powerbi.xlsx")

    print("Example database connection script")
    print("1. Create a .env file with your database credentials")
    print("2. Uncomment and modify the code in main() to connect to your database")
    print("3. Run the script to export data for Power BI")


if __name__ == "__main__":
    main()
