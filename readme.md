######		Battleship Game-Simple 	########
##### 		By Krista Parry 	########
##### 	Earnest Data Engineering Challenge #####


Battleship boards are created in main, by calling the add_ship() function.

A sample board looks like this, when the following
inputs is provided:

name:'C', length=3 at position: (7,2), orientation: v
name:'A', length=5 at position: (1,1), orientation: v

User board:

	1	2	3	4	5	6	7	8	9	10
	__________________________________________________________________________
1 |	A	0	0	0	0	0	0	0	0	0
  |
2 |	A	0	0	0	0	0	0	0	0	0
  |	
3 |	A	0	0	0	0	0	0	0	0	0
  |
4 |	A	0	0	0	0	0	0	0	0	0
  |	
5 |	A	0	0	0	0	0	0	0	0	0
  |
6 |	0	0	0	0	0	0	0	0	0	0	
  |
7 |	0	C	0	0	0	0	0	0	0	0
  |
8 |	0	C	0	0	0	0	0	0	0	0
  |
9 |	0	C	0	0	0	0	0	0	0	0
  |	
10|	0	0	0	0	0	0	0	0	0	0

##### Game Play and Winning #####

Once the board is set up,  a shot can be fired by calling attack(row,col) and providing the 
row,column pair as input.

If the shot hits a ship, then the shot is called a "Hit".
If the shot does not hit a ship, then the shot is called a "Miss".
If the shot has already been attempted, the message "Already taken" is displayed. 

If all single ship has been hit at every row,column value, then it is considered "Sunk".

The winner is declared if all ships have been sunk.

###### Playing against the computer #######

Computer should use this algorithm for best strategic plays.

http://www.datagenetics.com/blog/december32011/index.html







