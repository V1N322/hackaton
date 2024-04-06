import path

def create_way():
    finishPoint = path.point.Point(999.9, 666.6, 'Футбол', 'Поиграем?', ['sport'], connections=[])
    connection = path.connection.Connection(14.6, finishPoint)

    point = path.point.Point(0.0, 13.8, 'KFC', 'Лучший ресторан по изготовки изжоги и язв', ['rest'], connections=[connection])

    way = path.way.Way()

    way.add_segment(point, connection)
    
    print(way.get_weight(), way.get_LODPAC()[0]['point'].get_name())
    
def main():
    create_way()

if __name__ == '__main__':
    main()