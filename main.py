#Import required libraries
import os
import subprocess

subprocess.call("docker rmi $(docker ps -a -q)", shell=True)