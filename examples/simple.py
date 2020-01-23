from random import random

from develocorder import LinePlot, set_recorder, record

set_recorder(my_value=LinePlot())

for _ in range(10):
    record(my_value=random())

input("Press Enter to exit...")
