#!/usr/bin/python

import os
import argparse
import sys
from src.rank import processScore

def main():
  parser = argparse.ArgumentParser(prog='rank')
  parser.add_argument('source', nargs='?', help='file with scores')
  args = parser.parse_args()

  # if (len(sys.argv) == 1):
  #   results = sorted(proccessStdin().items(), key=lambda results: results[0])
  #   print sorted(results, key=lambda results: results[1], reverse=True)
  # else:
  #   results = sorted(proccessScoresFile(args.source).items(), key=lambda results: results[0])
  #   print sorted(results, key=lambda results: results[1], reverse=True)

  print reduce(processScore, sys.stdin if len(sys.argv) == 1 else readFile(args.source), {})

def readFile(fname):
  file = os.path.normpath(fname)
  with open(file, 'rt') as fin:
    return fin.readlines()

if __name__ == '__main__': 
  main()
