# For visualizing graphs
import pylab as plt

# List of function values
x_values = []
linear = []
quadratic = []
cubic = []
exponential = []

# Range of 0-29
for i in range(0,30):
    x_values.append(i)
    linear.append(i)
    quadratic.append(i**2)
    cubic.append(i**3)
    exponential.append(1.5**i)

# Use pylab to plot function in individual figures
# plt.figure('lin')
# Clear plot figure
#plt.clf()
#plt.ylim(0,1000)
#plt.title('Linear')
#plt.xlabel('sample points')
#plt.ylabel('linear function')
#plt.plot(x_values, linear)
#
#plt.figure('quad')
#plt.ylim(0,1000)
#plt.title('Quadratic')
#plt.xlabel('sample points')
#plt.ylabel('quadratic function')
#plt.plot(x_values, quadratic)

#plt.figure('cube')
#plt.plot(x_values, cubic)

#plt.figure('exp')
#plt.plot(x_values, exponential)

# Plotting multiple functions in one figure
# plt.plot arg3 is style
# subplots for two figures in one windows (nrows, ncol, index)
#plt.figure('lin quad')
#plt.clf()
#plt.subplot(211)
#plt.title('Linear vs Quadratic')
#plt.ylim(0,900)
#plt.plot(x_values, linear, 'b-', label = 'linear', linewidth = 2.0)
#plt.subplot(212)
#plt.ylim(0,900)
#plt.plot(x_values, quadratic, 'ro',label = 'quadratic', linewidth = 3.0)
#plt.legend(loc = 'upper left')


#plt.figure('cube expo')
#plt.clf()
#plt.title('Cubic vs Exponential')
#plt.subplot(121)
#plt.ylim(0, 140000)
#plt.plot(x_values, cubic, 'g^',label = 'cubic', linewidth = 4.0)
#plt.subplot(122)
#plt.ylim(0, 140000)
#plt.plot(x_values, exponential, 'r--',label = 'exponential', linewidth = 5.0)
#plt.legend()


#plt.figure('cube expo log')
#plt.clf()
#plt.title('Cubic vs Exponential')
#plt.plot(x_values, cubic, 'g^',label = 'cubic', linewidth = 4.0)
#plt.plot(x_values, exponential, 'r--',label = 'exponential', linewidth = 5.0)
#plt.yscale('log')
#plt.legend()
#
#plt.figure('cube expo lin')
#plt.clf()
#plt.title('Cubic vs Exponential')
#plt.plot(x_values, cubic, 'g^',label = 'cubic', linewidth = 4.0)
#plt.plot(x_values, exponential, 'r--',label = 'exponential', linewidth = 5.0)
#plt.legend()

# Example
def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1+mRate) + monthly]
    return base, savings

def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, 
                label = 'retire:' + str(monthly))
        plt.legend(loc = 'upper left')

def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, 
                label = 'retire:' + str(month) + ':' + str(int(rate*100)))
        plt.legend(loc = 'upper left')

def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, 
                monthLabel+rateLabel, label = 'retire:' + str(monthly) + ':' + str(int(rate*100)))
            plt.legend(loc = 'upper left')
# displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40* 12)

# displayRetireWRates(800, [.03, .05, .07], 40* 12)

displayRetireWMonthsAndRates([500, 700, 900, 1100],
                             [.03, .05, .07],
                             40* 12)
plt.show()


