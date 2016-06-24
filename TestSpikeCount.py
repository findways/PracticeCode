#Updated 6/13/16

import numpy as np
import itertools

##Mock data is collected over a time horizon of 0-1sec
##Goal is to find how many spike occur in each sub time interval

##Run time - specified by user for the simulation
duration = 5    #units: seconds


##Practice spike time array; this array output consists of the number of spikes occuring in the network for each time
## subinterval
time = ([0, 1.3, 1.4, 2.2, 2.7, 3.5, 4.3],[.1, 1.3, 1.4, 2.2, 2.7, 3.5, 4.3, 4.4], [0, 1.3, 1.4, 2.2, 2.7, 3.5, 4.3, 4.4])
# time = [1.80000000e-03, 2.00000000e-03, 2.10000000e-03, 9.99850000e+00, 9.99910000e+00, 9.99980000e+00]
# time = [0, 0.55555556,1.11111111,1.66666667,2.22222222,2.77777778, 3.33333333,3.88888889,4.44444444,5]
time = np.array(time)       #make time list an array
# print ('time = ', time)

#Interval array - intervals in which to break up the time array - sub time interval array
dt = 2                                     #User defined time interval in to which count spikes over
n = duration/dt                             #How many subintervals from time horizun results from user defined interval
# print (n)
splitInterval = np.linspace(0,duration, n+1)    #Generate a interval array to find the number of spikes occuring in each
# print ('splitInterval: ', splitInterval)
# splitInterval = ([0, 2.5, 5], [0, 2.5, 5], [0, 2.5, 5])
# splitInterval = np.array(splitInterval)
# print ('splitInterval: ', splitInterval)

##Trying different lengths over which to iterate in for loop
length_splitInt = len(splitInterval)
# print ('length splitInterval: ', length_splitInt)
length_time = len(time[0])
# print ('length time: ',length_time)
length = length_splitInt + ((length_time)-2)
# print ('length :', length)


h=0
i=0     #inex for for subinterval (length of splitInterval)
j=0     #index for splitInterval array.
k = 0   #index for new matrix that will store the grouped values from the split time array
n = 0   #row tracker
counter = 0
SpikeCount = []

# print ('time element: ', time[3,0])
# print ('length of row: ', len(time))
# print ('len(time[0]): ', len(time[0]))
leng = len(time)
# print ('leng: ', leng)
# print ('len(time[h:]): ', len(time[h:]))

for h in range(leng+1):
    print ('h: ', h)
    # counter = 0
    if h < (leng):
        print ('len(time[h][]: ', leng)
        for i in range(len(splitInterval) + len(time[h])-1):
            print ('i: ', i)
            if (i==0) and (time[h][i] == splitInterval[0]):
                counter += 1
                i += 1
                print('i if: ', i)
                print('should happen once')

                #Spot check
                print('if counter: ', counter)
                print('time element: ', time[h][k])
                print('splitInt: ', splitInterval[j], splitInterval[j + 1])
                print('if k: ', k)
                print('len(time[:i]) - 1: ', len(time[i]) - 1)
                if k < (len(time[h]) - 1):
                    k += 1

                    # Spot check
                    print('iff k: ', k)
                    print('iff counter: ', counter)
                else:
                    j += 1
                    # Spot check

                    print('iff counter: ', counter)
                    print(SpikeCount)
                    print('iff j: ', j)

            elif (time[h][k] > splitInterval[j]) and (time[h][k] <= splitInterval[j + 1]):
                counter += 1
                i += 1

                #Spot check
                print('elif counter: ', counter)
                print('time element: ', time[h][k])
                print('splitInt: ', splitInterval[j], splitInterval[j + 1])
                print('i: ', i)
                print('elif k: ', k)

                if k < (len(time[h])-1):
                    k += 1

                    # Spot check
                    print('elifif k: ', k)
                    print('elifif counter: ', counter)
                    print('elifif i: ', i)
                else:
                    j += 1
                    # Spot check
                    SpikeCount.append(counter)
                    print('elseif counter: ', counter)
                    print(SpikeCount)
                    print('elseif j: ', j)


            else:
                SpikeCount.append(counter)
                counter = 0
                j += 1
                i+=1

                #Spot Check
                print('else counter: ', counter)
                print(SpikeCount)
                print('time element: ', time[h][k])
                # print('splitInt: ', splitInterval[j], splitInterval[j + 1])
                print('else j: ', j)
                print('else i: ', i)
                print ('else k: ', k)
                print('else h: ', h)
                h+=1
#
    else:
        break




SpikeCount.append(counter)
print('Spike count: ', SpikeCount)
print (len(SpikeCount))












