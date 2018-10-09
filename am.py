def ClosestXdestinations(numDestinations, allLocations, numDeliveries):

    route = {}
    e = 1
    for distance in allLocations:
        value = (distance[0]**2)+(distance[1]**2)
        route[value] = [distance[0], distance[1]]
        e += 1

    e = 1
    final_route = []
    for k, v in sorted(route.items()):
        final_route.append(v)
        if e >= numDeliveries:
            break
        else:
            e+=1
    pass

    return final_route


def minimumDistance(numRows, numColumns, area):

    if (numRows < 1 and numColumns < 1) or (numRows > 1000 and numColumns > 1000):
        return -1

    path = 1
    for row in range(0, numRows-1):
        for col in range(0, numColumns-1):
            if area[col][row] == 1:
                path += 1
            elif area[col][row] == 1:
                path += 1
            elif area[col][row] == 9:
                path += 1
                return path
    return path


def main():
    print(ClosestXdestinations(3, [[1, -3], [1, 2], [3, 4]], 1))
    print(ClosestXdestinations(6, [[3, 6], [2, 4], [5, 3], [2,7], [1,8], [7,9]], 3))
    print(minimumDistance(3, 3, [[1, 0, 0], [1, 0, 0], [1, 9, 1]]))
    print(minimumDistance(5, 4, [[1,1,1,1],[0,1,1,1],[0,1,0,1],[1,1,9,1],[0,0,1,1]]))

if __name__ == '__main__':
    main()
