from src.rank import processScore

def test_with_first_team_winning():
  assert processScore('A 4, B 0') == [['A', 3], ['B', 0]]

def test_with_second_team_winning():
  assert processScore('C 0, D 1') == [['C', 0], ['D', 3]]

def test_zero_draw():
  assert processScore('E 0, F 0') == [['E', 1], ['F', 1]]

def test_non_zero_draw():
  assert processScore('G 2, H 2') == [['G', 1], ['H', 1]]

def test_with_team_name_with_spaces():
  assert processScore('I i 3, J j 4') == [['I i', 0], ['J j', 3]]
