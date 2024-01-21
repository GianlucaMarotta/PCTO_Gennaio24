#!/usr/bin/env python3
########################################################################
# Filename    : getData.py
# Description : receive Data from MPU6050 sensor
# Author      : E.Giani, G. Marotta
########################################################################

from MPU6050 import MPU6050 
from livePlot import live_plot
import numpy as np
mpu = MPU6050.MPU6050()     # instantiate a MPU6050 class object


def setup():
    mpu.dmp_initialize()    # initialize MPU6050
            
if __name__ == '__main__':     # Program entrance
    print("Program is starting ... ")
    setup()
    live_plot(data="mean", sleep=0.1)
