import math
input = []
sum = 0 

with open('day02_input.txt') as file:
    input = file.read().strip().split('\n')

for mass in input:
    current_mass = mass
    while current_mass > 7:
        current_mass = math.floor(int(current_mass)/3) - 2
        sum += current_mass

print(sum)