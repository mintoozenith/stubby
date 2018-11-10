#!/usr/bin/python
#Call python module for OS commands

import os
import subprocess

#Define variable for stop the container

stop_container = "docker ps | grep oikuda/stubby-quad9 | awk '{print $1}' | xargs docker kill"

#Calling the variable for stopping the container
stop = subprocess.Popen(stop_container, shell=True, stderr=subprocess.PIPE)
