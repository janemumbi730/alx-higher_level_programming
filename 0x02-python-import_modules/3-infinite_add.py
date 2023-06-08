#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    jm = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            jm += int(arg)
    print(jm)
