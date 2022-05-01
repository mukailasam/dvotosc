import matplotlib.pyplot as plt


plt.title("Figure 4: Hourly Correlation Coefficient Between TEC and Sunspot Numbers\nFrom January 2011 to December 2013.", y=-0.16, fontsize=5)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

y = [0.62, 0.68, 0.76, 0.72, 0.66, 0.49, 0.52, 0.92, 0.95, 0.84, 0.88, 0.84, 0.81, 0.82, 0.81, 0.77, 0.81, 0.81, 0.76, 0.53, 0.57, 0.60, 0.64, 0.69]

plt.plot(x, y,  marker="o")
plt.xlabel("TIME (LT)", fontsize=5)
plt.ylabel("r (S,T)")

plt.savefig("fig_4")
plt.show()