import math
import time

try:
  import sim
except:
  print ('--------------------------------------------------------------')
  print ('"sim.py" could not be imported. This means very probably that')
  print ('either "sim.py" or the remoteApi library could not be found.')
  print ('Make sure both are in the same folder as this file,')
  print ('or appropriately adjust the file "sim.py"')
  print ('--------------------------------------------------------------')
  print ('')

client_ID = []
goal_handles = []

def sim_init():
  global sim
  global client_ID
  
  #Initialize sim interface
  sim.simxFinish(-1) # just in case, close all opened connections
  client_ID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim    
  if client_ID!=-1:
    print ('Connected to remote API server')
    return True
  else:
    return False

def get_handles():
  #Get the handles to the sim items

  global joint_1_handle
  global joint_2_handle
  global end_effector_handle
  global goal_handles
  global link1_handle
  global link2_handle
  global wall_handle

  # Handle to joints, end effector, wall, and goal:
  res , joint_1_handle = sim.simxGetObjectHandle(client_ID, "/joint_1", sim.simx_opmode_blocking)
  res , joint_2_handle = sim.simxGetObjectHandle(client_ID, "/joint_2", sim.simx_opmode_blocking)
  res , end_effector_handle = sim.simxGetObjectHandle(client_ID, "/end_effector", sim.simx_opmode_blocking)
  res , link1_handle = sim.simxGetObjectHandle(client_ID, "/link1Respondable", sim.simx_opmode_blocking)
  res , link2_handle = sim.simxGetObjectHandle(client_ID, "/link2Respondable", sim.simx_opmode_blocking)
  res , wall_handle = sim.simxGetObjectHandle(client_ID, "/wall", sim.simx_opmode_blocking)

  res , temp_goal_handle = sim.simxGetObjectHandle(client_ID, "/goal_1", sim.simx_opmode_blocking)
  goal_handles.append(temp_goal_handle)
  res , temp_goal_handle = sim.simxGetObjectHandle(client_ID, "/goal_2", sim.simx_opmode_blocking)
  goal_handles.append(temp_goal_handle)
  res , temp_goal_handle = sim.simxGetObjectHandle(client_ID, "/goal_3", sim.simx_opmode_blocking)
  goal_handles.append(temp_goal_handle)

  # Get the position of the end effector for the first time in streaming mode
  res , end_effector_position = sim.simxGetObjectPosition(client_ID, end_effector_handle, -1 , sim.simx_opmode_streaming)
  
  # Get the position of the goal for the first time in streaming mode
  res , goal_position = sim.simxGetObjectPosition(client_ID, goal_handles[0], -1 , sim.simx_opmode_streaming)
  res , goal_position = sim.simxGetObjectPosition(client_ID, goal_handles[1], -1 , sim.simx_opmode_streaming)
  res , goal_position = sim.simxGetObjectPosition(client_ID, goal_handles[2], -1 , sim.simx_opmode_streaming)
  
  # Set all joints to zero to ensure manipulator is starting configuration
  res = sim.simxSetJointTargetPosition(client_ID, joint_1_handle, 0, sim.simx_opmode_streaming)
  res = sim.simxSetJointTargetPosition(client_ID, joint_2_handle, 0, sim.simx_opmode_streaming)
  
  # Set all joint rates to zero to ensure manipulator is starting configuration
  #res = sim.simxSetJointTargetVelocity(client_ID, joint_1_handle, 0, sim.simx_opmode_streaming)
  #res = sim.simxSetJointTargetVelocity(client_ID, joint_2_handle, 0, sim.simx_opmode_streaming)
  
  #Do collission checks
  res, collisionState1 = sim.simxCheckCollision(client_ID, link1_handle, wall_handle, sim.simx_opmode_streaming )
  res, collisionState2 = sim.simxCheckCollision(client_ID, link2_handle, wall_handle, sim.simx_opmode_streaming )

  print ("Succesfully obtained handles")

  return

def start_simulation():
  global sim
  global client_ID

  ###Start the Simulation: Keep printing out status messages!!!
  res = sim.simxStartSimulation(client_ID, sim.simx_opmode_oneshot_wait)

  if res == sim.simx_return_ok:
    print ("---!!! Started Simulation !!! ---")
    return True
  else:
    return False

def get_joint_position():
  #Function that will return the current joint angles
  #PS. THE ORIENTATION WILL BE RETURNED IN RADIANS        
  global sim
  global client_ID
  global joint_1_handle
  global joint_2_handle
  
  res , joint_1_position = sim.simxGetJointPosition(client_ID, joint_1_handle, sim.simx_opmode_blocking)
  res , joint_2_position = sim.simxGetJointPosition(client_ID, joint_2_handle, sim.simx_opmode_blocking)
  
  print("current joint positions", joint_1_position, joint_2_position)

  return [joint_1_position, joint_2_position]       

def set_joint_position(joint_angles):
  #Function to set the joint angles
  global sim
  global client_ID
  global joint_1_handle
  global joint_2_handle
 
  # Convert to radians
  joint_amgles_in_rad = [0,0]
  joint_amgles_in_rad[0] = joint_angles[0]*(3.14/180)
  joint_amgles_in_rad[1] = joint_angles[1]*(3.14/180)
  
  # Set position
  sim.simxSetJointTargetPosition(client_ID, joint_1_handle, joint_amgles_in_rad[0], sim.simx_opmode_oneshot_wait)
  sim.simxSetJointTargetPosition(client_ID, joint_2_handle, joint_amgles_in_rad[1], sim.simx_opmode_oneshot_wait)
  
  return  

def get_end_effector_position():
  #Function that will return the goal pose
  #PS. THE ORIENTATION WILL BE RETURNED IN RADIANS        
  global sim
  global client_ID
  global end_effector_handle
  
  #Obtain goal position
  res , end_effector_position = sim.simxGetObjectPosition(client_ID, end_effector_handle, -1 , sim.simx_opmode_buffer)
  
  print("End effector position (simulation)", end_effector_position[0], end_effector_position[1])
  return [end_effector_position[0], end_effector_position[1]]    

def get_goal_position(id):
  #Function that will return the goal pose
  #PS. THE ORIENTATION WILL BE RETURNED IN RADIANS        
  global sim
  global client_ID
  global goal_handles
  
  if id > 3:
      print("Goal ID out of range")
      return
  
  #Obtain goal position
  res , goalPosition = sim.simxGetObjectPosition(client_ID, goal_handles[id-1], -1 , sim.simx_opmode_buffer)
  
  print("current goal position", goalPosition[0], goalPosition[1])

  return [goalPosition[0], goalPosition[1]]    

def sim_shutdown():
  #Gracefully shutdown simulation

  global sim
  global client_ID

  #Stop simulation
  res = sim.simxStopSimulation(client_ID, sim.simx_opmode_oneshot_wait)
  if res == sim.simx_return_ok:
    print ("---!!! Stopped Simulation !!! ---")

  # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
  sim.simxGetPingTime(client_ID)

  # Now close the connection to CoppeliaSim:
  sim.simxFinish(client_ID)      

  return           

def collission_check():
    #Check collission between links and wall
    global link1_handle
    global link2_handle
    global wall_handle
    res, collisionState1 = sim.simxCheckCollision(client_ID, link1_handle, wall_handle, sim.simx_opmode_buffer)
    res, collisionState2 = sim.simxCheckCollision(client_ID, link2_handle, wall_handle, sim.simx_opmode_buffer)
    if collisionState1 or collisionState2:
        return True
    else:
        return False
                
