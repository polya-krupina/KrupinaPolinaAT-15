#n = int(input())
n = int(open('input.txt').readline())
coords = [0, 0]
current_step_length = 1
current_direction = -1
s_from_last_dot = 0
current_coord_index = 0
for i in range(n):
    if s_from_last_dot == current_step_length:
        if current_coord_index:
            current_coord_index = 0
            current_direction *= -1
            current_step_length += 1
        else:
            current_coord_index = 1
        s_from_last_dot = 0
    coords[current_coord_index] += current_direction
    s_from_last_dot += 1
#print(coords[0], coords[1])
open('output.txt','w' ).write(str(coords[0]) + ' ' + str(coords[1]))