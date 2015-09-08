from sys import argv
import os
import subprocess

if len(argv) < 2 or len(argv) > 2:
	print "Usage: python pwoo.py [binary file]"
	exit(0)
filename = str(os.getcwd()) + "/" + str(argv[1])
subprocess.call(["chmod","+x",argv[1]])
print("-----------file--------------")
subprocess.call(["file",filename])
print("-----------ls--------------")
subprocess.call(["ls","-la",argv[1]])
print("-----------readelf----------------")
subprocess.call(["readelf","-h",filename])
print("-----------objdump---------------")
subprocess.call(["objdump","-R",filename])
print("-------------nm---------------")
subprocess.call(["nm",filename])
print("-----------------------------")
