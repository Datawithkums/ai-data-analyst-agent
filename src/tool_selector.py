from llm_client import ask_llm


def choose_tool(question):

    prompt = f"""
You are an AI Data Analyst Agent.

Available tools:

1. profile_data
   - Understand the structure of the dataset.

2. check_data_quality
   - Check missing values, duplicates, unique values,
     numeric columns and categorical columns.

3. analyze_data
   - Calculate overall numeric summaries, averages,
     minimums and maximums.

4. group_analysis
   - Compare a numeric metric across categories.
   - Example: average Rating by City.
   - Example: average Votes by City.

User question:

{question}

Choose the most appropriate tool.

Return ONLY the tool name.
"""

    response = ask_llm(prompt).strip()

    if "profile_data" in response:
        return "profile_data"

    elif "check_data_quality" in response:
        return "check_data_quality"

    elif "analyze_data" in response:
        return "analyze_data"

    elif "group_analysis" in response:
        return "group_analysis"

    else:
        raise ValueError(f"AI selected an unknown tool: {response}")