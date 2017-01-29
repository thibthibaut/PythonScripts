#! /usr/bin/python

import commands,os,os.path,sys,string, glob

print "Taking choosen value"

if len(sys.argv) < 2:
	print "******************** ERROR **************************"
	print "arguments:"
	print "give a full path to files"
	print "..."
	sys.exit(0)

## HERE DEFINE WHAT ARE YOU LOOKINg FOR ##
typeOfFile = '*.txt'
pathToFiles = sys.argv[1]
pathToFiles = pathToFiles + typeOfFile

files = glob.glob(pathToFiles)
for input_file in files:
	print "input file : "+ input_file
	with open(input_file, 'r') as f:		
		first_line = f.readline()
		print "swinia " + first_line
		for i in first_line:
			print "swinkaa " + i
			while (f.readline() == "R"):
				content = f.readline()
				content = f.readline()
				print "swiania"
#content = [x.strip() for x in content]
#print content
sys.exit(0)




