import pandas as pd


def check_data_quality(file_path):

    df = pd.read_csv(file_path)

    quality_report = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values": df.isnull().sum().to_dict(),
        "unique_values": df.nunique().to_dict(),
        "numeric_columns": df.select_dtypes(include="number").columns.tolist(),
        "categorical_columns": df.select_dtypes(include="object").columns.tolist()
    }

    return quality_report