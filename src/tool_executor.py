from data_profiler import profile_data
from data_quality import check_data_quality
from data_analyzer import analyze_data
from business_analysis import group_analysis


def execute_tool(tool_name, file_path, plan=None):

    if tool_name == "profile_data":

        return profile_data(file_path)

    elif tool_name == "check_data_quality":

        return check_data_quality(file_path)

    elif tool_name == "analyze_data":

        return analyze_data(file_path)

    elif tool_name == "group_analysis":

        if plan is None:
            raise ValueError("Analysis plan is required")

        return group_analysis(
            file_path,
            group_column=plan["group_column"],
            value_column=plan["value_column"],
            operation=plan["operation"],
            top_n=10
        )

    else:

        raise ValueError(f"Unknown tool: {tool_name}")