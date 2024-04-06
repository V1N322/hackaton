from path import point
from path import way
from path import connection
import json

class WaysBuilder:
    def __init__(self) -> None:
        self.ways = []
        self.data = {}

    def get_from_json(self):
        with open('pointsDB.json') as json_file:
            self.data = json.load(json_file)


    def _convert_to_points_and_connections(self):
        points_and_connections = []

        for item in self.data:
            point = point.Point(item['X'], item['Y'], item['Name'], item['Description'], item['Activities'])

            connections = []
            for neighbor in item['Neighbors']:
                connection = connection.Connection(neighbor['Weight'], point)
                connections.append(connection)

            way_obj = way.Way()
            way_obj.add_segment(point, connections)
            points_and_connections.append(way_obj)

        return points_and_connections

    def generate_ways(self):
        # TODO: Тут будет происходить процесс перебора и поиска наилучшего пути и вывод его в виде списка путей.
        pass