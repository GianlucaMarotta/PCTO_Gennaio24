#!/usr/bin/env python3
########################################################################
# Filename    : getData.py
# Description : receive Data from MPU6050 sensor
# Author      : E.Giani, G. Marotta
########################################################################

from MPU6050 import MPU6050 
import time
import numpy as np


mpu = MPU6050.MPU6050()     # instantiate a MPU6050 class object
accel = [0]*3               # define an arry to store accelerometer data
gyro = [0]*3                # define an arry to store gyroscope data

def get_data(log=True):
    raw_accel = np.array(mpu.get_acceleration())      # get accelerometer data
    accel = raw_accel/16384.0
    if log is True:
        print(f"Raw data: a_x: {raw_accel[0]}, a_y: {raw_accel[1]}, a_z: {raw_accel[2]}")
        print(f"Accelerations: a_x: {accel[0]} g, a_y: {accel[1]} g, a_z: {accel[2]} g")

    return accel


def setup():
    mpu.dmp_initialize()    # initialize MPU6050
    
def loop():
    while(True):
        get_data()
        time.sleep(0.5)

        
if __name__ == '__main__':     # Program entrance
    print("Program is starting ... ")
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
