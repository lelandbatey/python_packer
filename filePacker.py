#!/usr/bin/env python
from __future__ import print_function
import argparse
import os.path
import base64
import json
import sys
import os

def main():

	parser = argparse.ArgumentParser()

	parser.add_argument("--include", nargs='+',required=True)
	parser.add_argument("--exclude-extensions", nargs='+',
	                    default=['.pyc','.exe','.stackdump','.git'])
	parser.add_argument("--output-dir", required=True)
	parser.add_argument("--import-name", required=True)


	args = parser.parse_args()

	files = args.include

	excludedFiles = args.exclude_extensions
	zipDict = {}

	def recursive_pack(itemList, dirpath):
		outDict = {}
		for item in itemList:
			ipath = os.path.abspath(os.path.join(dirpath, item))
			# Checks that nothing in excluded files is in the current name
			validName = True
			for x in excludedFiles:
				if x in item:
					validName = False
			if os.path.isfile(ipath):		
				
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

	print(open("unpack.py",'r').read().format(args.output_dir, strDict, args.import_name))


if __name__ == '__main__':
	main()
