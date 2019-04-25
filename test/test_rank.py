from src.rank import addPoints

def test_addPoints():
  dic = {}
  addPoints(dic, 'a', 5)
  assert dic == {'a': 5}