from marsrover import MarsRover

print('The landing in the surface of Mars was succesfully completed!\n'
      'The rover is at the center of the plateau facing north.')
commands = input('Now introduce the sequence of rover commands without any space between them.\n'
                 'If the rover finds any obstacle it will return the last possible position at the plateau '
                 'with a 0 at the beginning\n\n'
                 'M: move forward one unit.\nR: turn to the right\nL: turn to the left\n\n')

perseverance = MarsRover()
print(perseverance.move(commands))
