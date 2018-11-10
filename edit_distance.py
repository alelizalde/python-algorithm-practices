def edit_distance(word1, word2):
    distances = [[0] * (len(word1) + 1) for i in range(len(word2) + 1)]

    last_row = len(distances) - 1
    last_col = len(distances[0]) - 1

    distances[last_row][last_col] = 0

    for col in range(last_col):
        distances[last_row][col] = len(word1) - col

    for row in range(last_row):
        distances[row][last_col] = len(word2) - row

    for row in range(last_row - 1, -1, -1):
        for col in range(last_col - 1, -1, -1):
            if word2[row] == word1[col]:
                distances[row][col] = distances[row + 1][col + 1]
            else:
                distances[row][col] = 1 + min(distances[row + 1][col + 1], distances[row + 1][col], distances[row][col + 1])
            print(distances)
    return distances[0][0]


print(edit_distance('horse', 'ros'))