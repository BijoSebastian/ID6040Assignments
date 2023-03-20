#Import libraries
import time
import math

#Import files
import sim_interface
import inv_kin


def main():
    if (sim_interface.sim_init()):

        #Obtain handles to sim elements
        sim_interface.get_handles()

        #Start simulation
        if (sim_interface.start_simulation()):
            
            #Exercise 2
            #Inverse kinematics 
            for i in range(3):
                print("Goal ", i+1)
            
                #Obtain goal position
                goal_position = sim_interface.get_goal_position(i+1)
            
                #Compute joint angles to get to desired position
                joint_angles = inv_kin.inv_kin_fn(goal_position)
            
                #Set joint angles 
                sim_interface.set_joint_position(joint_angles)
                time.sleep(0.5)
            
                #Obtain end effector position
                end_effector_position = sim_interface.get_end_effector_position()            
                
                #Verify
                difference_norm = math.fabs(goal_position[0] - end_effector_position[0]) + math.fabs(goal_position[1] - end_effector_position[1]) 
                if difference_norm < 0.01:
                    print("Exercise 2 result: Success")
                else:
                    print("Exercise 2 result: Failed")
                    
            
        
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
            

 