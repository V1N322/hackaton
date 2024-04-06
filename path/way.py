from path import point
from path import connection
from queue import PriorityQueue


class Way:
    def __init__(self, listOfDictsPointsAndConnections: list = [], weight: float = 0.0):
        self.LODPAC = listOfDictsPointsAndConnections
        self.weight = weight

    def add_segment(self, point, connections):
        self.LODPAC.append({'point': point, 'connection': connections})
        for connection in connections:
            print(self.weight, type(self.weight), connection.get_weight(), type(connection.get_weight()))
            self.weight += connection.get_weight()

    def add_segments(self, segments):
        for segment in segments:
            self.add_segment(segment[0]['point'], segment[0]['connection'])

    def add_weight(self, weight):
        self.weight += weight

    def get_weight(self):
        return self.weight
    
    def get_LODPAC(self):
        return self.LODPAC
    
    def a_star_search(self, start_point, end_point, user_interests):
        # Implement A* search algorithm here
        open_list = [start_point]
        closed_list = []

        input(open_list)

        while open_list:
            current_point = min(open_list, key=lambda x: x.get_weight())
            open_list.remove(current_point)
            closed_list.append(current_point)

            if current_point == end_point:
                return closed_list

            for connection in current_point.get_connections():
                neighbor = connection.get_finishPoint()
                if neighbor in closed_list:
                    continue

                new_weight = current_point.get_weight() + connection.get_weight()
                if neighbor in open_list:
                    if new_weight < neighbor.get_weight():
                        neighbor.change_weight(new_weight)
                else:
                    neighbor.change_weight(new_weight)
                    open_list.append(neighbor)

        return None