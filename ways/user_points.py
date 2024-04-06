def get_user_points(userActivities, points):

    result = []

    for activity in userActivities:
        for point in points:
            if activity in point.get_activity():
                result+=[point]

    return result