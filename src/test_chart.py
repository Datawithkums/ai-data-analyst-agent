from chart_generator import create_bar_chart


results = {
    "New Delhi": 5473,
    "Gurgaon": 1118,
    "Noida": 1080,
    "Faridabad": 251,
    "Ghaziabad": 25
}


chart = create_bar_chart(
    results,
    title="Top Cities by Restaurant Count",
    x_label="City",
    y_label="Restaurant Count"
)

print(f"Chart created: {chart}")