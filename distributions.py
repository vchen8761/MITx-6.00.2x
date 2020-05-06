# From MIT Lecture Handout
import pylab, random

#dist = []
#for i in range(100000):
#    dist.append(random.gauss(0,30))
#    # random.gauss
#    # arg1: mu (mean)
#    # arg2: sigma (std dev)
#pylab.hist(dist, 30)
#pylab.show()

"""
Normal distributions peak at mean and fall off symmetrically

"""

import scipy.integrate

def gaussian(x, mu, sigma):
    factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2

def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu =', mu, 'and sigma =', sigma)
        for numStd in (1, 1.96, 3):
            area = scipy.integrate.quad(gaussian, 
                    mu-numStd*sigma,
                    mu+numStd*sigma,
                    (mu, sigma))[0]
            print(' Fraction within', numStd, 'std =', round(area, 4))

# checkEmpirical(3)

#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
#set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

#L = [1,1,1,1,2]
#pylab.hist(L)
#factor = pylab.array(len(L)*[1])/len(L)
#print(factor)
#pylab.figure()
#pylab.hist(L, weights = factor)
#pylab.show()

def plotMeans(numDice, numRolls, numBins,legend, color, style):
    means = []
    for i in range(numRolls//numDice):
        vals = 0
        for j in range(numDice):
            vals += 5*random.random()
        means.append(vals/float(numDice))
    pylab.hist(means, numBins, color = color, label = legend,
            weights = pylab.array(len(means)*[1])/len(means),
            hatch = style)
    return getMeanAndStd(means)

mean, std = plotMeans(1, 100000, 19, '1 die', 'b', '*')
print('Mean of rolling 1 die =', str(mean) + ',', 'Std =', std)
mean, std = plotMeans(50, 1000000, 19, 'Mean of 50 dice', 'r', '//')
print('Mean of rolling 50 dice =', str(mean) + ',', 'Std =', std)
pylab.title('Rolling Continuous Dice')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()
pylab.show()
