


# total = 0

# for line in file:
#     total += int(line.rstrip())
    
# print(total)



def find_frequency(file):
    frequency = 0
    number_set = set()

    while True:
        filename = "day1.txt"
        file = open(filename)
        for line in file:
            frequency += int(line.rstrip())
            if frequency in number_set:
                return frequency
            else:
                number_set.add(frequency)
        file.close()
    return frequency

print(find_frequency(file))

