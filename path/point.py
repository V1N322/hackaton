import coordinates

class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0, name: str = "", description: str = "", activities: list = [], connections: list = []):
        self.connections = connections
        self.coordinates = coordinates.Letlong(x, y)
        self.name = name
        self.description = description

        self.weight = 3

        self._activity = self._get_activity(activities)

    def add_connection(self, connection):
        self.connections.append(connection)

    def get_weight(self):
        return self.weight

    def get_connections(self):
        return self.connections

    def _get_activity(self, activities: str):
        result = {
            'sport': False,
            'nature': False,
            'rest': False,
            'gastronom': False,
            'architecture': False,
            'local_culture': False
        }

        for activity in activities:
            if activity in result:
                result[activity] = True

        return result
    
    def get_activity(self):
        return self._activity
    
    def get_pos(self):
        return self.coordinates.get()
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def change_weight(self, weight):
        self.weight = weight

    def change_x(self, x):
        self.coordinates.change_x(x)
    
    def change_y(self, y):
        self.coordinates.change_y(y)

    def change_name(self, name):
        self.name = name
    
    def change_description(self, description):
        self.description = description

