import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(4, 3)
  

#plot 1

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [16.1, 11.7, 7.7, 4.5, 3.1, 4.2, 8.3, 14.5, 20.8, 25.7, 29.0, 30.9, 32.2, 33.3, 34.3, 34.7, 34.4,32.7, 26.8, 18, 13.0, 12.2, 12.8, 13.7]


axs[0, 0].set_ylabel("TEC")

axs[0, 0].plot(x, y, marker="o", label="January", linewidth=2.0, markersize=3.5, color="green")


fig.set_size_inches(20, 15)
axs[0,0].legend()




#plot 2

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [16.7, 12.5, 8.7, 5.7, 4.5, 6.0, 10.3, 16.9, 23.7, 29.2, 32.8, 35.1, 36.5, 37.1, 37.2, 37.2, 37.2, 35.4, 29.0, 20.0, 15.1, 14.3, 14.8, 15.4]

axs[0, 1].plot(x, y, marker="o", label="Febuary", linewidth=2.0, markersize=3.5)
fig.set_size_inches(20, 15)
axs[0,1].legend()


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [17.2, 13.2, 9.6, 7.0, 6.1, 8.0, 12.8, 20.0, 27.5, 33.7, 37.7, 39.9, 40.6, 40.6, 40.8, 41.5, 41.6, 39.4, 32.3, 23.2, 18.4, 17.2, 17.2, 17.3]

axs[0,2].plot(x, y, marker="o", label="March", linewidth=2.0, markersize=3.5)
fig.set_size_inches(20, 15)
axs[0,2].legend()


#plot 4

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [
17.2, 13.4, 10.0,7.5, 6.9, 9.0, 14.0, 21.4, 29.0, 34.9, 38.4, 40.0, 40.1, 40.2, 40.9, 42.0, 42.4, 40.0, 32.2, 23.0, 18.4, 17.2, 17.0, 17.0]

axs[1, 0].plot(x, y, marker="o", label="April", linewidth=2.0, markersize=3.5)
axs[1, 0].set_ylabel("TEC")
fig.set_size_inches(20, 15)
axs[1,0].legend()

#plot 5

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [14.9, 10.4, 7.1, 4.8, 4.4, 6.7, 11.9, 19.1, 26.2, 31.3, 33.9, 34.6, 34.6, 35.1, 36.2, 37.4, 37.9, 35.6, 28.1, 18.9, 14.2,13.0, 12.7, 12.8]

axs[1, 1].plot(x, y, marker="o", label="May", linewidth=2.0, markersize=3.5, color="black")
fig.set_size_inches(20, 15)
axs[1,1].legend()



# plot 6

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [10.2, 6.7, 3.6, 1.5, 1.3, 3.8, 9.1, 16.3, 23.1, 27.6, 29.5, 30.3, 31.2, 32.3, 33.7, 35.0, 35.2, 32.3, 24.2, 15.0, 10.6, 9.4, 9.1, 9.0]

axs[1, 2].plot(x, y, marker="o", label="June", linewidth=2.0, markersize=3.5, color="green")
fig.set_size_inches(20, 15)
axs[1,2].legend()

# plot 7

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [10.3, 7.0, 4.1, 2.2, 2.3, 5.0, 10.4, 17.3, 23.5, 27.6, 29.8, 31.3, 32.8, 34.2, 35.8, 37.0, 37.0, 33.8, 25.4, 16.3, 12.0, 10.5, 9.9, 9.6]

axs[2, 0].plot(x, y, marker="o", label="July", linewidth=2.0, markersize=3.5, color="blue")
axs[2, 0].set_ylabel("TEC")
fig.set_size_inches(20, 15)
axs[2,0].legend()

# plot 8

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [11.2, 8.0, 5.4, 3.8, 4.0, 6.6, 11.7, 18.1, 24.2, 29.1, 32.6, 35.2, 37.2, 38.8, 40.1, 40.8, 40.5, 36.5, 27.3, 18.0, 13.2, 11.7, 11.1, 10.6]

axs[2, 1].plot(x, y, marker="o", label="August", linewidth=2.0, markersize=3.5, color="red")
fig.set_size_inches(20, 15)
axs[2,1].legend()

# plot 9

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [12.4, 9.5, 7.0, 5.5, 5.5, 7.5, 12.2, 19.1, 27.0, 34.0, 39.0, 42.4, 44.4, 45.7, 46.6, 47.3, 46.2, 41.5, 31.5, 21.9, 17.0, 15.0, 13.7, 12.8]

axs[2, 2].plot(x, y, marker="o", label="September", linewidth=2.0, markersize=3.5, color="grey")
fig.set_size_inches(20, 15)
axs[2,2].legend()

# plot 10

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [12.8, 9.8, 7.3, 5.7, 5.6, 7.6, 12.1, 19.0,26.2, 32.4, 36.7, 39.6, 41.5, 43.0, 44.0, 44.6, 43.6, 38.9, 29.0, 19.7, 15.3, 13.7, 12.8, 12.1]

axs[3, 0].plot(x, y, marker="o", label="October", linewidth=2.0, markersize=3.5, color="purple")
axs[3, 0].set_ylabel("TEC")
axs[3, 0].set_xlabel("HOUR (LT)")
fig.set_size_inches(20, 15)
axs[3,0].legend()


#plot 11

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [13.9, 11.0, 8.3, 6.0, 5.3, 7.7, 14.0, 23.0, 32.3, 40.1, 45.6, 49.12, 51.4, 52.7, 53.4, 53.0, 51.0, 44.4, 33.0, 23.6, 19.1, 17.0, 15.5, 14.2]

axs[3, 1].plot(x, y, marker="o", label="November", linewidth=2.0, markersize=3.5, color="black")
axs[3, 1].set_xlabel("HOUR (LT)")
fig.set_size_inches(20, 15)
axs[3,1].legend()

axs[3, 0].set_title("Figure 4.1: Diurnal Variation in VTEC for Each Month During January-December 2011 at Zaria", y=-0.63, x=1.7, fontsize=25)



# plot 12

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [14.1, 11.0, 8.0, 5.4, 5.0, 8.0, 14.6, 23.5, 32.4, 39.4, 44.3, 47.4,49.2, 50.4, 51.1, 50.8, 48.7, 42.4, 31.3, 22.3, 18.1, 16.2, 15.0, 13.9]

axs[3, 2].plot(x, y, marker="o", label="December", linewidth=2.0, markersize=3.5, color="green")
axs[3, 2].set_xlabel("HOUR (LT)")
fig.set_size_inches(20, 15)
axs[3,2].legend()


plt.savefig("2011")

plt.show()