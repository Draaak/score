import os
import sys

def processScore(matchScoreText):
  matchScores = _splitScores(matchScoreText)
  points = _calculatePoints([matchScores[0][1], matchScores[1][1]])
  return [[score[0], points[i]] for i, score in enumerate(matchScores)]

def _splitScores(score):
  teams = map(lambda text: text.strip(), score.split(','))
  return list(map(lambda score: score.rsplit(' ', 1), teams))

def _calculatePoints(scores):
  weight = int(scores[0]) - int(scores[1])
  return [1, 1] if weight == 0 else [3, 0] if weight > 0 else [0, 3]
