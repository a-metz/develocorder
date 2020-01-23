from random import random

from develocorder import LinePlot, set_recorder, record

set_recorder(some_value=LinePlot())

for _ in range(10):
    record(some_value=random())

input("Press Enter to exit...")
