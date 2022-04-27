import unittest
import numpy as np
from marsrover import MarsRover


class TestExamples(unittest.TestCase):

    def test_1(self):
        perseverance = MarsRover([])
        self.assertEqual(perseverance.move('MMRMMLM'), '2:3:N')

    def test_2(self):
        perseverance = MarsRover([])
        self.assertEqual(perseverance.move('MMMMMMMMMM'), '0:0:S')

    def test_3(self):
        perseverance = MarsRover(obstacles=[[0, 3]])
        self.assertEqual(perseverance.move('MMMM'), '0:0:2:N')