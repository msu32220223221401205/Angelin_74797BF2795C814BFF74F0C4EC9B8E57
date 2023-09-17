






#define the base class player
class Player:
  def play(self):
    print("the player is playing cricket")

#define the derived class batsman
class Batsman(Player):
  def play(self):
    print("the Batsman is batting ")

#define the derived class bowler
class Bowler(Player):
  def play(self):
    print("the bowler is bowling ")

#create objects of batsman and Bowler classes
batsman = Batsman()
bowler = Bowler ()

#call the play() method for each object
batsman.play()
bowler.play()
