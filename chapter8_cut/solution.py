# Solution from the book repo
# This uses the ',' to select only specified columns whereas '1-3' selects the entire substring inclusive

import sys

_, delim, fields = sys.argv
split_at = [int(x) for x in fields.split(',')]

while True:
    try:
        line = input()
        cuts = line.split(delim)
        for i in split_at:
            print(f"{cuts[i]} ", end="")
        print()

    except EOFError:
        sys.exit(0)
    except IndexError:
        pass