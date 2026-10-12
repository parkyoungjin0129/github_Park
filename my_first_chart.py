import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"   #윈도우는Malgun Gothic

prices = [60000, 47300, 52600, 8280, 49600]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(prices)
for i, p in enumerate(prices):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
        xytext=(0, 8), ha="center")

ax.set_title("내 지출 그래프")
fig.savefig("my_first_chart.png")