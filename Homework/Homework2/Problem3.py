import numpy as np
import matplotlib.pyplot as plt
import math

x = 2
delx = 0.0001

xPert = x + delx

y = math.exp(x)
yPert = math.exp(xPert)

print("Taking in x value", y - 1)
print("Taking in perturbed x value", yPert - 1)