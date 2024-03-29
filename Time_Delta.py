#!/bin/python3

from datetime import datetime as fff

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    return int(abs((fff.strptime(t1, format) - 
                    fff.strptime(t2, format)).total_seconds()))

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)

