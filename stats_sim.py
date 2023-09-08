import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.special
import math

def draw_bar(x, y):
    x_axis = np.array(x)
    y_axis =np.array(y)
    plt.bar(x_axis, y_axis)
    plt.show()

def coin_toss_sim(num_times):
    num_heads = 0
    num_tails = 0
    for i in range(num_times):
        if random.randint(0,1) == 0:
            num_heads += 1
        else:
            num_tails += 1
    
    draw_bar(["Heads", "Tails"], [num_heads, num_tails])
    
def bin_to_normal(p, n):
    list_of_outcomes = []
    indices = []
    for i in range(n+1):
        list_of_outcomes.append(scipy.special.binom(n, i) * math.pow(p, i) * math.pow(1-p, n - i))
        indices.append(i)
        
    draw_bar(indices, list_of_outcomes)
    
def poisson_to_normal(l, limit):
    list_of_outcomes = []
    indices = []
    for i in range(limit+1):
        list_of_outcomes.append((math.pow(l, i) * math.pow(math.e, -l)) / (math.factorial(i)))
        indices.append(i)
    
    draw_bar(indices, list_of_outcomes)
    
