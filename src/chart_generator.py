import matplotlib.pyplot as plt
import os


def create_bar_chart(
    results,
    title="Analysis Result",
    x_label="Category",
    y_label="Value",
    output_path="outputs/chart.png"
):

    categories = list(results.keys())
    values = list(results.values())

    plt.figure(figsize=(10, 6))

    plt.bar(categories, values)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    plt.savefig(output_path)

    plt.close()

    return output_path