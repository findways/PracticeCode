import numpy as np
import itertools

##Mock data is collected over a time horizon of 0-1sec
##Goal is to find how many spike occur in each sub time interval

##Run time - specified by user for the simulation
duration = 5    #units: seconds
##Practice spike time array; this array output consists of the number of spikes occuring in the network for each time
## subinterval
time = [.1, 1.3, 1.4, 2.2, 2.7, 3.5, 4.3, 4.4]
# time = [0, 0.55555556,1.11111111,1.66666667,2.22222222,2.77777778, 3.33333333,3.88888889,4.44444444,5]
time = np.array(time)       #make time list an array
print ('time = ', time)
#Interval array - intervals in which to break up the time array - sub time interval array
dt = .2                                     #User defined time interval in to which count spikes over
n = duration/dt                             #How many subintervals from time horizun results from user defined interval
print (n)
splitInterval = np.linspace(0,duration, n+1)    #Generate a interval array to find the number of spikes occuring in each
print ('splitInterval: ', splitInterval)

##Trying different lengths over which to iterate in for loop
# length_splitInt = len(splitInterval)
# print ('length splitInterval: ', length_splitInt)
# length_time = len(time)
# print ('length time: ',length_time)
# length = length_splitInt + (length_time)
# print ('length :', length)

i=0     #inex for for subinterval (length of splitInterval)
j=0     #index for splitInterval array.
k = 0   #index for new matrix that will store the grouped values from the split time array

counter = 0
SpikeCount = []

for i in range(len(splitInterval):
    if (time[k] >= splitInterval[j]) and (time[k] <= splitInterval[j + 1]):
        print ('time element: ', time[k])
        print ('splitInt: ', splitInterval[j], splitInterval[j+1])
        counter += 1
        print('if counter: ', counter)
        i += 1
        print('i: ', i)
        if k > len(time - 1):
            print ('k:time element: ', k,time)
            counter = 0
            SpikeCount.append(counter)
            print(SpikeCount)
            print('k: ', k)
            print('stop k count')
        else:
            k+=1
            print ('if if k: ', k)
    else:
        SpikeCount.append(counter)
        print(SpikeCount)
        print('time element: ', time[k])
        print('splitInt: ', splitInterval[j], splitInterval[j + 1])
        counter = 0
        print('else counter: ', counter)
        j += 1
        print('j: ', j)
        i+=1
        print('i: ', i)
        print ('k: ', k)



SpikeCount.append(counter)
print('Spike count: ', SpikeCount)
print (len(SpikeCount))






