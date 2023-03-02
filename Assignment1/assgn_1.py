#!/usr/bin/env python

"""
Manipulator simulation setup
@author: Bijo Sebastian, Durva Gaikwad
"""

#Import libraries
import time
import math
import random
#Import files
import sim_interface
import robot_params
import fw_kin

    
def main():
    if (sim_interface.sim_init()):

        #Obtain handles to sim elements
        sim_interface.get_handles()

        #Start simulation
        if (sim_interface.start_simulation()):
            
            #Exercise: Forward kinematics
            
            #Get random joint angle
            a = random.randint(0,360)
            b = random.randint(0,360)
            joint_angles = [a, b] #In degrees
            print("joint angles", joint_angles)
                        
            #Set joint angles 
            sim_interface.set_joint_position(joint_angles)
            time.sleep(0.5)
            
            #Obtain end effector position
            end_effector_position_sim = sim_interface.get_end_effector_position()
            
            #Compute end effector position analytically
            end_effector_position_analytic = fw_kin.fw_kin(joint_angles)                                  
            
            #Verify
            difference_norm = math.fabs(end_effector_position_analytic[0] - end_effector_position_sim[0]) + math.fabs(end_effector_position_analytic[1] - end_effector_position_sim[1]) 
            if difference_norm < 0.01:
                print("Exercise result: Success")
            else:
                print("Exercise result: Failed")
            
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
            

 
