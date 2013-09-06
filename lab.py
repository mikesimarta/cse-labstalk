#! /usr/bin/python2.7
import subprocess, sys, re

def get_names(x):
	output = subprocess.check_output(["./getusername.sh", x.group(1)]).strip().split(" ")
	nameString = ": %s %s (%s)" % (output[0], output[-1], x.group(1))
	return nameString + " " * (32 - len(nameString))


data = subprocess.check_output(["lab", "-A"]).split("\n")

for line in data:
	
	if re.search(": \w", line):
		print ": \t".join(re.sub(": (\w+)\s+", get_names, line).split(": "))
	elif ("-q" not in sys.argv):
		print " ".join(line.split(" ")[:-2])	


	
