from path import point
from path import way
from path import connection
import json

class WaysBuilder:
    def __init__(self, pathToJson ) -> None:
        self.pathToJson = pathToJson
        self.ways = []
        self.userWay = None
        self.data = {}

    def get_from_json(self):
        with open(self.pathToJson) as json_file:
            self.data = json.load(json_file)


    def _convert_to_points_and_connections(self):
        points_and_connections = []

        for item in self.data:
            pointItem = point.Point(item['X'], item['Y'], item['Name'], item['Description'], item['Activities'])

            connections = []
            for neighbor in item['Neighbors']:
                connectionItem = connection.Connection(neighbor['Weight'], point)
                connections.append(connectionItem)

            way_obj = way.Way()
            way_obj.add_segment(pointItem, connections)
            points_and_connections.append(way_obj)

        self.ways = points_and_connections

    def get_point_by_name(self, name):
        for way in self.ways:
            for point in way.get_LODPAC():
                if point['point'].get_name == name:
                    input(f'Я нашел имя: {name}')
                    return way


    def generate_ways(self, userActivities, nameStart, nameFinish):
        self.ways[0].a_star_search(self.get_point_by_name(nameStart), self.get_point_by_name(nameFinish), userActivities)
        