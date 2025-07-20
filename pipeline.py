import pandas as pd
import os

def clean_column_name(col_name):
    """
    Cleans a column name by removing special characters,
    replacing spaces with underscores, and converting to lowercase.
    """
    col_name = col_name.replace(' ', '_')
    col_name = ''.join(e for e in col_name if e.isalnum() or e == '_')
    return col_name.lower()

def run_etl():
    """
    Executes the ETL process: Extract, Transform, Load.
    """
    input_file_path = '/app/data/Medicaldataset.csv'
    output_file_path = '/app/data/CleanedMedicalData.csv' # Output written to a mounted volume

    print(f"--- Starting ETL Process ---")
    print(f"Attempting to read data from: {input_file_path}")

    # 1. Extract
    try:
        df = pd.read_csv(input_file_path)
        print(f"Successfully extracted {len(df)} rows.")
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_file_path}. Please ensure 'Medicaldataset.csv' is in the 'data' directory.")
        return
    except Exception as e:
        print(f"An error occurred during extraction: {e}")
        return

    # 2. Transform
    print("Starting data transformation...")
    # Drop rows with any missing values
    initial_rows = len(df)
    df.dropna(inplace=True)
    rows_after_dropna = len(df)
    print(f"Dropped {initial_rows - rows_after_dropna} rows with missing values.")

    # Clean column names
    original_cols = df.columns.tolist()
    df.columns = [clean_column_name(col) for col in df.columns]
    print(f"Cleaned column names. Example original: {original_cols[0]}, new: {df.columns[0]}")

    print("Data transformation complete.")

    # 3. Load
    print(f"Loading cleaned data to: {output_file_path}")
    try:
        df.to_csv(output_file_path, index=False)
        print(f"Successfully loaded {len(df)} cleaned rows to {output_file_path}")
    except Exception as e:
        print(f"An error occurred during loading: {e}")

    print("--- ETL Process Finished ---")

if __name__ == "__main__":
    run_etl()