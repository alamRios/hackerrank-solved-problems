in_int = int(input())

width = len("{0:b}".format(in_int))

for i in range(1,in_int + 1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))