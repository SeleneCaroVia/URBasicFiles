# -*- coding: utf-8 -*-
"""
Created on Mon Feb 04 19:30:20 2019
Document to send scripts to the robot
@author: Selene Caro Via
"""

import socket
from Alexa import create_doc_UR_with_alexa as doc

PORT = 30002

#######################################
# movej: Move to position (linear in joint-space)
# host = ip of the robot
# rad_joint0 = base
# rad_joint1 = shoulder
# rad_joint2 = elbow
# rad_joint3 = wrist 1
# rad_joint4 = wrist 2
# rad_joint5 = wrist 3
# a = joint acceleration of leading axis [rad/s^2]
# v = joint speed of leading axis [rad/s]
# t = time [S]
# r = blend radius [m]
#   If a blend radius is set, the robot arm trajectory will be
#   modified to avoid the robot stopping at the point.
#   However, if the blend region of this move overlaps with
#   the blend radius of previous or following waypoints, this
#   move will be skipped, and an ’Overlapping Blends’
#   warning message will be generated.
#Example command: movej([0,1.57,-1.57,3.14,-1.57,1.57],a=1.4, v=1.05, t=0, r=0)
#######################################
def movej_rad(host, rad_joint0, rad_joint1, rad_joint2, rad_joint3, rad_joint4, rad_joint5, a, v, t, r):
    command = "    movej(["+ str(rad_joint0)+ "," + str(rad_joint1)+ "," + str(rad_joint2) + "," + str(rad_joint3) + "," + str(rad_joint4) + "," + str(rad_joint5) + "], a=" +str(a) +", v=" +str(v) +", t=" + str(t) + ", r=" + str(r) +")\n"
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err = s.connect((host, PORT))
    print("CONNECTANT movej_rad...\n")
    if (err != 0):
        s.send('def movej_rad():\n'.encode())
        s.send(command.encode())
        s.send('    sync()\n'.encode())
        s.send('end\n'.encode())
        s.close()
    else:
        print("ERROR, NO S'HA POGUT FER LA CONNEXIO\n")

#######################################
# movej: Move to position (linear in joint-space)
# host = ip of the robot
# x = x [m]
# y = y [m]
# z = z [m]
# rx = rx [rad]
# ry = ry [rad]
# rz = rz [rad]
# a = joint acceleration of leading axis [rad/s^2]
# v = joint speed of leading axis [rad/s]
# t = time [S]
# r = blend radius [m]
#   If a blend radius is set, the robot arm trajectory will be
#   modified to avoid the robot stopping at the point.
#   However, if the blend region of this move overlaps with
#   the blend radius of previous or following waypoints, this
#   move will be skipped, and an ’Overlapping Blends’
#   warning message will be generated.
#Example command: movej([0,1.57,-1.57,3.14,-1.57,1.57],a=1.4, v=1.05, t=0, r=0)
#######################################
def movej_pose(host, x, y, z, rx, ry, rz, a, v, t, r):
    command = "    movej(p["+ str(x)+ "," + str(y)+ "," + str(z) + "," + str(rx) + "," + str(ry) + "," + str(rz) + "], a=" +str(a) +", v=" +str(v) +", t=" + str(t) + ", r=" + str(r) +")\n"
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err = s.connect((host, PORT))
    print("CONNECTANT movej_pose...\n")
    if (err != 0):
        s.send('def movej_pose():\n'.encode())
        s.send(command.encode())
        s.send('    sync()\n'.encode())
        s.send('end\n'.encode())
        s.close()
    else:
        print("ERROR, NO S'HA POGUT FER LA CONNEXIO\n")

#######################################
# Move the robot in the X axis
# host = ip of the robot
# x = cm to move in the X axis
#######################################
def moveX(host, x):
    y = float(x*0.01) #cm unit
    command = "    pose = pose_add(get_actual_tcp_pose(),p["+ str(y)+ ",0,0,0,0,0])\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err = s.connect((host, PORT))
    print("CONNECTANT...\n")
    if (err != 0):
        s.send('def moveX():\n'.encode())
        s.send(command.encode())
        s.send('    movej(pose, a=1.2, v=0.25, t=0, r=0)\n'.encode())
        s.send('end\n'.encode())
        s.close()
    else:
        print("ERROR, NO S'HA POGUT FER LA CONNEXIO\n")

#######################################
# Move the robot in the Y axis
# host = ip of the robot
# x = cm to move in the y axis
#######################################        
def moveY(host, x):
    y = float(x*0.01) #cm unit
    command = "    pose = pose_add(get_actual_tcp_pose(),p[0,"+ str(y)+ ",0,0,0,0])\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err = s.connect((host, PORT))
    print("CONNECTANT...\n")
    if (err != 0):
        s.send('def moveY():\n'.encode())
        s.send(command.encode())
        s.send('    movej(pose, a=1.2, v=0.25, t=0, r=0)\n'.encode())
        s.send('end\n'.encode())
        s.close()
    else:
        print("ERROR, NO S'HA POGUT FER LA CONNEXIO\n")

