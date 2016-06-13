import numpy as np

#Mock data is collected over a time horizon of 0-1sec
#Goal is to find how many spike occur in each sub time interval

#Run time - specified by user for the simulation
duration = 5
#Spike time array
# time = [.1, 1.3, 1.4, 2.2, 2.7, 3.5, 4.3, 4.4, 6.1, 7.6, 8.4, 8.4, 9.5, 9.9]
time = [0, 0.55555556,1.11111111,1.66666667,2.22222222,2.77777778, 3.33333333,3.88888889,4.44444444,5]
time = np.array(time)
print ('time = ', time)
#Interval array - intervals in which to break up the time array - sub time interval array
dt = .2                                     #User defined time interval in to which count spikes over
n = duration/dt                             #How many subintervals from time horizun results from user defined interval
print (n)
splitInterval = np.linspace(0,duration, n+1)    #Generate a interval array to find the number of spikes occuring in each
print ('splitInterval: ', splitInterval)                                                #interval
length_splitInt = len(splitInterval)
length_time = len(time)
length = length_splitInt + (length_time-2)
print ('length :', length_splitInt)

i=0     #inex for for subinterval (length of splitInterval)
j=0     #index for splitInterval array.
k = 0   #index for new matrix that will store the grouped values from the split time array

counter = 0
SpikeCount = []

for i in range(length):
    if (time[k] >= splitInterval[j]) and (time[k] <= splitInterval[j + 1]):
        print ('time element: ', time[k])
        print ('splitInt: ', splitInterval[j], splitInterval[j+1])
        counter += 1
        print('if counter: ', counter)
        i += 1
        k+=1
        print ('k: ', k)
        print('i: ', i)
    else:
        SpikeCount.append(counter)
        print (SpikeCount)
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






