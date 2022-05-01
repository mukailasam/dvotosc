import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(4, 3)

  
#plot 1

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [15.9,11.7, 7.7, 4.7, 3.3, 4.5, 8.9, 15.8, 23.4, 30.1, 35.3, 39.00, 41.3, 42.5, 43.0, 42.7, 41.6, 39.1, 32.0, 22.7, 17.6, 16.4, 16.5, 16.7]


axs[0, 0].set_ylabel("TEC")
axs[0, 0].plot(x, y, marker="o", label="January", linewidth=2.0, markersize=3.5, color="green")

fig.set_size_inches(20, 15)
axs[0, 0].legend()

#plot 2

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [17.0, 12.9, 9.1, 6.1, 5.0, 6.3, 10.7,17.4, 24.6, 30.6, 34.8, 37.3, 38.8, 39.6, 39.8, 39.6, 39.3, 37.4, 30.6, 21.3, 16.5, 15.4, 15.5, 16.0]

axs[0, 1].plot(x, y, marker="o", label="Febuary", linewidth=2.0, markersize=3.5)
fig.set_size_inches(20, 15)
axs[0,1].legend()

# plot 3


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [17.7, 13.9, 10.4, 7.8, 7.0, 8.7, 13.5, 21.1, 29.5, 36.7, 41.5, 44.1, 45.0, 45.4, 45.5, 46.0, 46.3, 43.7, 35.9, 26.1, 21.0, 19.5, 19.1, 18.9]

axs[0,2].plot(x, y, marker="o", label="March", linewidth=2.0, markersize=3.5, color="blue")
fig.set_size_inches(20, 15)
axs[0,2].legend()

#plot 4

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [17.9, 14.2, 10.8, 8.4, 7.8, 9.8, 14.9, 22.3, 30.2, 36.5, 40.6, 42.5, 43.1, 43.3, 43.6, 44.2, 44.4, 41.7, 33.9, 24.7, 19.8, 18.4, 18.0, 17.9]

axs[1, 0].plot(x, y, marker="o", label="April", linewidth=2.0, markersize=3.5, color="red")
axs[1, 0].set_ylabel("TEC")
fig.set_size_inches(20, 15)
axs[1,0].legend()

#plot 5

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [14.8, 11.2, 8.1, 6.0, 5.6, 8.0, 13.3, 21.0, 29.1, 35.4, 39.0, 40.5, 41.3, 42.3, 43.4, 44.2, 44.0, 40.5, 31.8, 22.3, 17.6, 16.1, 15.5, 15.1]

axs[1, 1].plot(x, y, marker="o", label="May", linewidth=2.0, markersize=3.5, color="black")
fig.set_size_inches(20, 15)
axs[1,1].legend()

# plot 6

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [11.0, 7.7, 4.7, 2.7, 2.7,5.3, 10.8, 18.4, 25.7, 30.9, 33.6, 35.0, 36.1, 37.5, 38.9, 39.9, 39.5, 35.8, 26.9, 17.3, 12.8, 11.4, 11.0, 10.6]

axs[1, 2].plot(x, y, marker="o", label="June", linewidth=2.0, markersize=3.5, color="green")
fig.set_size_inches(20, 15)
axs[1,2].legend()

# plot 7

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [11.0, 7.7, 5.0, 3.2, 3.4, 6.9, 11.6, 18.9, 26.0, 31.4, 35.2, 37.6, 39.2, 40.6, 41.6, 42.2, 41.8, 37.7, 28.2, 18.7, 14.1, 12.4, 11.7, 11.1]

axs[2, 0].plot(x, y, marker="o", label="July", linewidth=2.0, markersize=3.5, color="blue")
axs[2, 0].set_ylabel("TEC")
fig.set_size_inches(20, 15)
axs[2,0].legend()

# plot 8

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [11.6, 8.5, 6.0, 4.5, 4.7, 7.4, 12.7, 19.5, 26.1, 31.5, 35.4, 38.3, 40.2, 41.6, 42.8, 43.3, 42.5, 38.1, 28.2, 19.0, 14.5,13.0, 12.1, 11.4]

axs[2, 1].plot(x, y, marker="o", label="August", linewidth=2.0, markersize=3.5, color="red")
fig.set_size_inches(20, 15)
axs[2,1].legend()


# plot 9

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [12.6, 9.7, 7.3, 5.9, 6.1, 8.5, 13.3, 19.9, 27.2, 33.6, 38.3, 41.6, 43.8, 45.4, 46.4, 46.8, 45.5, 40.5,30.3, 20.8, 16.2, 14.4, 13.3, 12.5]

axs[2, 2].plot(x, y, marker="o", label="September", linewidth=2.0, markersize=3.5, color="grey")
fig.set_size_inches(20, 15)
axs[2,2].legend()

# plot 10

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [13.5, 10.7, 8.4, 6.9, 6.8, 8.7, 13.3, 20.4, 28.4, 35.5, 40.7, 44.1, 46.3, 47.5, 48.2, 48.3, 47.0, 41.7, 31.3, 21.8, 17.3, 15.4, 14.2, 13.2]

axs[3, 0].plot(x, y, marker="o", label="October", linewidth=2.0, markersize=3.5, color="purple")
axs[3, 0].set_ylabel("TEC")
axs[3, 0].set_xlabel("HOUR (LT)")
fig.set_size_inches(20, 15)
axs[3,0].legend()

#plot 11

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [14.2, 11.5, 9.1, 7.2, 6.7, 8.8, 14.1, 22.2, 31.0, 38.2, 43.4, 46.6, 48.7, 50.2, 51.0, 50.9, 49.0, 43.0, 32.1, 22.8, 18.3, 16.3, 15.0, 13.8]

axs[3, 1].plot(x, y, marker="o", label="November", linewidth=2.0, markersize=3.5, color="black")
axs[3, 1].set_xlabel("HOUR (LT)")
fig.set_size_inches(20, 15)
axs[3,1].legend()

axs[3, 0].set_title("Figure 4.2: Diurnal Variation in VTEC for Each Month During January-December 2012 at Zaria", y=-0.63, x=1.7, fontsize=25)



# plot 12

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [14.6, 11.8, 9.1, 7.0, 6.3, 8.6, 14.4, 22.7, 31.0, 37.7, 42.4, 45.1, 47.2, 48.4, 49.2, 49.2, 47.7, 42.0, 31.3,22.1, 17.7, 15.8, 14.7, 13.7]

axs[3, 2].plot(x, y, marker="o", label="December", linewidth=2.0, markersize=3.5, color="green")
axs[3, 2].set_xlabel("HOUR (LT)")
fig.set_size_inches(20, 15)
axs[3,2].legend()

plt.savefig("2012")

plt.show()