#!/usr/bin/python3
from sys import argv
__name__ == "__main__"
if len(argv) == 1:
    print("0 arguments.")
else:
    print("{} argments:".format(len(argv) - 1))
    for x in range(1, len(argv)):
        print("{}: {}".format(x, argv[x]))
