from path import point
from path import connection

class Way:
    def __init__(self, listOfDictsPointsAndConnections: list = [], weight: float = 0.0):
        self.LODPAC = listOfDictsPointsAndConnections
        self.weight = weight

    def add_segment(self, point, connection):
        self.LODPAC.append({'point': point, 'connection': connection})
        self.weight += connection.get_weight()

    def add_segments(self, segments):
        for segment in segments:
            self.add_segment(segment['point'], segment['connection'])

    def add_weight(self, weight):
        self.weight += weight

    def get_weight(self):
        return self.weight
    
    def get_LODPAC(self):
        return self.LODPAC