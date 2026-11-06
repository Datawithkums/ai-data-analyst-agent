from tool_selector import choose_tool
from tool_executor import execute_tool
from llm_client import ask_llm
from analysis_planner import create_analysis_plan
import pandas as pd
from chart_generator import create_bar_chart


def run_agent(question, file_path):

    print("\n===== USER QUESTION =====")
    print(question)

    # Step 1: Choose the tool
    tool = choose_tool(question)

    print("\n===== SELECTED TOOL =====")
    print(tool)

    # Step 2: Create analysis plan for group analysis
    if tool == "group_analysis":

        # Load dataset and get actual column names
        df = pd.read_csv(file_path)

        dataset_columns = df.columns.tolist()

        try:

            plan = create_analysis_plan(
                question,
                dataset_columns,
                file_path
            )

        except ValueError as error:

            return f"""
        I cannot perform this analysis.

        Reason:
        {error}

        Please choose a numeric column for this operation.
        """
        print("\n===== ANALYSIS PLAN =====")
        print(plan)

        result = execute_tool(
            tool,
            file_path,
            plan
        )
        chart_path = create_bar_chart(
            result["top_results"],
            title=f"{plan['operation'].title()} {plan['value_column']} by {plan['group_column']}",
            x_label=plan["group_column"],
            y_label=plan["value_column"]
        )

        print("\n===== CHART =====")
        print(f"Chart created: {chart_path}")

    else:

        result = execute_tool(
            tool,
            file_path
        )

    print("\n===== TOOL RESULT =====")
    print(result)

    # Step 3: AI interprets the result
    prompt = f"""
You are a professional Data Analyst.

User question:
{question}

Tool used:
{tool}

Tool result:
{result}

IMPORTANT RULES:

1. Use ONLY the information provided in the Tool result.
2. NEVER change, remove, reorder, or invent any result.
3. If the Tool result contains multiple results, report ALL of them.
4. Preserve the ranking and values exactly as provided by the Tool result.
5. Do not calculate new values unless necessary.
6. Do not invent business meaning.
7. Do not claim that data is accurate, complete, or high quality unless the Tool result explicitly provides evidence.
8. Do not make unsupported data-quality observations.
9. Never assume currency, location meaning, or business meaning.
10. Keep the answer concise and business-focused.

For ranking questions:
- Show every result returned by the tool.
- Preserve the exact ranking order.
- Do not skip results.

Provide:

Direct Answer:
List the results from the tool.

Key Insights:
Explain only what can be directly observed from the results.

Data Quality:
Mention only an actual data-quality issue present in the tool result.
If there is no evidence of a data-quality issue, say:
"No specific data-quality issue was identified from this analysis."
"""

    answer = ask_llm(prompt)

    return answer