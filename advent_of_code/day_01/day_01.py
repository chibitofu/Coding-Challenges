import math
with open('day_01_input.txt') as file:
    mass_array = file.read().strip().split('\n')
    sum = 0
    
    for mass in mass_array:
        sum += math.floor(int(mass)/3) - 2
    
    print(sum)