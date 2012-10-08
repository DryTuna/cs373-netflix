#!/usr/bin/env python

"""
To run the program
% python RunNetflix.py < RunNetflix.in > RunNetflix.out
% chmod ugo+x RunNetflix.py
% RunNetflix.py < RunNetflix.in > RunNetflix.out

To document the program
% pydoc -w Netflix
"""

# -------
# imports
# -------

import sys

from Netflix import solve

# ----
# main
# ----

solve(sys.stdin, sys.stdout)
