#! /usr/bin/python

import commands,os,os.path,sys,string, glob

print "Taking choosen value"

if len(sys.argv) < 2:
	print "******************** ERREUR **************************"
	print "arguments:"
	print "give a full path to files"
	print "..."
	sys.exit(0)

#where i am
#basedir = os.path.abspath(os.path.dirname(__file__))


#print (basedir)
print (sys.argv)

glob.glob(sys.argv/'*.txt')



