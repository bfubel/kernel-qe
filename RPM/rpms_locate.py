#!/usr/bin/python
import sys, getopt
import ast
import json
import os
import pprint

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -o <19.F> -v <rpm> -a <arch> -f <RPM basefile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-o':
         print ('OVS Version -o <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is "', inputfile)
   print ('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])