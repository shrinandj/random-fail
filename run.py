#!/usr/bin/env python

import random
import sys

failPercent = 50
if len(sys.argv) > 1:
    failPercent = int(sys.argv[1])
result = random.randint(1, 100)
print "Result is: " + str(result) + " / " + str(failPercent)
if result <= failPercent:
    sys.exit(1)
else:
    sys.exit(0)
