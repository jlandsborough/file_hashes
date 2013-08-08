#
# Description: Generates hashes of files in the given directory and subdirectories
#
# By: Jason Landsborough
# Last updated: 08/7/13
#
#


import hashlib
import os
import sys


global global_dir1
global_dir1 = "/home/jason/Pictures"

fout = open("hashes.txt", "w")

for curdir, dirs, files in os.walk(global_dir1):
	print "Directory: " + curdir
	fout.write("\nDirectory: " + curdir + "\n")
	for thefile in files:
		sha1 = hashlib.sha1()
		f = open(str(curdir) + "/" + thefile)		
		try:
		        sha1.update(f.read())
		finally:
			f.close()
		hashstr = sha1.hexdigest() 
		print('{0:50}\t{1:10}'.format(thefile, hashstr))
		fout.write(('{0:50}\t{1:10}\n'.format(thefile, hashstr))) 

fout.close()




