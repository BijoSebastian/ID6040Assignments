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
import kinematics_helper_functions
   
def at_goal(goal_position):
    #Check if manipulator end effector has reached goal location given in m
   
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
            #Starting at goal 2, move the manipulator end effector along global x axis at a speed of 0.01m/s to reach Goal 
            
            #Obtain goal position
            goal_position = sim_interface.get_goal_position(3)
                  
            while not at_goal(goal_position):
                current_joint_angles = sim_interface.get_joint_position()
                desired_joint_angle_rates = kinematics_helper_functions.get_desired_joint_rate(current_joint_angles)                
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
            

 
