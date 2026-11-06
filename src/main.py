from pathlib import Path

from agent import run_agent


# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset path
file_path = PROJECT_ROOT / "data" / "Zomato_Dataset.csv"


question = "What is the lowest rating by city?"

answer = run_agent(
    question,
    str(file_path)
)

print("\n===== FINAL AI ANSWER =====")
print(answer)