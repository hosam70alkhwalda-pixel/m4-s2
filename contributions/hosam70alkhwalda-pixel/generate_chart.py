import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    sns.set_theme(style="whitegrid", palette="colorblind")


    df_full = pd.read_csv("full_dataset.csv")

 
    df = df_full.groupby("city")["revenue"].sum().reset_index()

    df = df[df["city"] != "Unknown"]
    df = df.sort_values(by="revenue", ascending=False)


    amman_revenue = df[df["city"] == "Amman"]["revenue"].values[0]
    total_revenue = df["revenue"].sum()
    amman_share = amman_revenue / total_revenue


    colors = ["#DD8452" if city == "Amman" else "#4C72B0" for city in df["city"]]

    plt.figure(figsize=(10,6))
    plt.bar(df["city"], df["revenue"], color=colors)

    for i, v in enumerate(df["revenue"]):
        plt.text(i, v, f"{int(v):,}", ha='center', va='bottom')

    plt.title(f"Amman Generates {amman_share:.0%} of Total Revenue", weight='bold')
    plt.xlabel("City")
    plt.ylabel("Revenue (JOD)")
    plt.xticks(rotation=30)

    plt.tight_layout()
    plt.savefig("chart.png", dpi=150, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    main()