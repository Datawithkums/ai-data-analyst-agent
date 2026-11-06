import pandas as pd


def group_analysis(
    file_path,
    group_column,
    value_column,
    operation="mean",
    top_n=10
):

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

    if operation == "min":
        result = result.sort_values(ascending=True)
    else:
        result = result.sort_values(ascending=False)

    result = result.head(top_n)

    return {
        "group_column": group_column,
        "value_column": value_column,
        "operation": operation,
        "top_results": result.to_dict()
    }