import numpy as np


class MarsRover:
    def __init__(self, obstacles=None):
        """
        The rover starts its journey at the center of the plateau facing north
        The number of possible obstacles in the plateau can vary between 0 and 5
        """
        self.position = np.array([0, 0])
        self.current_direction = np.array([0, 1])
        self.compass_direction = 'N'
        self.compass_direction_dict = {'N': [0, +1],
                                       'E': [+1, 0],
                                       'S': [0, -1],
                                       'W': [-1, 0]}
        if obstacles is None:
            self.generate_obstacles()
        else:
            self.obstacles = obstacles

    def generate_obstacles(self):
        self.obstacles = np.random.randint(5, size=(np.random.randint(0, 6), 2))
        self.obstacles = np.unique(self.obstacles, axis=0).tolist()
        self.obstacles = [obstacles for obstacles in self.obstacles if not (obstacles == [0, 0])]

    def rotation_matrix(self, angle):
        angle = np.radians(-angle)
        return np.array([[np.cos(angle), -np.sin(angle)],
                         [np.sin(angle), np.cos(angle)]])

    def rotate_direction(self, rotation):
        if rotation == 'R':
            return np.dot(self.rotation_matrix(90).astype(int), self.current_direction)
        elif rotation == 'L':
            return np.dot(self.rotation_matrix(-90).astype(int), self.current_direction)
        elif rotation == 'END':
            return np.dot(self.rotation_matrix(180).astype(int), self.current_direction)

    def update_compass_direction(self):
        for key, value in self.compass_direction_dict.items():
            if list(self.current_direction) == value:
                self.compass_direction = key

    def move(self, movement_commands):
        for movement in movement_commands:
            if movement == 'M':
                self.position = self.position + self.current_direction
                if self.obstacles is not None:
                    if any(np.array_equal(obstacle, self.position) for obstacle in self.obstacles):
                        self.position = self.position - self.current_direction
                        return '0:{}:{}:{}'.format(*self.position, self.compass_direction)
                if any(abs(coordinates) > 5 for coordinates in self.position):
                    self.position = self.position - 2*self.current_direction
                    self.current_direction = self.rotate_direction('END')
                    self.update_compass_direction()

            elif movement in ['R', 'L']:
                self.current_direction = self.rotate_direction(movement)
                self.update_compass_direction()
            else:
                exit('{} is a rong input command, rover could not find the correct direction'.format(movement))
        return '{}:{}:{}'.format(*self.position, self.compass_direction)

