import Arithmos
import numpy as np

size = Arithmos.data.DiscreteVariable("size", ["small", "big"])
height = Arithmos.data.ContinuousVariable("height")
shape = Arithmos.data.DiscreteVariable("shape", ["circle", "square", "oval"])
speed = Arithmos.data.ContinuousVariable("speed")

domain = Arithmos.data.Domain([size, height, shape], speed)

X = np.array([[1, 3.4, 0], [0, 2.7, 2], [1, 1.4, 1]])
Y = np.array([42.0, 52.2, 13.4])

data = Arithmos.data.Table(domain, X, Y)
print(data)
