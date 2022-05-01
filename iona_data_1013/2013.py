import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(4, 3)

  
#plot 1

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [16.3, 12.2, 8.4, 5.4, 4.0, 5.1, 9.4, 16.5, 24.7, 32.0, 37.6, 41.5, 44.0, 45.4, 45.8, 45.6, 44.6, 41.6, 33.8, 24.1, 18.8, 17.5, 17.4, 17.6]

axs[0, 0].set_ylabel("TEC")
axs[0, 0].plot(x, y, marker="o", label="January", linewidth=2.0, markersize=3.5, color="green")

fig.set_size_inches(20, 15)
axs[0, 0].legend()

#plot 2

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [17.4, 13.3, 9.6, 6.6, 5.4, 6.6, 11.0, 17.9, 25.5, 32.0, 36.6, 39.7, 41.7, 43.0, 43.5, 43.3, 42.5, 39.9, 32.6, 23.3, 18.2, 17.0, 17.0, 17.3]

axs[0, 1].plot(x, y, marker="o", label="Febuary", linewidth=2.0, markersize=3.5)
fig.set_size_inches(20, 15)
axs[0,1].legend()

# plot 3


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [18.2, 14.4, 11.0, 8.3, 7.3, 9.0, 13.7, 21.1, 29.6, 37.1, 42.6, 45.8, 47.0, 47.1, 47.0, 47.1, 47.1, 44.5, 36.7, 27.0, 21.5, 20.0, 19.4, 19.2]

axs[0,2].plot(x, y, marker="o", label="March", linewidth=2.0, markersize=3.5, color="blue")
fig.set_size_inches(20, 15)
axs[0,2].legend()

#plot 4

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [18.6, 15.0, 11.8, 9.4, 8.8, 10.8, 16.0, 23.7, 32.3, 39.7, 44.7, 47.2, 47.9, 48.1, 48.5, 49.0, 48.7, 45.4, 37.0, 27.3, 22.3, 20.8, 20.2, 19.8]

axs[1, 0].plot(x, y, marker="o", label="April", linewidth=2.0, markersize=3.5, color="red")
axs[1, 0].set_ylabel("TEC")
fig.set_size_inches(20, 15)
axs[1,0].legend()

#plot 5

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [16.7, 13.4, 10.4, 8.4, 8.0, 10.3, 15.7, 23.7, 32.4, 39.6, 44.0, 46.1, 47.1, 48.0, 48.9, 49.4, 48.8, 45.0, 35.8, 26.0, 21.0, 19.2, 18.3, 17.6]

axs[1, 1].plot(x, y, marker="o", label="May", linewidth=2.0, markersize=3.5, color="black")
fig.set_size_inches(20, 15)
axs[1,1].legend()

# plot 6

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [13.0, 9.7, 6.8, 4.8, 4.5, 6.8, 12.2, 20.0, 28.0, 34.2, 37.8, 39.8, 41.0, 42.2, 43.3, 44.0, 43.5, 39.9, 30.7, 20.9, 16.0, 14.3, 13.5, 13.0]

axs[1, 2].plot(x, y, marker="o", label="June", linewidth=2.0, markersize=3.5, color="green")
fig.set_size_inches(20, 15)
axs[1,2].legend()

# plot 7

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [11.5, 8.3, 5.5, 3.8, 3.9, 6.5, 12.0, 19.6, 27.0, 32.6, 36.1, 38.2, 40.0, 41.3, 42.5, 43.3, 42.7, 38.6, 29.0, 19.6, 14.9, 13.1, 12.3, 11.6]

axs[2, 0].plot(x, y, marker="o", label="July", linewidth=2.0, markersize=3.5, color="blue")
axs[2, 0].set_ylabel("TEC")
fig.set_size_inches(20, 15)
axs[2,0].legend()

# plot 8

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [12.2, 9.3, 6.8, 5.4, 5.6, 8.2, 13.5, 20.6, 27.7, 33.6, 38.0, 41.1, 43.2, 44.7, 45.8, 46.2, 45.0, 40.2, 30.2, 20.7, 16.1, 14.3, 13.4, 12.5]

axs[2, 1].plot(x, y, marker="o", label="August", linewidth=2.0, markersize=3.5, color="red")
fig.set_size_inches(20, 15)
axs[2,1].legend()


# plot 9

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [13.0, 10.0, 7.5, 6.0, 6.2, 8.9, 14.0, 20.5, 27.1, 32.6, 36.6, 39.5, 41.5, 43.1, 44.0, 44.6, 43.6, 39.0, 29.0, 19.5, 15.2, 13.7, 13.0, 12.2]

axs[2, 2].plot(x, y, marker="o", label="September", linewidth=2.0, markersize=3.5, color="grey")
fig.set_size_inches(20, 15)
axs[2,2].legend()

# plot 10

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [13.9, 11.1, 8.8, 7.4, 7.5, 9.6, 14.2, 21.0, 28.7, 35.7, 40.8, 44.2, 46.4, 48.0, 48.8, 49.1, 47.7, 42.4, 32.0, 22.3, 17.7, 15.7, 14.5, 13.5]

axs[3, 0].plot(x, y, marker="o", label="October", linewidth=2.0, markersize=3.5, color="purple")
axs[3, 0].set_ylabel("TEC")
axs[3, 0].set_xlabel("HOUR (LT)")
fig.set_size_inches(20, 15)
axs[3,0].legend()

#plot 11

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [14.7, 12.0, 9.7, 8.1, 7.8, 9.5, 14.4, 22.0, 30.6, 38.0, 43.3, 46.8, 49.0, 50.4, 51.2, 51.2, 49.5, 43.7, 33.0, 23.4, 18.8, 16.7, 15.3, 14.2]

axs[3, 1].plot(x, y, marker="o", label="November", linewidth=2.0, markersize=3.5, color="black")
axs[3, 1].set_xlabel("HOUR (LT)")
fig.set_size_inches(20, 15)
axs[3,1].legend()

axs[3, 0].set_title("Figure 4.3: Diurnal Variation in VTEC for Each Month During January-December 2013 at Zaria", y=-0.63, x=1.7, fontsize=25)



# plot 12

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [15.5, 12.8, 10.2, 8.2, 7.4, 9.5, 15.2, 23.8, 33.0, 40.5, 45.9, 49.4, 51.5, 52.8, 53.5, 53.3, 51.3, 45.0, 33.9, 24.4, 19.8, 17.7, 16.2, 14.9]

axs[3, 2].plot(x, y, marker="o", label="December", linewidth=2.0, markersize=3.5, color="green")
axs[3, 2].set_xlabel("HOUR (LT)")
fig.set_size_inches(20, 15)
axs[3,2].legend()

plt.savefig("2013")

plt.show()