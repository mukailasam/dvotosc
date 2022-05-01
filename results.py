import matplotlib.pyplot as plt




# fig= plt.figure(figsize=(4,5))

plt.title("Figure 1: Diurnal Variation in TEC", y=-0.14 )

plt.rcParams["figure.figsize"] = (10, 7) 

time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

tec_1 = [13.9, 10.4, 7.2, 5.0, 4.5, 6.7, 11.8, 19.0, 26.3, 32.1, 35.8, 38.0, 39.3, 40.3, 41.2, 41.8, 41.3, 37.7, 29.2, 20.0, 15.4, 13.9, 13.5, 13.2]

tec_2 = [14.3, 11.0, 8.0, 5.9, 5.4, 7.6, 12.6, 20.0, 27.7, 34.0, 38.3, 41.0, 42.6, 43.7, 44.5, 44.8, 44.1, 40.1, 31.0, 21.6, 17.0, 15.4, 14.7, 14.2]

tec_3 = [15.1, 11.8, 8.9, 6.8, 6.4, 8.4, 13.4, 20.9, 28.9, 35.6, 40.3, 43.3, 45.0, 46.2, 46.9, 47.2, 46.3, 42.1, 32.8, 23.2, 18.4, 16.7, 15.9, 15.3]


plt.plot(time, tec_1, label="2011", marker="o", linewidth=5, markersize=10)
plt.plot(time, tec_2, label="2012", color="black", marker="o", linewidth=5, markersize=10)
plt.plot(time, tec_3, label="2013", color="green", marker="o", linewidth=5, markersize=10)
plt.legend()

plt.savefig("Figure_1")
plt.show()  
