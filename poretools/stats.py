import numpy
import common
import Fast5File

def run(parser, args):
	sizes = []
	for filename in common.get_fast5_files(args.files):
		fast5 = Fast5File.Fast5File(filename)
                fas = fast5.get_fastas(args.type)
		sizes.extend([len(fa.seq) for fa in fas if fa is not None])
		fast5.close()

	print "total reads\t%d" % (len(sizes))
	print "total base pairs\t%d" % (sum(sizes))
	print "mean\t%.2f" % (numpy.mean(sizes))
	print "median\t%d" % (numpy.median(sizes))
	print "min\t%d" % (numpy.min(sizes))
	print "max\t%d" % (numpy.max(sizes))
