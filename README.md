# Pacman-Portal

A recreation of the classic arcade game Pac-Man but with a twist. Pac-Man now has the ability to enter/exit portals, similar to the portal mechanic in the game, Portal. This project was written in Python, using the PyCharm IDE. In this project, not all of the features are implemented, such as the portals unfortunately. This was one of my first few exposures to using Python, and despite the flaws, I'm happy with the result.

===============================================================================

Works

-Maze generator works: given a text file with an text-drawn Pac-Man maze, the program creates a maze with working walls/openings
for the player to travel through. 

-Player can control Pac-Man and move within the maze

-Ghosts are presemt and kill the player upon contact

-Dots are scattered within the maze. The player can collect them to increase their score

-Working title screen. The player can start the game and view the high score from there. High scores are saved across playthroughs


===============================================================================

Doesn't Really Work

-Ghosts don't actively search out the player to defeat them; the ghosts are in a set location just bouncing back and forth upon colliding with a wall

-Game does not end when the player collects all the dots (as a result there can only be one high score)

-Portals are not implemented whatsoever

-Extra features such as power pellets, eating ghosts, spawning fruit, etc. from the original game are not implemented.
