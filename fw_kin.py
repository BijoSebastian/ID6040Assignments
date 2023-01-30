import math
import robot_params

def fw_kin(joint_angles):
    #Compute end effector position [in meters] for the given pair of joint angles [in degrees] 
    
    ### Fill this part ###
    #Hint: see file robot_params for link lengths
    end_effector_position_analytic = [x_end_effector, y_end_effector]
    
    print("End effector position (analytic)", end_effector_position_analytic)
    return end_effector_position_analytic