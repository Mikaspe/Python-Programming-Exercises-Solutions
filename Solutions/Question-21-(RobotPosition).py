from math import sqrt

robot_position = [0, 0]

while True:
    print(robot_position)
    MOVE = input().split()

    if not MOVE:
        break
    elif MOVE[0] == 'UP':
        robot_position[1] += int(MOVE[1])
    elif MOVE[0] == 'DOWN':
        robot_position[1] -= int(MOVE[1])
    elif MOVE[0] == 'LEFT':
        robot_position[0] -= int(MOVE[1])
    elif MOVE[0] == 'RIGHT':
        robot_position[0] += int(MOVE[1])
    else:
        break

DISTANCE = int(round(sqrt(robot_position[0]**2 + robot_position[1]**2)))

print(DISTANCE)
