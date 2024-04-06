import path
from dataBase import waysInterface
import _private_dirs

def create_way():
    finishPoint = path.point.Point(999.9, 666.6, 'Футбол', 'Поиграем?', ['sport'], connections=[])
    connection = path.connection.Connection(14.6, finishPoint)

    point = path.point.Point(0.0, 13.8, 'KFC', 'Лучший ресторан по изготовки изжоги и язв', ['rest'], connections=[connection])

    way = path.way.Way()

    way.add_segment(point, connection)
    
    print(way.get_weight(), way.get_LODPAC()[0]['point'].get_name())

def json_test():
    db = waysInterface.WaysBuilder(_private_dirs.JSON_DB)
    db.get_from_json()

    print(db.data)

    db._convert_to_points_and_connections()
    print(db.ways)

def test_way_class():
    # Create some points and connections
    start_point = path.point.Point(0.0, 0.0, 'Start', 'Starting Point', ['start'], connections=[])
    end_point = path.point.Point(10.0, 10.0, 'End', 'Ending Point', ['end'], connections=[])
    
    connection1 = path.connection.Connection(5.0, end_point)
    connection2 = path.connection.Connection(2.0, end_point)
    connection3 = path.connection.Connection(3.0, end_point)
    
    start_point.add_connection(connection1)
    start_point.add_connection(connection2)
    start_point.add_connection(connection3)
    
    way = path.way.Way()
    way.add_segment(start_point, [connection1, connection2, connection3])
    
    result = way.a_star_search(start_point, end_point, ['end'])
    
    if result:
        print("A* search successful. Path found:")
        for point in result:
            print(point.get_name())
    else:
        print("A* search failed. No path found.")

def test_sambiu_krutou_putb():
    db = waysInterface.WaysBuilder(_private_dirs.JSON_DB)
    db.get_from_json()

    print(db.data)

    db._convert_to_points_and_connections()
    print(db.ways)

    db.generate_ways(['sport'], 'KFC', 'Finish')

def main():
    # json_test()
    # create_way()
    test_way_class()
    # test_sambiu_krutou_putb()


if __name__ == '__main__':
    main()