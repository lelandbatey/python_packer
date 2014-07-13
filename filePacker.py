#!/usr/bin/env python
from __future__ import print_function
import argparse
import os.path
import base64
import json
import sys
import os

parser = argparse.ArgumentParser()

parser.add_argument("--include", nargs='+',required=True)
parser.add_argument("--exclude-extensions", nargs='+',
                    default=['.pyc','.exe','.stackdump'])
parser.add_argument("--output-dir", required=True)
parser.add_argument("--import-name", required=True)


args = parser.parse_args()

# Assumes that every argument is a file or folder to be compressed. Each one
# must be in the current directory.

# files = sys.argv[1:]
files = args.include
# print(type(files))
# print(args)
# exit()

excludedFiles = args.exclude_extensions
zipDict = {}
# print(excludedFiles)

def recursive_pack(itemList, dirpath):
	outDict = {}
	for item in itemList:
		ipath = os.path.abspath(os.path.join(dirpath, item))
		# print(ipath)
		# print(excludedFiles)
		# print(item)
		if os.path.isfile(ipath):		
			# Checks that nothing in excluded files is in the current name
			validName = True
			for x in excludedFiles:
				if x in item:
					validName = False
			
			# print(validName, item, file=sys.stderr)
			if validName:
				tmp = open(ipath,'r')
				dat = base64.b64encode(tmp.read())
				outDict[item] = dat
				tmp.close()

		elif os.path.isdir(ipath):
			outDict[item] = recursive_pack(os.listdir(ipath),ipath)
	return outDict


zipDict = recursive_pack(files,'./')
strDict = json.dumps(zipDict, sort_keys=True, indent=4, separators=(',', ': '))

# print(zipDict)

print(open("unpack.py",'r').read().format(args.output_dir, strDict, args.import_name))

