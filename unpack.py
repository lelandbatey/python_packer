#!/usr/bin/env python
import collections
import platform
import os.path
import inspect
import base64
import time
import sys
import os

d = {1}



def recursive_unpack(itemDict, dirpath):
	for item in itemDict.keys():
		ipath = os.path.abspath(os.path.join(dirpath, item))

		if isinstance(itemDict[item], basestring):
			tmp = open(ipath,'w')
			tmp.write(base64.b64decode(itemDict[item]))
			tmp.close()
		elif isinstance(itemDict[item], dict):
			os.makedirs(ipath)
			recursive_unpack(itemDict[item], ipath)
		else:
			print type(itemDict[item])

# By default, all files go into a folder called "{0}"
# Check if all the files already exist:
if not os.path.isdir("{0}"):
	os.makedirs("{0}")
	recursive_unpack(d,"{0}")



# Get the current os
currentOS = platform.system().lower()
# Get the current file
thisFile = inspect.getfile(inspect.currentframe())

if "windows" not in currentOS:
	# Check if the current file is executable
	os.system("chmod +x {{}}".format(thisFile))
	# If we're on Mac, rename the file to be '.command'
	if "darwin" in currentOS:
		os.system('mv {{}} {{}}'.format(thisFile, thisFile.split('.')[0]+'.command'))



# Execute the actual python file
os.chdir("{0}")
sys.path.append(os.getcwd())
import {2}
{2}.main()
