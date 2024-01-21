#!/usr/bin/env python3
########################################################################
# Filename    : 
# Description : 
# Author      : 
########################################################################

import MPU6050 
import time
import numpy as np

mpu = MPU6050.MPU6050()     # instantiate a MPU6050 class object
accel = [0]*3               # define an arry to store accelerometer data
gyro = [0]*3                # define an arry to store gyroscope data

n_acquisizioni = 100

accel_x = np.array([0]*n_acquisizioni)
accel_y = np.array([0]*n_acquisizioni)
accel_z = np.array([0]*n_acquisizioni)


   
def setup():
    mpu.dmp_initialize()    # initialize MPU6050
    
def loop():
    while(True):
        angolo = input("Inserisci l'angolo: ")
        for i in range(n_acquisizioni):
            accel = mpu.get_acceleration()      # get accelerometer data
            accel_x[i] = accel[0]
            accel_y[i] = accel[1]
            accel_z[i] = accel[2]
            time.sleep(0.01)

        a_mean_x = np.mean(accel_x)
        a_mean_y = np.mean(accel_y)
        a_mean_z = np.mean(accel_z)
        
        a_std_x = np.std(accel_x)
        a_std_y = np.std(accel_y)
        a_std_z = np.std(accel_z)

        with open("data.dat", "a+") as file:
            file.write("==============================================\n")
            file.write(f"Angolo: {angolo}")
            file.write("a/g:%d\t%d\t%d \n"%(a_mean_x,a_mean_y,a_mean_z))
            file.write("a/g:%.5f g\t%.5f g\t%.5f g \n"%(a_mean_x/16384.0,a_mean_y/16384.0,
            a_mean_z/16384.0))
            file.write("a/g:%.5f g\t%.5f g\t%.5f g \n"%(a_std_x/16384.0,a_std_y/16384.0,
            a_std_z/16384.0))

        print("a/g:%d\t%d\t%d "%(a_mean_x,a_mean_y,a_mean_z))
        print("a/g:%.5f g\t%.5f g\t%.5f g "%(a_mean_x/16384.0,a_mean_y/16384.0,
            a_mean_z/16384.0))
        print("a/g:%.5f g\t%.5f g\t%.5f g "%(a_std_x/16384.0,a_std_y/16384.0,
            a_std_z/16384.0))

        
if __name__ == '__main__':     # Program entrance
    print("Program is starting ... ")
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass

