## s - t range of house
## a = apple tree location, b = orange tree location
## apples = array of apple locations
## oranges = array of orange locations
## Determine how many apples and oranges fall on the house

def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apples = 0
    total_oranges = 0
    max_len = 0

    if len(apples) >= len(oranges):
        max_len = len(apples)
    else:
        max_len = len(oranges)

    for i in range(max_len):
        if i < len(apples):
            if apples[i] + a >= s and apples[i] + a <= t:
                total_apples += 1
        if i < len(oranges):
            if oranges[i] + b >= s and oranges[i] + b <= t:
                total_oranges += 1

    return total_apples, total_oranges

test_array = 7, 11, 5, 15, [-2, 1, 1], [5, -6]

print(countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6]))