#!/usr/bin/env python3

#this is from my AI course on Udemy (reinforcement learning)

import numpy as np
import matplotlib.pyplot as plt

def xrange(X):
    return iter(range(X))

class Bandit:
    def __init__(self, m, upper_limit):
        self.m = m
        self.mean = upper_limit
        self.N = 1
    
    def pull(self):
        return np.random.randn() + self.m

    def update(self, x):
        self.N += 1
        self.mean = (1-1.0/self.N)*self.mean + 1.0/self.N*x

def run_experiment(m1,m2,m3,N, upper_limit=10):
    bandits = [Bandit(m1, upper_limit), Bandit(m2, upper_limit), Bandit(m3, upper_limit)]
    data = np.empty(N)
    for i in xrange(N):
        j = np.argmax([b.mean for b in bandits])
        x = bandits[j].pull()
        bandits[j].update(x)

        #add data to array for plotting
        data[i] = x

    cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

    plt.plot(cumulative_average)
    plt.plot(np.ones(N)*m1)
    plt.plot(np.ones(N)*m2)
    plt.plot(np.ones(N)*m3)
    plt.xscale('log')
    plt.show()

    for b in bandits:
        print(b.mean)

    return cumulative_average

if __name__ == '__main__':
    oiv = run_experiment(1.0, 2.0, 3.0, 100000)

    plt.plot(oiv, label='optimistic')
    plt.legend()
    plt.xscale('log')
    plt.show()
