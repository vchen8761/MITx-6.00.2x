import pylab
import random

dist = []
for i in range(100000):
    dist.append(random.gauss(0,30))
    # random.gauss
    # arg1: mu (mean)
    # arg2: sigma (std dev)
pylab.hist(dist, 30)
pylab.show()

"""
Normal distributions peak at mean and fall off symmetrically

"""
