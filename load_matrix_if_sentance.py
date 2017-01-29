#! /usr/bin/python

import commands,os,os.path,sys,string, glob

print "Taking choosen value"

if len(sys.argv) < 2:
	print "******************** ERREUR **************************"
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
		howmuchRinfile = first_line
		print "elements of R " + first_line
		content = f.readlines()
		content = [x.strip() for x in content]
		print content
		if content == "R":
			print "wartosc:" 
			print content
sys.exit(0)




