import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

starttime = '2024-01-01'

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {"format": "csv", "starttime": starttime, "minmagnitude": 4.5}
df = pd.read_csv(url + "?" + "&".join(f"{k}={v}" for k, v in params.items()),
                 parse_dates=["time"])

df = df.sort_values("time")

sns.set_theme(style="darkgrid", context="talk", palette="deep")
fig, ax = plt.subplots(figsize=(12, 5.5))
sns.scatterplot(
    data=df,
    x="time",
    y="mag",
    hue="mag",
    palette="magma",
    size="mag",
    sizes=(15, 120),
    alpha=0.75,
    edgecolor="white",
    linewidth=0.35,
    legend=False,
    ax=ax,
)
ax.set_xlabel("Time")
ax.set_ylabel("Magnitude")
ax.set_title("USGS earthquakes (M ≥ 4.5) since 2024-01-01")
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
fig.autofmt_xdate()
plt.tight_layout()
# fig.savefig(f"plot-{starttime}.png", dpi=150)
plt.show()
