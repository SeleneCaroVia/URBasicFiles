# -*- coding: utf-8 -*-
"""
Created on Mon Feb 04 19:21:46 2019
Document to send commands to the interface
https://www.universal-robots.com/how-tos-and-faqs/how-to/ur-how-tos/dashboard-server-e-series-port-29999-42728/
@author: Selene Caro Via
"""

import socket

PORT = 29999

#######################################
# Load a program in the robot
# host = ip of the robot
# name_program = name of the program to be load
#######################################
def load_program(host, name_program):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send(('load '+ name_program +'\n').encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Stop the running program in the robot
# host = ip of the robot
#######################################
def stop_program(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('stop\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()
    
#######################################
# Play a program in the robot
# host = ip of the robot
#######################################    
def play_program(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('play\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Pause a program in the robot
# host = ip of the robot
#######################################
def pause_program(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('pause\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Closes connection
# host = ip of the robot
# name_program = name of the program to be load
#######################################    
def disconnect(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('quit\n'.encode())
    msg = s.read(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Shuts down and turns off robot and controller
# host = ip of the robot
#######################################     
def shutdown(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('shutdown\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Execution state enquiry
# host = ip of the robot
#######################################  
def is_running(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('running\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Robot mode enquiry
# host = ip of the robot
#######################################      
def know_robotmode(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('robotmode\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Which program is loaded
# host = ip of the robot
#######################################       
def get_loaded_program(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('get loaded program\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()
 
#######################################
# The popup-text will be translated to the selected language, if the text exists in the language file
# host = ip of the robot
# text = text in the popup
#######################################   
def show_popup(host, text):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send(('popup '+ text + '\n').encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Closes the popup
# host = ip of the robot
#######################################
def close_popup(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('close popup\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Adds log-message to the Log history
# host = ip of the robot
# text = text in the popup
#######################################       
def add_log_message(host, text):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send(('addToLog '+ text + '\n').encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Returns the save state of the active program and path to loaded program file
# host = ip of the robot
#######################################      
def is_program_saved(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('isProgramSaved\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()
    
#######################################
# Returns the state of the active program and path to loaded program file, or STOPPED if no program is loaded
# host = ip of the robot
#######################################
def program_state(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('programState\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Returns the version of the PolyScope software
# host = ip of the robot
#######################################	
def polyscope_version(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('PolyscopeVersion\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Controls the operational mode. See User manual for details.
# IMPORTANT:
# This functionality is intended for using e.g. Ethernet based Key Card Readers to switch operational modes.
# The device for switching operational mode should be placed in vicinity to the robot.
# host = ip of the robot
# mode = manual or automatic
#######################################	    
def set_operational_mode(host, mode):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    if (mode == "manual" | mode == "automatic"):
        s.send(('set operational mode '+ mode + '\n').encode())
        msg = s.recv(1024).decode()
        msg = s.recv(1024).decode()
        print (msg)
    else:
        print ("Error mode. It should be manual or automatic.")
    s.close()

#######################################
# If this function is called the operational mode can again be changed from PolyScope, and the user password is 
# enabled.
# host = ip of the robot
#######################################	    
def clear_operational_mode(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('clear operational mode\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Powers on the robot arm
# host = ip of the robot
#######################################	    
def power_on(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('power on\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Powers off the robot arm
# host = ip of the robot
#######################################	    
def power_off(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('power off\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Releases the brakes
# host = ip of the robot
#######################################	    
def brake_release(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('brake release\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Safety mode enquiry
# host = ip of the robot
#######################################	    
def safetymode(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('safetymode\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Closes the current popup and unlocks protective stop
# IMPORTANT:
# It is the responsibility of the integrator to ensure the cause of the protective stop is resolved before using the 
# "unlock protective stop" command
# host = ip of the robot
#######################################	    
def unlock_protective_stop(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('unlock protective stop\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Closes a safety popup
# host = ip of the robot
#######################################	
def close_safety_popup(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('close safety popup\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Loads the specified installation file but does not return until the load has completed (or failed).
# The load command fails if the associated installation requires confirmation of safety. The return value will be 
# 'Failed to load installation'.
# host = ip of the robot
#######################################	    
def load_installation(host, installation):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send(('load installation '+ installation + '\n').encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()

#######################################
# Used when robot gets a safety fault or violation to restart the safety. After safety has been rebooted the robot 
# will be in Power Off.
# IMPORTANT: 
# You should always ensure it is okay to restart the system. It is highly recommended to check the error log before 
# using this command (either via PolyScope or e.g. ssh connection).
# host = ip of the robot
#######################################	    
def restart_safety(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send('restart safety\n'.encode())
    msg = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    print (msg)
    s.close()
