import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import nan
from getData import get_data
from meanData import mean_data
from MPU6050 import MPU6050 
import numpy as np

mpu = MPU6050.MPU6050()  


# Create figure for plotting
fig, axs = plt.subplots(3)

ys = [[nan], [nan], [nan]]
xs = [[nan], [nan], [nan]]

xrange = 50
start_time = time.time()

# This function is called periodically from FuncAnimation
def animate(i, ys, data=None):

    if data == "raw":
        read_data = get_data(log=False)
    elif data == "mean":
        read_data, _ = mean_data(log=False)
    else:
        raise ValueError("data should be 'raw' or 'mean'")
    
    for i in range(3):
        ys[i].append(read_data[i])
        xs[i].append(time.time()-start_time)
        ys[i] = ys[i][-xrange:]
        xs[i] = xs[i][-xrange:]
        axs[i].clear()
        axs[i].plot(xs[i], ys[i])
    for i in range(2):
        axs[i].set_xticks([])

    
    # Format plot
    axs[0].set(ylabel="a_x (g)")
    axs[1].set(ylabel="a_y (g)")
    axs[2].set(ylabel="a_z (g)", xlabel="time (s)")
    fig.suptitle(f'MPU6050 {data} Data')

# Set up plot to call animate() function periodically
def live_plot(data, sleep=10):
    ani = animation.FuncAnimation(fig, animate, fargs=(ys, data), interval=sleep)
    plt.show()

def setup():
    mpu.dmp_initialize()    # initialize MPU6050
            
if __name__ == '__main__':     # Program entrance
    print("Program is starting ... ")
    setup()
    live_plot(data="mean", sleep=10)
