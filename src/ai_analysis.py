from llm_client import ask_llm


def explain_data_profile(profile):

    prompt = f"""
You are a Data Analyst.

Analyze the following dataset profile:

Rows: {profile["rows"]}
Columns: {profile["columns"]}

Column Names:
{profile["column_names"]}

Missing Values:
{profile["missing_values"]}

Duplicate Rows:
{profile["duplicate_rows"]}

Data Types:
{profile["data_types"]}

Explain:

1. What this dataset contains
2. Important data quality issues
3. What should be checked next
4. What business analysis could be performed

Keep the explanation practical and beginner-friendly.
"""

    return ask_llm(prompt)