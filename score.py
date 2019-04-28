#!/usr/bin/python

import os
import argparse
import sys
from src.rank import processScore
from functools import reduce

def main():
  parser = argparse.ArgumentParser(prog='score')
  parser.add_argument('source', nargs='?', help='file with match scores')
  args = parser.parse_args()

  leaderBoard = reduce(_addPoints, map(processScore, _readFile(args.source) if args.source else sys.stdin), {})
  results = sorted(leaderBoard.items(), key=lambda results: results[0])
  print(sorted(results, key=lambda results: results[1], reverse=True))

def _readFile(fname):
  with open(os.path.normpath(fname), 'rt') as fin:
    return fin.readlines()

def _addPoints(dic, points):
  for result in points:
    if result[0] in dic:
      dic[result[0]] += result[1]
    else:
      dic[result[0]] = result[1]
  return dic

if __name__ == '__main__':
  main()
