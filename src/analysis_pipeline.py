from data_profiler import profile_data
from data_quality import check_data_quality
from data_analyzer import analyze_data


def run_analysis(file_path):

    print("\n================================")
    print("      DATA ANALYSIS PIPELINE")
    print("================================")

    print("\n[1] Profiling dataset...")

    profile = profile_data(file_path)

    print(f"Rows: {profile['rows']}")
    print(f"Columns: {profile['columns']}")
    print(f"Duplicate Rows: {profile['duplicate_rows']}")

    print("\n[2] Checking data quality...")

    quality = check_data_quality(file_path)

    print(f"Total Rows: {quality['total_rows']}")
    print(f"Total Columns: {quality['total_columns']}")

    print("\n[3] Running basic analysis...")

    analysis = analyze_data(file_path)

    print("\nAverage Values:")

    for column, value in analysis["average_values"].items():
        print(f"{column}: {value:.2f}")

    return {
        "profile": profile,
        "quality": quality,
        "analysis": analysis
    }