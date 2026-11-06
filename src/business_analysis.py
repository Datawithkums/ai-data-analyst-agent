import pandas as pd


def group_analysis(file_path, group_column, value_column, operation="mean"):

    df = pd.read_csv(file_path)

    if operation == "mean":
        result = df.groupby(group_column)[value_column].mean()

    elif operation == "sum":
        result = df.groupby(group_column)[value_column].sum()

    elif operation == "count":
        result = df.groupby(group_column)[value_column].count()

    elif operation == "max":
        result = df.groupby(group_column)[value_column].max()

    elif operation == "min":
        result = df.groupby(group_column)[value_column].min()

    else:
        raise ValueError("Unsupported operation")

    return result.sort_values(ascending=False)