import numpy as np
import matplotlib.pyplot as plt

raw_data = []
with open('20160801.txt','r') as file:
    for line in file:
        raw_data.append(line.split(','))

print(raw_data[:10])