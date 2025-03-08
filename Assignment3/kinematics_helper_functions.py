# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:51:21 2023

@author: Bijo Sebastian
"""
import numpy as np
import math
import robot_params

def get_desired_joint_rate(joint_angles):
    
    #Compute 2x2 jacobian matrix for given joint angles [in radians] 
    j11 = 
    j12 = 
    j21 = 
    j22 = 
    jacobian  = np.array([[j11, j12], [j21, j22]])
    
    #Compute desired joint angle rate by inverting jacobian and multiplying with desired end effector velocity
    desired_end_effector_velocity = np.array([[0.01], [0.0]])
    desired_joint_angle_rates = 
    
    return [desired_joint_angle_rates[0], desired_joint_angle_rates[1]]
