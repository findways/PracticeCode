# S. Pickard
# July 2016
# (Using python 3.4.4, and brian2 2.0rc)
#
# DESCRIPTION
#   Function/method that produces an output vector of averaged spike counts across neurons per time step
#   This analysis was inspired by Lazar et al.(2009) Figure 5.b
#   Goal is to find how many spikes occur in the network for each sub time interval

import numpy as np

def count_distribution(NeuCountArray):
    """
    FUNCTION DESCRIPTION
        This function takes as input a N-D numpy.array of spike times, and outputs a spike count vector; the spike
        counts are averaged over a user defined interval

    :param NeuCountArray: N-D numpy.array, units are seconds, neuron spike times for each neuron stored in an numpy.array
    """


NeuCountArray = ([0, 0, 1, 0, 0, 0, 1, 1, 0, 1],[0, 0, 1, 2, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 1, 0, 1])

#Spike times array turned into a numpy array
NeuCountArray = np.array(NeuCountArray)
print(NeuCountArray)


# SpikeCountDist = []     #Initialize array to collect the number of spikes occuring wihtin each subinterval

SpikeCountDist = np.mean(NeuCountArray, axis = 0)
print (SpikeCountDist)

# return (SpikeCount, splitInterval)
