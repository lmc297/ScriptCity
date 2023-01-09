#!/usr/bin/python

import sys, os, glob



def run_wgsim(f):

	fname = os.path.basename(f)
	fname = fname.split(".")[0:-1]
	fname = ".".join(fname)
	print(fname)

	# estimate genome size from file size
	fsize = os.path.getsize(f)

	# specify wgsim parameters based on those used by lyve-set
	readLength = 250 # simulate 250 bp reads
	d = 400 # outer distance between the two ends [500 by default, 400 by lyve-set]
	N = fsize*100/(readLength*2) # number of read pairs [1000000 by default, formula per lyve-set]
	e = 0.0 # base error rate [0.020 by default, 0.0 by lyve-set]
	r = 0.0 # rate of mutations [0.0010 by default, 0.0 by lyve-set]
	R = 0.0000 # fraction of indels [0.15 by default, 0.0000 by lyve-set]

	# construct wgsim command
	cmd = "wgsim -d {0} -N {1} -1 {2} -2 {2} -e {3} -r {4} -R {5} -h {6} {7} {8}".format(d, N, readLength, e, r, R, f, fname + "_1.fastq", fname + "_2.fastq")

	# run wgsim
	os.system(cmd)

if __name__ == "__main__":

	run_wgsim(str(sys.argv[1]).strip())
