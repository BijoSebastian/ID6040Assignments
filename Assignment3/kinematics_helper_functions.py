# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:51:21 2023

@author: Bijo Sebastian
"""
import numpy as np
import math
import robot_params

def inv_kin(goal_position):
    #Compute inverse kinematics function for 2 link manipulator
    #Goal position given in m
    #Return joint angles in radians

    #Fill here
    return [theta_1, theta_2]
    
def get_desired_joint_rate(joint_angles):
    #Compute joint angle rate in rad/sec to achieve effector velocity along global x axis of 0.01m/s
    
    desired_end_effector_velocity = np.array([[0.01], [0.0]])
    desired_joint_angle_rates = 

    #Fill here
    return [desired_joint_angle_rates[0], desired_joint_angle_rates[1]]
