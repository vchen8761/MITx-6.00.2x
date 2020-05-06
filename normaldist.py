import pylab
import random

dist = []
for i in range(100000):
    dist.append(random.gauss(0,30))
pylab.hist(dist, 30)
pylab.show()
