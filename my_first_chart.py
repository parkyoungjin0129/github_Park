import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"   #윈도우는Malgun Gothic

prices = [59000, 47300, 62600, 82800, 39600]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(prices)
for i, p in enumerate(prices):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
        xytext=(0, 8), ha="center")

ax.set_title("내첫그래프")
fig.savefig("my_first_chart.png")