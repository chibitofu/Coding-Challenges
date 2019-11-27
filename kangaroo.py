def kangaroo(input):
    time_X = (input[0], input[1])
    time_Y = (input[2], input[3])

    if time_X[0] < time_Y[0] and time_X[1] < time_Y[1]:
        return "NO"
    else:
        sum_X = time_X[0]
        sum_Y = time_Y[0]
        while True:
            if sum_X == sum_Y:
                return "YES"

            sum_X += time_X[1]
            sum_Y += time_Y[1]

            if sum_X * 2 < sum_Y or sum_Y * 2 < sum_X:
                return "NO"

jumps = [0, 2, 5, 3]

print(kangaroo(jumps))