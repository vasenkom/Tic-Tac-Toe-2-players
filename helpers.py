import random

def choose_starting_player(name1, name2):
  player_names = [name1, name2]
  random.shuffle(player_names)
  starting_player = player_names[0]
  print(starting_player + " starts the game")
  return starting_player

def choose_marks(starting_player):
  print(starting_player + ", choose X or 0: ")
  mark1 = input().upper()
  mark2 = "0" if mark1 == "X" else "X"
  return mark1, mark2
  
def set_board(spots):
  #Board
  board = (
    f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
    f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
    f"|{spots[7]}|{spots[8]}|{spots[9]}|\n"
  )
  print(board)

#Check who's turn is it. The first player starts with X (for now)
def check_turn(turn, mark1, mark2):
  if turn % 2 == 0:
    return mark2
  else:
    return mark1

#Check for win situations
def check_for_wins(spots):
  
  #Check the horizontal line
  if (spots[1] == spots[2] == spots[3]) \
    or (spots[4] == spots[5] == spots[6]) \
    or (spots[7] == spots[8] == spots[9]):
    return True
  
  #Check the vertical line
  elif (spots[1] == spots[4] == spots[7]) \
    or (spots[2] == spots[5] == spots[8]) \
    or (spots[3] == spots[6] == spots[9]):
    return True

  #Check the diagonals
  elif (spots[1] == spots[5] == spots[9]) \
    or (spots[3] == spots[5] == spots[7]):
    return True

  else:
    return False
  
