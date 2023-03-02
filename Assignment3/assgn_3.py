#!/usr/bin/env python

"""
Manipuator simulation setup
@author: Bijo Sebastian 
"""

#Import libraries
import time
import math

#Import files
import sim_interface
import robot_params

def inv_kin(goal_position):
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

def get_path(joint_angles_1, joint_angles_2):
    #Get path [in radians] that goes from current to new goal while avoiding obstacle (wall)
    joint_angles = [joint_angles_1]
    divisions = 10
    theta_1_increment = (joint_angles_2[0] - joint_angles_1[0])/divisions
    theta_2_increment = (joint_angles_2[1] - joint_angles_1[1])/divisions
    for i in range(0,divisions,1):
        joint_angles.append([joint_angles_1[0] + (theta_1_increment*(i+1)), joint_angles_1[1] + (theta_2_increment*(i+1))])
    
    print ("path", joint_angles)
    return joint_angles

def get_jacobian(joint_angles):
    #Get 2x2 jacobian matrix for given joint angles [in radians] 
    
   
    
    print("Jacobian", jacobian)
    return jacobian
    
def main():
    if (sim_interface.sim_init()):

        #Obtain handles to sim elements
        sim_interface.get_handles()

        #Start simulation
        if (sim_interface.start_simulation()):
            
            #Exercise 3
            
            #Start at goal 2 
            goal_position = sim_interface.get_goal_position(2)
            #Compute joint angles to get to desired position
            joint_angles = inv_kin(goal_position)
            #Set joint angles 
            sim_interface.set_joint_position(joint_angles)
            time.sleep(0.5)
            
            #Move the manipulator along global x axis for 0.5m to reach goal 3
            
            #Obtain goal_3 position
            goal_position = sim_interface.get_goal_position(3)
                        
            for i in range(1,50,1):
                desired_joint_angles = []
                current_joint_angles = sim_interface.get_joint_position()
                jacobian = get_jacobian(current_joint_angles)
                joint_angle_rates = np.matmul(np.linalg.inv(jacobian),np.array([[0.01], [0.0]]))
                print("Joint angle rates", joint_angle_rates)
                desired_joint_angles.append(current_joint_angles[0] + joint_angle_rates[0,0])
                desired_joint_angles.append(current_joint_angles[1] + joint_angle_rates[1,0])
                sim_interface.set_joint_position(desired_joint_angles)
                time.sleep(0.1)
                
            #Obtain end effector position
            end_effector_position = sim_interface.get_end_effector_position()            
            
            #Verify
            difference_norm = math.fabs(goal_position[0] - end_effector_position[0]) + math.fabs(goal_position[1] - end_effector_position[1]) 
            if difference_norm < 0.1:
                print("Exercise 3 result: Success")
            else:
                print("Exercise 3 result: Failed")
                return

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
            

 
