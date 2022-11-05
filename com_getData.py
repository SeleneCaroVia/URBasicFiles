# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 12:47:32 2019
Document to receive data from the robot. To launch the server, you must follow:
1. ctrl + alt + f1
2. user = root
3. Password = easybot
4. cd /etc/init.d
5. ./ur_server start
6. ifconfig (to know the ip of the robot)
In your computer connect to the wifi called dd-wrt which password is ur_hack_la_salle
@author: Selene Caro Via
"""

import socket
import time
from UR import com_URScript as script

PORT = 30100
PORT2 = 30101
NAME_FILE = "./UR/ask_info.script"

##########################
#Available commands
##########################
TIMESTAMP = "timestamp"
TARGET_Q = "target_q"
TARGET_QD = "target_qd"
TARGET_GDD = "target_qdd"
TARGET_CURRENT = "target_current"
TARGET_MOMENT = "target_moment"
ACTUAL_Q = "actual_q"
ACTUAL_QD = "actual_qd"
ACTUAL_CURRENT = "actual_current"
JOINT_CONTROL_OUTPUT = "joint_control_output"
ACTUAL_TCP_POSE = "actual_TCP_pose"
ACTUAL_TCP_SPEED = "actual_TCP_speed"
ACTUAL_TCP_FORCE = "actual_TCP_force"
TARGET_TCP_POSE = "target_TCP_pose"
TARGET_TCP_SPEED = "target_TCP_speed"
ACTUAL_DIGITAL_INPUT_BITS = "actual_digital_input_bits"
JOINT_TEMPERATURES = "joint_temperatures"
ACTUAL_EXECUTION_TIME = "actual_execution_time"
ROBOT_MODE = "robot_mode"
JOINT_MODE = "joint_mode"
SAFETY_MODE = "safety_mode"
ACTUAL_TOOL_ACCELEROMETER = "actual_tool_accelerometer"
SPEED_SCALING = "speed_scaling"
TARGET_SPEED_FRACTION = "target_speed_fraction"
ACTUAL_MOMENTUM = "actual_momentum"
ACTUAL_MAIN_VOLTAGE = "actual_main_voltage"
ACTUAL_ROBOT_VOLTAGE = "actual_robot_voltage"
ACTUAL_ROBOT_CURRENT = "actual_robot_current"
ACTUAL_JOINT_VOLTAGE = "actual_joint_voltage"
ACTUAL_DIGITAL_OUTPUT_BITS = "actual_digital_output_bits"
RUNTIME_STATE = "runtime_state"
SAFETY_STATUS_BITS = "safety_status_bits"
ROBOT_STATUS_BITS = "robot_status_bits"
GET_ALL_JOINT_POSITIONS = "get_all_joint_positions"
GET_WALLS = "get_walls"
GET_INFO = "get_info"
GET_ALL_JOINT_TARGET_POSITIONS = "get_all_joint_target_positions"

##########################
#Available requiredInformation
##########################
SAFETY_LIMITS = "(1.0)"
IS_STEADY     = "(2.0)"

#######################################
# ask information to the robot
# host = ip of the robot
# command = information we want to know of the robot
# return = the information
####################################### 
def getData(host, command):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))

    s.send(command.encode())
    msg = s.recv(4096).decode()
    s.close()
    return msg

#######################################
# ask information to the second server
# host_ur = ip of the robot
# host_computer = ip of the computer
# requiredInformation = information we want to know of the robot
# extraData = extra information to ask the information:
#     SAFETY_LIMITS = this camp must be a pose
#     IS_STEADY = this camp must be ""
# return = the information
#######################################     
def runServer2(host_ur, host_computer, requiredInformation, extraData):
    script.send_program_from_doc(host_ur, NAME_FILE) #IMPORTANT! Posar la IP de l'ordinador en aquest fitxer!
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host_computer, PORT2)) # Bind to the port 
    s.listen(5) # Now wait for client connection.
    print("connexion established")
    c, addr = s.accept() # Establish connection with client.
    try:
        msg = c.recv(1024).decode()
        print (msg)
        time.sleep(1)
        if msg == "ask_me":
            c.send(requiredInformation.encode())
            if extraData != "":
                c.send(extraData.encode())
            time.sleep(0.5)
            msg = c.recv(1024).decode()
            print (msg)
    except socket.error as socketerror:
        print ("ERROR\n")
    c.close()
    s.close()
    print ("Program finish\n")
    return msg
