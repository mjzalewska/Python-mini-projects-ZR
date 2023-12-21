# Python checkers

### A console version of the classic board game.

The game can be played in a player vs player or player vs computer (CPU) mode.

The  game is based on the following rules :<br />

  * piece color is assigned to players randomly, <br />
  * white moves first, then players alternate turns, <br />
  * an uncrowned piece (man) can only move diagonally and forwards one square at a time <br />
  * a king can move diagonally both forwards and backwards, one square at a time <br />
  * a man is promoted to king if he reaches the opposite end of the board (row A or H) <br />
  * the white king icon is colored red in the game, while the black king is colored blue <br />
  * when capturing another piece, both the kings and men can jump two squares at a time <br />
  * an opponent's piece can only be captured if the square immediately beyond it is vacant <br />
  * when opponent's piece can be captured, capturing is mandatory <br />
  * when multiple captures in a row are possible, all captures must be carried out <br />
  * the player without pieces remaining, or who cannot move due to being blocked, loses the game.


Requirements: the game utilises standard Python library and termcolor v. 2.4.0



