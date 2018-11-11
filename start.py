#!/usr/bin/python
#Call python module for OS commands

import os
import subprocess

#Define variable for stop the container


#Calling the variable for stopping the container
def execute_cmd(cmd):
    
    start = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True) ###execution, non-blocking
    out, err = start.communicate()
    ret = start.returncode
    return (ret,out,err)

#Function denine for stubby

def stubby():
    cmd = "docker run --init -d -p 127.0.0.1:53:53/udp mintooraj/stubby-quad9"
    return execute_cmd(cmd)

#check if stubby is running, if not then start it up

ret,out,err = stubby()
if ("ret == 1"):
        print ("stubby not running , starting it up")
stubby()
