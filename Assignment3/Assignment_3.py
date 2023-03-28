#!/usr/bin/env python

"""
Manipuator simulation setup
@author: Bijo Sebastian 
"""

#Import libraries
import time
import math
import numpy as np

#Import files
import sim_interface
import robot_params
import differential_kinematics

def inv_kin(goal_position):
    #Inverse kinematics function for 2 link manipulator 
    x_desired = goal_position[0]
    y_desired = goal_position[1]
    
    cos_theta_2 = (x_desired*x_desired + y_desired*y_desired - robot_params.link_1_length*robot_params.link_1_length - robot_params.link_2_length*robot_params.link_2_length) / (2*robot_params.link_1_length*robot_params.link_2_length)
    sin_theta_2 = math.sqrt(1 - (cos_theta_2*cos_theta_2))
    theta_2 = math.atan2(sin_theta_2, cos_theta_2)
   
    M = robot_params.link_1_length + robot_params.link_2_length*cos_theta_2
    N = robot_params.link_2_length*sin_theta_2
    
    theta_1 =  math.atan2(y_desired , x_desired) - math.atan2(N, M)
  
    print("Desired joint angles",[theta_1, theta_2])
    return [theta_1, theta_2]
    
def at_goal(goal_position):
    #Check if manipulator end effector has reached goal location 
    #Obtain end effector position
    end_effector_position = sim_interface.get_end_effector_position()            
    
    #Verify
    difference_norm = math.fabs(goal_position[0] - end_effector_position[0]) + math.fabs(goal_position[1] - end_effector_position[1]) 
    if difference_norm < 0.1:
        print("Exercise 3 result: Success")
        return True
    else:
        return False
    
def main():
    if (sim_interface.sim_init()):

        #Obtain handles to sim elements
        sim_interface.get_handles()

        #Start simulation
        if (sim_interface.start_simulation()):
            
            #Exercise 3
            
            #Starting at goal 2, move the manipulator end effecot along global x axis at a speed of 0.01m/s to reach Goal 3
            
            #Obtain goal_3 position
            goal_position = sim_interface.get_goal_position(3)
                  
            while not at_goal(goal_position):
                current_joint_angles = sim_interface.get_joint_position()
                desired_joint_angle_rates = differential_kinematics.get_desired_joint_rate(current_joint_angles)                
                print("Joint angle rates", desired_joint_angle_rates)
                sim_interface.set_joint_velocity(desired_joint_angle_rates)
                time.sleep(0.1)
                
        else:
            print ('Failed to start simulation')
    else:
        print ('Failed connecting to remote API server')
    
    #Stop simulation
    sim_interface.sim_shutdown()
    time.sleep(0.5)
    return

#run
if __name__ == '__main__':

    main()                    
    print ('Program ended')
            

 