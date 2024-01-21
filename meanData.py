#!/usr/bin/env python3
########################################################################
# Filename    : getData.py
# Description : receive Data from MPU6050 sensor
# Author      : E.Giani, G. Marotta
########################################################################

from MPU6050 import MPU6050 
import time
import numpy as np
from getData import get_data

mpu = MPU6050.MPU6050()     # instantiate a MPU6050 class object
accel = [0]*3               # define an arry to store accelerometer data
gyro = [0]*3                # define an arry to store gyroscope data

n_acq = 1000
accel_x = [0]*n_acq
accel_y = [0]*n_acq
accel_z = [0]*n_acq
mean = [0]*3
std = [0]*3


def mean_data(log=True):
    
    for i in range(n_acq):
        accel = get_data(log=False)
        accel_x[i] = accel[0]
        accel_y[i] = accel[1]
        accel_z[i] = accel[2]

    mean[0] = np.mean(accel_x)
    mean[1] = np.mean(accel_y)
    mean[2] = np.mean(accel_z)
    
    std[0] = np.std(accel_x)
    std[1] = np.std(accel_y)
    std[2] = np.std(accel_z)

    if log is True:
        print(f"Mean data: a_x: {mean[0]}, a_y: {mean[1]}, a_z: {mean[2]}")
        print(f"Data std: a_x: {std[0]}, a_y: {std[1]}, a_z: {std[2]}")

    return mean, std

def setup():
    mpu.dmp_initialize()    # initialize MPU6050
    
def loop():
    while(True):
        mean_data()
        time.sleep(0.1)

        
if __name__ == '__main__':     # Program entrance
    print("Program is starting ... ")
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass

