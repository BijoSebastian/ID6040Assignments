# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 12:01:49 2023

@author: Bijo Sebastian
"""

import math
import numpy
import robot_params

def inv_kin_fn(goal_position):
    #Compute joint angles [in degrees] to reach desired position [in meters] 
    x_desired = goal_position[0]
    y_desired = goal_position[1]

    ### Fill this part ###

    print("Desired joint angles",[theta_1, theta_2])
    return [theta_1, theta_2]