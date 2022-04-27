MarsRover
========
Python api for mars rover exercise from https://katalyst.codurance.com/mars-rover

The api allows ths user to move the rover around a 10x10 plateau and returns the final position of the rover in x y 
coordinates. When the rover faces the end of the plateau it wrap-around. If the rover founds any obstacle it will return 
the last possible position of the rover in the plateau but with an additional 0 at the beginning of the coordinates.

Requirements:
- Numpy
