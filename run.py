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

