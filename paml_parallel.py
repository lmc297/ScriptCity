#!/usr/bin/env python

# run multi-threaded codeml
# run script from directory with .ctl files
# usage: python paml_parallel.py <number of threads>


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
	pool = multiprocessing.Pool(int(sys.argv[1]))
	tasks = glob.glob("*.ctl")
	pool.map(run_paml, tasks)






