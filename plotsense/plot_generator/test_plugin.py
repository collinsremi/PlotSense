import pandas as pd
from generator import PlotGenerator


df = pd.DataFrame({
    "age": [23, 45, 31, 22, 36, 28],
    "fare": [7.25, 71.83, 8.05, 8.05, 53.10, 8.05],
    "pclass": [3, 1, 3, 3, 1, 3]
})


suggestions = pd.DataFrame([
    {"plot_type": "heatmap", "variables": "age, fare, pclass"},   
    {"plot_type": "lineplot", "variables": "age, fare"}            
])

gen = PlotGenerator(df, suggestions)


print("\nTesting heatmap plugin...")
fig1 = gen.generate_plot(0)
if fig1:
    fig1.show()
    print("✅ Heatmap generated successfully.")


print("\nTesting lineplot plugin...")
fig2 = gen.generate_plot(1)
if fig2:
    fig2.show()
    print("✅ Lineplot generated successfully.")


input("\nPress Enter to exit...")
