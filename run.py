from random import randint

scores={"computer":0,"player1":0}

class Board:
  """
  The main board class. Sets the board sizze, the number of ships, the player1's name and the board type ie player1's board or computer's board.
  Has methods for adding ships and guesses and printing the board.
  """

  def __init__(self,size,num_ships,name,type):
    self.size=size
    self.board=[["." for x in range(size)] for y in range(size)]
    self.num_ships=num_ships
    self.name=name
    self.type=type
    self.guesses=[]
    self.ships=[]

  def print(self):
      for row in self.board:
        print(" ".join(row))

  def guess(self,x,y):
      self.guesses.append((x,y))
      self.board[x][y]="X"
      if (x,y) in self.ships:
        self.board[x][y]="*"
        return "Hit"
      else:
        return "Miss"

  def add_ship(self,x,y,type="computer"):
      if len(self.ships)>=self.num_ships:
        print("Error: you cannnot add any more ships!")

      else:
        self.ships.append((x,y))
        if self.type=="player1":
          self.board[x][y]="@"


def random_point(size):
  """
  Helper funtion to return a random integer between 0 and size
  """
  return randint(0,size-1)

def valid_coordinates(x,y,board):
  """
  validate that the cordinates inputs that validates that not yet guessed.
  Validate that they are not outside our board.
  """
  listvar=[0,1,2,3,4]

  try:
    if x not in listvar:
      raise ValueError(f"Sorry you entered invalid input {x}!")

  except ValueError as e:
        print(f"Invalid guess:{e},please try numbers any of the following numbers 0,1,2,3,4")
        return False

  try:
    if y not in listvar:
      raise ValueError(f"Sorry you entered invalid input {y}!")

  except ValueError as e:
        print(f"Invalid guess:{e},please try numbers any of the following numbers 0,1,2,3,4")
        return False



  try:
    if((x,y) in board.guesses):
      raise ValueError(
          f"Sorry you have already guessed {(x,y)}!"
      )
  except ValueError as e:
        print(f"Invalid guess:{e},please try again.\n")
        return False

  return True


def populate_board(board):
  """
  choose random row and random column and put a ship there.
  """
  x=random_point(5)
  y=random_point(5)

  board.add_ship(x,y)
  #board.print()

