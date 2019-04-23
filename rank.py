#!/usr/bin/python

import os
import argparse
import sys

def main():
  parser = argparse.ArgumentParser(prog='rank')
  parser.add_argument('source', nargs='?', help='file with scores')
  args = parser.parse_args()

  if (len(sys.argv) == 1):
    results = sorted(proccessStdin().items(), key=lambda results: results[0])
    print sorted(results, key=lambda results: results[1], reverse=True)
  else:
    results = sorted(proccessScoresFile(args.source).items(), key=lambda results: results[0])
    print sorted(results, key=lambda results: results[1], reverse=True)

def proccessScoresFile(fname):
  file = os.path.normpath(fname)
  with open(file, 'rt') as fin:
    return reduce(processScore, fin, {})

def proccessStdin():
  return reduce(processScore, sys.stdin, {})

def processScore(dic, matchScoreText):
  matchScores = splitScoreText(matchScoreText)
  points = calculatePoints(matchScores)
  addPoints(dic, matchScores[0][0], points[0])
  addPoints(dic, matchScores[1][0], points[1])
  return dic

def splitScoreText(score):
  splitTeam = map(lambda text: text.strip(), score.split(','))
  return map(lambda list: list.rsplit(' ', 1), splitTeam)

def calculatePoints(matchScores):
  weight = int(matchScores[0][1]) - int(matchScores[1][1])
  if (weight > 0):
    return [3, 0]
  else:
    if (weight < 0):
      return [3, 0]
    else:
      return [1, 1]

def addPoints(dic, team, points):
  if (team in dic):
    dic[team] += points
  else:
    dic[team] = points

if __name__ == '__main__': 
  main()
