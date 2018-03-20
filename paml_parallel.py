#!/usr/bin/python

import os, glob
import multiprocessing
import shlex

from multiprocessing.pool import ThreadPool

def run_paml(f):
	print f
	prefix = f.replace(".ctl", "")
	os.mkdir(prefix)
	os.system("cp *"+prefix+"* "+prefix)
	os.chdir(prefix)
	os.system('yes 2>/dev/null | codeml '+f)
	os.chdir("..")

if __name__ == "__main__":
	pool = multiprocessing.Pool(20)
	print "Here we go"
	print pool
	tasks = glob.glob("*.ctl")
	pool.map(run_paml, tasks)