#######################################
# Move the robot in the Z axis
# host = ip of the robot
# x = cm to move in the Z axis
#######################################
def moveZ(host, x):
    y = float(x*0.01) #cm unit
    command = "    pose = pose_add(get_actual_tcp_pose(),p[0,0," + str(y) + ",0,0,0])\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err = s.connect((host, PORT))
    print("CONNECTANT...\n")
    if (err != 0):
        s.send('def moveZ():\n'.encode())
        s.send(command.encode())
        s.send('    movej(pose, a=1.2, v=0.25, t=0, r=0)\n'.encode())
        s.send('end\n'.encode())
        s.close()
    else:
        print("ERROR, NO S'HA POGUT FER LA CONNEXIO\n")


#######################################
# Move the robot in the XYZ axis
# host = ip of the robot
# x = cm to move in the X axis
# y = cm to move in the Y axis
# z = cm to move in the Z axis
# rx = rad to rotate in the RX axis
# ry = rad to rotate in the RY axis
# rz = rad to rotate in the RZ axis
#######################################
def moveXYZ(host, x, y, z, rx, ry, rz):
    x = float(x*0.01)
    y = float(y*0.01)
    z = float(z*0.01)
    command = "    pose = pose_add(get_actual_tcp_pose(),p[" + str(x) + "," + str(y) + "," + str(z) + "," + str(rx) +"," + str(ry) + "," + str(rz) + "])\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err = s.connect((host, PORT))
    print("CONNECTANT...\n")
    if (err != 0):
        s.send('def moveXYZ():\n'.encode())
        s.send(command.encode())
        s.send('    movej(pose, a=1.2, v=0.25, t=0, r=0)\n'.encode())
        s.send('end\n'.encode())
        s.close()
    else:
        print("ERROR, NO S'HA POGUT FER LA CONNEXIO\n")
    

#######################################
# Move the robot in a vertical plane (Y and Z axis)
# host = ip of the robot
# y = cm to move in the Y axis
# z = cm to move in the Z axis
#######################################        
def move_plane(host, y, z):
    y = float(y*0.01)
    z = float(z*0.01)
    command = "    pose = pose_add(get_actual_tcp_pose(),p[0,"+ str(y)+ ","+ str(z) + ",0,0,0])\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err = s.connect((host, PORT))
    print("CONNECTANT...\n")
    if (err != 0):
        s.send('def planeYZ():\n'.encode())
        s.send(command.encode())
        s.send('    movej(pose, a=1.2, v=0.25, t=0, r=0)\n'.encode())
        s.send('end\n'.encode())
        s.close()
    else:
        print("ERROR, NO S'HA POGUT FER LA CONNEXIO\n")

#######################################
# Move the robot's joints (Y and Z axis)
# host = ip of the robot
# y = rad to move in the joint[4]
# z = rad to move in the joint[3]
#######################################  
def move_joints_x_y(host, rot_y, rot_z):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err = s.connect((host, PORT))
    print("CONNECTANT...\n")
    if (err != 0):
        command1 = "    joint[4] = joint[4]+(" + str(rot_y) + ")\n"
        command2 = "    joint[3] = joint[3]+(" + str(rot_z) + ")\n"
        print(command1)
        print(command2)
        s.send('def jointsXY():\n'.encode())
        s.send('    joint = get_actual_joint_positions()\n'.encode())
        s.send(command1.encode())
        s.send(command2.encode())
        s.send('    movej(joint, a=1.4, v=1.05, t=0, r=0)\n'.encode())
        s.send('end\n'.encode())
        s.close()
        print("enviat")
    else:
        print("ERROR, NO S'HA POGUT FER LA CONNEXIO\n")
    
#######################################
# Put the robot in freemode
# host = ip of the robot
#######################################  
def freedrive_mode(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('def Freedrive():\n'.encode())
    s.send('    while(1):\n'.encode())
    s.send('        freedrive_mode()\n'.encode())
    s.send('        sync()\n'.encode())
    s.send('    end\n'.encode())
    s.send('end\n'.encode())
    s.close()
    #podem substituir el while(1) per un sleep(t) [t en segons]????

#######################################
# Stop the freemode
# host = ip of the robot
####################################### 
def end_freedrive_mode(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('def EndFreedrive():\n'.encode())
    s.send('    end_freedrive_mode()\n'.encode())
    s.send('    sync()\n'.encode())
    s.send('end\n'.encode())
    s.close()

########################################
# Opens the gripper
# host = ip of the robot
# n = number (id) of the output, integer: [0:7]
########################################
def open_gripper(host, n):
    command = "    set_standard_digital_out(" + str(n) + ", False)\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('def ObrePinca():\n'.encode())
    s.send(command.encode())
    s.send('    sync()\n'.encode())
    s.send('end\n'.encode())
    s.close()

########################################
# Closes the gripper
# host = ip of the robot
# n = number (id) of the output, integer: [0:7]
########################################
def close_gripper(host, n):
    command = "    set_standard_digital_out(" + str(n) + ", True)\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('def TancaPinca():\n'.encode())
    s.send(command.encode())
    s.send('    sync()\n'.encode())
    s.send('end\n'.encode())
    s.close()    
    
    
########################################
# Sends a script file to the robot
# host = ip of the robot
# name_file = path of the file. if it is in the same folder, do ./name_of_file.script
########################################    
def send_program_from_doc(host, name_file):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(s.connect((host, PORT)))
    f = doc.doc(name_file, "r")
    line = f.get_line()
    #print(line)
    while (line):
        #print(line)
        s.send(line.encode())
        line = f.get_line()
    s.close()
    f.close_doc() 
