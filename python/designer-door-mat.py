N,M = tuple(input().split())
M = int(M)
N = int(N)
decorator = '.|.'
message = 'WELCOME'
fill = '-'

n_decorators = 1
middle_row = int(N/2)

for row in range(N - 1):
    if row == middle_row:
        print(message.center(M,fill))
        n_decorators -= 2
        print((decorator*n_decorators).center(M,fill))
        n_decorators -= 2
    else:
        print((decorator*n_decorators).center(M,fill))
        if row > middle_row:
            n_decorators -= 2
        else:
            n_decorators += 2
