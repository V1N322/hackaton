from path import point

class Connection:
    def __init__(self, weight: float = 0.0, finishPoint: point.Point = None):
        self.weight = weight
        self.finishPoint = finishPoint


    def change_weight(self, weight):
        self.weight = weight

    def change_finishPoint(self, finishPoint):
        self.finishPoint = finishPoint

    def get_weight(self):
        return self.weight

    def get_finishPoint(self):
        return self.finishPoint
    
    def get(self):
        return {
            'weight': self.weight,
            'finishPoint': self.finishPoint
        }
    