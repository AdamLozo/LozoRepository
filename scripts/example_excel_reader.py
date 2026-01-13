"""
Example script: Reading and analyzing Excel files with pandas

This script demonstrates how to:
- Read Excel files
- Perform basic data analysis
- Export results
"""

import pandas as pd
from pathlib import Path

def read_excel_file(file_path: str) -> pd.DataFrame:
    """
    Read an Excel file and return a pandas DataFrame

    Args:
        file_path: Path to the Excel file

    Returns:
        DataFrame containing the Excel data
    """
    try:
        df = pd.read_excel(file_path)
        print(f"Successfully loaded {file_path}")
        print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return pd.DataFrame()


def analyze_data(df: pd.DataFrame) -> dict:
    """
    Perform basic analysis on the DataFrame

    Args:
        df: Input DataFrame

    Returns:
        Dictionary with analysis results
    """
    if df.empty:
        return {}

    analysis = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum().to_dict(),
        "numeric_summary": df.describe().to_dict() if not df.select_dtypes(include='number').empty else {}
    }

    return analysis


def export_to_excel(df: pd.DataFrame, output_path: str):
    """
    Export DataFrame to Excel with formatting

    Args:
        df: DataFrame to export
        output_path: Where to save the Excel file
    """
    try:
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Data', index=False)
        print(f"Data exported to {output_path}")
    except Exception as e:
        print(f"Error exporting to Excel: {e}")


def main():
    """Main execution function"""
    # Example usage
    # Uncomment and modify the file path to test

    # file_path = "data/raw/example.xlsx"
    # df = read_excel_file(file_path)

    # if not df.empty:
    #     # Analyze the data
    #     analysis = analyze_data(df)
    #     print("\nData Analysis:")
    #     for key, value in analysis.items():
    #         print(f"{key}: {value}")
    #
    #     # Export processed data
    #     output_path = "data/processed/analyzed_data.xlsx"
    #     export_to_excel(df, output_path)

    print("Example Excel reader script")
    print("Uncomment the code in main() to process your Excel files")


if __name__ == "__main__":
    main()
