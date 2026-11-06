import pandas as pd


def analyze_data(file_path):

    df = pd.read_csv(file_path)

    analysis = {
        "numeric_summary": df.describe().to_dict(),
        "average_values": df.select_dtypes(include="number").mean().to_dict(),
        "minimum_values": df.select_dtypes(include="number").min().to_dict(),
        "maximum_values": df.select_dtypes(include="number").max().to_dict()
    }

    return analysis