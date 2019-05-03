# artificial intelligence > bot building > bot saves princess

#!/bin/python

def displayPathtoPrincess(n,grid):
    m_cords = [0,0]
    p_cords = [0,0]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'p':
                p_cords = [row,col]
            elif grid[row][col] == 'm':
                m_cords = [row,col]
    while m_cords[0] != p_cords[0]:
        if m_cords[0] < p_cords[0]:
            m_cords[0] += 1
            print('RIGHT')
        else:
            m_cords[0] -= 1
            print('LEFT')
    while m_cords[1] != p_cords[1]:
        if m_cords[1] < p_cords[1]:
            m_cords[1] += 1
            print('DOWN')
        else:
            m_cords[1] -= 1
            print('UP')
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)