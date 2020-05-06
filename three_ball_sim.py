import random

def noReplacementSimulation(numTrials):
    count = 0
    for x in range(numTrials):
        bucket = ['r','r','r','g','g','g']
        for pull in range(3):
            ball = random.choice(bucket)
            bucket.remove(ball)
        if all(element == 'r' for element in bucket) or all(
                element == 'g' for element in bucket):
           count += 1
    return count/numTrials

print(noReplacementSimulation(1000))
