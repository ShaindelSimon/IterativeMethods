from colors import bcolors


def linearInterpolation(table_points, point):
    """This function check the behavior of the function at point that is not in the table_points
    :param table_points: table of points which are in the function
    :param point: the point to interpolate- A point that is not in the table, and we would like to evaluate the behavior
     of the function at this point
    :return: None
    """
    #p = []
    result = 0
    flag = 1
    """for i in range(len(table_points)):
        p.append(table_points[i][0])"""
    for i in range(len(table_points) - 1):
        # linear interpolation is just for point that in range of table point
        if i <= point <= i + 1:
            x1 = table_points[i][0]
            x2 = table_points[i + 1][0]
            y1 = table_points[i][1]
            y2 = table_points[i + 1][1]
            result = (((y1 - y2) / (x1 - x2)) * point) + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            print(bcolors.OKGREEN, "\nThe approximation (interpolation) of the point ", point, " is: ", bcolors.ENDC, round(result, 4))
            return 1

    print("The point is not between table_points values, check with another method")
    return 0

if __name__ == "__main__":
    linearInterpolation(
        [
            [-5, 7],
            [-1, 4],
        ],
        10
    )



