#!/usr/bin/env python3

import sys
import discount

if __name__ == "__main__":
    print("Version:", sys.version)
    d = dir(discount)
    print(d)
    for i in d:
        print(i, ":", getattr(discount, i))

else:
    raise Exception("Error: imported __main__ as module")
