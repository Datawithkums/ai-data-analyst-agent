import pandas as pd


def profile_data(file_path):
    df = pd.read_csv(file_path)

    profile = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": df.duplicated().sum(),
        "data_types": df.dtypes.astype(str).to_dict()
    }

    return profile