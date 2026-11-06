from llm_client import ask_llm
import json
import pandas as pd


def create_analysis_plan(question, dataset_columns, file_path):

    question_lower = question.lower()

    # --------------------------------------------------
    # Detect metric directly from the user's question
    # --------------------------------------------------

    if "rating" in question_lower:
        expected_value_column = "Rating"

    elif "vote" in question_lower:
        expected_value_column = "Votes"

    elif any(
        word in question_lower
        for word in ["cost", "price", "spend", "expense"]
    ):
        expected_value_column = "Average_Cost_for_two"

    else:
        expected_value_column = None

    # --------------------------------------------------
    # Ask AI to create the analysis plan
    # --------------------------------------------------

    prompt = f"""
You are a Data Analyst AI.

Dataset columns:

{dataset_columns}

User question:

{question}

Create an analysis plan.

Return ONLY one valid JSON object.

Format:

{{
    "group_column": "column name",
    "value_column": "column name",
    "operation": "mean"
}}

Allowed operations:

mean
sum
count
max
min

Important:

Choose the value_column that matches the metric requested
by the user.

For example:

rating -> Rating
votes -> Votes
cost -> Average_Cost_for_two

Do not provide explanations.
Do not use markdown.
Do not return a JSON array.
"""

    response = ask_llm(prompt).strip()

    # Remove markdown fences if AI adds them
    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    print("\n===== RAW AI PLAN =====")
    print(response)

    # --------------------------------------------------
    # Parse JSON
    # --------------------------------------------------

    try:

        plan = json.loads(response)

    except json.JSONDecodeError:

        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            raise ValueError(
                "AI did not return a valid JSON analysis plan."
            )

        json_text = response[start:end + 1]

        try:

            plan = json.loads(json_text)

        except json.JSONDecodeError:

            raise ValueError(
                "AI returned an invalid JSON analysis plan."
            )

    # --------------------------------------------------
    # Validate required fields
    # --------------------------------------------------

    required_fields = [
        "group_column",
        "value_column",
        "operation"
    ]

    for field in required_fields:

        if field not in plan:

            raise ValueError(
                f"Analysis plan missing required field: {field}"
            )

    # --------------------------------------------------
    # Validate columns
    # --------------------------------------------------

    if plan["group_column"] not in dataset_columns:

        raise ValueError(
            f"Invalid group column: {plan['group_column']}"
        )

    if plan["value_column"] not in dataset_columns:

        raise ValueError(
            f"Invalid value column: {plan['value_column']}"
        )

    # --------------------------------------------------
    # Validate operation
    # --------------------------------------------------

    allowed_operations = [
        "mean",
        "sum",
        "count",
        "max",
        "min"
    ]

    if plan["operation"] not in allowed_operations:

        raise ValueError(
            f"Invalid operation: {plan['operation']}"
        )

    # --------------------------------------------------
    # IMPORTANT:
    # Enforce obvious metric intent
    # --------------------------------------------------

    if expected_value_column is not None:

        if expected_value_column in dataset_columns:

            plan["value_column"] = expected_value_column

    # --------------------------------------------------
    # Validate numeric column
    # --------------------------------------------------

    numeric_operations = [
        "mean",
        "sum",
        "max",
        "min"
    ]

    if plan["operation"] in numeric_operations:

        df = pd.read_csv(file_path)

        if not pd.api.types.is_numeric_dtype(
            df[plan["value_column"]]
        ):

            raise ValueError(
                f"Operation '{plan['operation']}' "
                f"requires a numeric column, "
                f"but '{plan['value_column']}' "
                f"is not numeric."
            )

    return plan