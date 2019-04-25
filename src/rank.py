import os
import sys

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
    return [0, 3] if (weight < 0) else [1, 1]

def addPoints(dic, team, points):
  if (team in dic):
    dic[team] += points
  else:
    dic[team] = points

