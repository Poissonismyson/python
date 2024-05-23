
# (3,0)
# (2,0) (3,1)
# (1,0) (2,1) (3,2)

# (0,0) (1,1) (2,2) (3,3)

# (0,1) (1,2) (2,3)
# (0,2) (1,3)
# (0,3)


def B_Ex2(m):
    result = ""

    for i in range(len(m)-1, -1, -1):
        for col in range(len(m[i])):
            if i+col < len(m) and m[i+col][col] != 0:
                result += str(m[i+col][col])

    for j in range(1, len(m[0])):
        for row in range(len(m[0])):
            if row+j < len(m[0]) and m[row][row+j] != 0:
                result += str(m[row][row+j])
    return result


