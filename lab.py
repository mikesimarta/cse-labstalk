#! /usr/bin/python2.7
import subprocess, sys, re

def get_names(x):
	output = subprocess.check_output(["./getusername.sh", x.group(1)]).strip().split(" ")
	nameString = ": %s %s (%s)" % (output[0], output[-1], x.group(1))
	return nameString + " " * (48 - len(nameString))


def labstalk():
	data = subprocess.check_output(["lab", "-A"]).split("\n")

	for line in data:
		
		if re.search(": \w", line):
			print ": \t".join(re.sub(": (\w+)\s+", get_names, line).split(": "))
		elif ("-q" not in sys.argv):
			print " ".join(line.split(" ")[:-2])	


def find_a_lab():
	data = subprocess.check_output(["lab", "-A"]).split("\n")
	for line in data:
		if "Lab" in line:
			if "FREE" in line:
				splitline = line.split(" ")
				free = -1 # because we match the lab line too
				for labline in data:
					if splitline[1] in labline:
						if not re.search(": \w", labline):
							free+=1
					
					
				print "%s has %d free computers" % (splitline[1], free)								

	

	
if __name__ == '__main__':

	if "-f" in sys.argv:
		find_a_lab()
	else:
		labstalk()

