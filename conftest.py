# this can be used to override various internals.
# we will use it to add to the python path
#
# (useful when we can not set PYTHONPATH)
# (and our code is under some custom directory)

import sys
import os.path

ROOT_DIR = os.path.dirname(__file__)

sys.path.insert(0, ROOT_DIR)
