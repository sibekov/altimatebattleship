<h1>altimatebattleship</h1>

<p>A Python programing languege game that is all about hitting the ships of your oponent while your openent is also trying to do the same thing,hitting your ships.</p>

<h1>How is it played</h1>

<p> The player need to enter their name and press enter and two boards will be randomly generated.  The player will be able to see their ships, labelled by @ sign.  The player will not be able to see the oponents ships, ie. the computer's in this case.   Guesses are marked by X for a miss and by * for a hit.  The player and  the computer will take turns in trying to locate the openents ship.  Tha one that will manage to kill all of the oponents sheep will win. otherwise the game will need to be restarted after four attempts.</p>

<h1>Features</h1>
<h2>Landing Page</h2>
<img src="landingpage.png">
<p> The Orange RUN PROGRAM button is used to start or restart the game when it is finished. When pressed the user will be welcomed advised of the board size of 5 by 5 and number of ships which is kept at 4, and the fact that the top left most corner would be row 0 column 0 and then the user will be prompted to ender their name.</p>
<h2>The Game Boards</h2>
<img src="gameboards.png"><img src="gameboard.png">
<p>Ships positions are randomly generated on both the computer's board and the player's board, vee's board in this example. Compare with the next board and see that the ships are indeed randomly generated as they are not placed at the sameplace if you rerun the program with the run program button. It is interesting again to note that only the player's ships are visible to the player. The Player's ships are dipicted by the @, as already discrible on how it is played above paragraph above.  The player can not see the computers's ships she or he has to gues them, that is the game</p>
<h2>Missed Ship</h2>
<img src="mis.png">
<p>Once the user has entered their name, they will be asked to enter their number twice in a row, the first number will be their row and the second number will be their column. In this example the user picked 0 followed by 1 meaning he or she is guesing the computer's ship is hiddin at row 0 column1. This is shown back to the user as coordinate (0,1) additionally the player is advised that he is missed in this case.  He is also advised of the computer's shot, in this case the computer guessed the player's ship to be hidden at row 2 column 1, i.e. coordinate (2,1) which was also a miss for the computer. Lastly the scores after this round are shown.The misses are marked with X as it has already been explained in how it is played.</p>
<h2>Computer Hitted Ship</h2>
<img src="computerhit.png">
<p>See that when player's ship is hit then the @ changes to *, this way the play can see how many ships are still alive. The massage will advise that the computer hitted and player missed and also showing coordinates and the updated score after the round. In this case the computer has 1 and vee hass 0. Since the computer correclty guessed the player's ship to be hidding in row 4 column 4 i.e. coordinate (4,4) meanwhile vee misse's as he incorrectly guessed (2,2) and none of the computer's ship are hidding there.</p>
<h2>Player Hitted Ship</h2>
<img src="veehitted.png">
<p>See that also when the player hit he also get advised that he hit, the coordinates are confirmed back and the scores are updated accordingly. In this case player,vee guessed the computers' ship to be hidding at row 4 and column 4 ie coordinate (4,4) wich was one of the computer's ship's hidding spot. </p>
<h1>Input Validation and Error-checking</h1>
<h2>Not A Number!</h2>
<img src="notanumber.png">
<p>See that when a player enters something other than a number,tee, in this case, an error message is returned letting the user that what they entered is not a number, they need to enter numbers between 0 and 4. </p>
<h2>Out of Range!</h2>
<img src="rangeout.png">
<p>See that when a player enters a coordinate that is outside the board,like 99 or 5 as in this case, they receive an error message letting them they are out of range, they need to puck numbers between 0 and 4.</p>
<h2>Avoid Duplicates!</h2>
<img src="sameguess.png">
<p>See that when a player enters a coordinate that has already been entered, in this case (2,2), the player will get the error message that the guess was already made she or he must try again.</p>
<h1>Data Model</h1>
<p>The game has two instances of the board class to keep player's and the computer'sboard.   The Board class keeps the board size, the number of ships, the posistion of the ships, the guesses against that board, and the details of the board type may be a competer's board or the player's board and the plyer's name is kept. methods in the class that help to play the game are the print menthod the add_ships and the guess</p>
<h1>Testing<h1>
<h2>Manual Testing<h2>
<p>I manually tested the invlid inputs eg: out of range inputes, duplicates inputs and strings when expecting numbes. Refere to validation and Error-checking above.</p>
<h2>PEP8 Testing<h2>

<h1>Solved Bugs<h1>
<h2>Not A Number<h2>
<img src="numbererror.png">
<p>As you can see above the code used to brake whenever the player enters a string while the game is expecting a number.  This I have resolved by employing a function called ismynumber which checks first if the input is an integer returns an error message if not otherwise it returns back where it was called in the guess function. This solved the problem as you can see the results under the validation and error-checking section</p>
<img src="continuous.png">
<p>The other problem that can bee see from above is that the game was not continuous it would stop after the user has inputed the row and column and I had to reinitiate it each time.  I resolved this by inserting a while loop and now is continuous.  see validation and error-cheking section for results.</p>
<img src="propername.png">
<p>Another problem is that the user can enter a number or empty string as a name or anthing for that matter the the game would play.  See on the above snip for an example the computer is playing a person with no name.</p>
<h1>Solved PEP8 Errors<h1>
<img src="pepfault.png">
<p>pep8 picked up a lot of white spaces and indentations errors which I had to fix line by line. see example of such error messages from one snip I took before resolving them above.</p>
<h1>References<h1>
<h2>Anna Greaves</h2>
<p>The code is inspired by the Love Sandwiches Code Institute walkthrough Project videos delivered by Full Stack Web developer and content creator, Anna Greaves.</p>
<h2>Matt Rudge</h2>
<p>The CSS code on the footer was partly taken from the battle ships game walk through project presented by Matt Rudge, Senior Product Developer at code institude.</p>
<h2>Tutorialspoint</h2>
<p>This site help to refresh my memory on how to declare empty string and empty list
https://www.tutorialspoint.com/How-to-declare-a-variable-in-Python-without-assigning-a-value-to-it#:~:text=Using%20the%20None%20keyword&text=It's%20only%20necessary%20to%20use,can%20set%20it%20to%20None.</p>
<h2>Ian Nelson on Stackoverflow.com</h2>
<img src="givenname.png">
<p>This side gave me an indication on how long I could make the name field for the player. 35 was convincing for me.
https://stackoverflow.com/questions/30485/what-is-a-reasonable-length-limit-on-person-name-fields</p>
<h2>Stackoverflow.com</h2>
<p>This site provided information on how to code an exit function by pressing any key
https://stackoverflow.com/questions/11876618/python-press-any-key-to-exit.</p>
