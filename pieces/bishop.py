from grid import Grid
from house import House
from pieces.piece import Piece

from utils.trace_line import trace_attack_line

class Bishop(Piece):

    def __init__(self, grid: Grid, location: House, team: int):
        self.location = location

        self.grid = grid
        self.grid.add_content(location, self)
        
        self.team = team


    def __str__(self):
        return "3"

    def set_location(self, location: House):
        self.location = location

    def get_legal_moves_position(self):
        movment_range = 999
        positions = []

        positions.extend(trace_attack_line(self.grid, self.location, (1,1), movment_range, self.team))
        positions.extend(trace_attack_line(self.grid, self.location, (-1,-1), movment_range, self.team))
        positions.extend(trace_attack_line(self.grid, self.location, (-1,1), movment_range, self.team))
        positions.extend(trace_attack_line(self.grid, self.location, (1,-1), movment_range, self.team))

        return positions