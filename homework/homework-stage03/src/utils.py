import pandas as pd
from pathlib import Path

def get_summary_stats(df, group_col=None):
    summary_stats = df.describe()
    grouped_stats = None
    if group_col and group_col in df.columns:
        num_cols = df.select_dtypes(include='number').columns
        grouped_stats = df.groupby(group_col)[num_cols].agg(['mean', 'median', 'std', 'count'])
    return summary_stats, grouped_stats

if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data" / "starter_data.csv"
    print("Reading:", data_path)

    df = pd.read_csv(data_path)
    s, g = get_summary_stats(df, group_col='category')
    print("\n=== Summary ===")
    print(s)
    print("\n=== Grouped by 'category' ===")
    print(g)