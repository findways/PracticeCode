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
# length_splitInt = len(splitInterval)
# # print ('length splitInterval: ', length_splitInt)
# length_time = len(time[0])
# # print ('length time: ',length_time)
# length = length_splitInt + ((length_time)-2)
# # print ('length :', length)


row=0
col=0     #inex for for subinterval (length of splitInterval)
j=0     #index for splitInterval array.
k = 0   #index for new matrix that will store the grouped values from the split time array
n = 0   #row tracker
counter = 0
SpikeCount = [[] for col in range(len(time))]



for row in range(len(time)+1):
    print ('row: ', row)
    if row < (len(time)):
        print ('len(time[row]: ', len(time))
        for col in range(len(splitInterval) + len(time[row])-2):
            print ('col: ', col)
            # print('time[row][k]: ', time[row][k])
            if (col==0) and (time[row][col] == splitInterval[0]):
                counter += 1
                col += 1
                print('col if: ', col)
                print('should happen once')
                print('SpikeCount: ', SpikeCount)
                #Spot check
                print('if counter: ', counter)
                print('time element: ', time[row][k])
                print('splitInt: ', splitInterval[j], splitInterval[j + 1])
                print('if k: ', k)
                print('len(time[:row]): ', len(time[row]))

                if k < (len(time[row])):
                    k += 1

                    # Spot check
                    print('iff k: ', k)
                    print('iff counter: ', counter)
                    print('SpikeCount: ', SpikeCount)
                else:
                    j += 1
                    # Spot check

                    print('iff counter: ', counter)
                    print('SpikeCount: ', SpikeCount)
                    print('iff j: ', j)

            elif (k<= len(time[row])) and (time[row][k] > splitInterval[j]) and (time[row][k] <= splitInterval[j + 1]):
                counter += 1
                col += 1

                #Spot check
                print('elif counter: ', counter)
                print('SpikeCount: ', SpikeCount)
                print('time element: ', time[row][k])
                print('splitInt: ', splitInterval[j], splitInterval[j + 1])
                print('col: ', col)
                print('elif k: ', k)
                print ('len(time[row]): ', len(time[row]))
                print('row: ', row)

                if k < (len(time[row])):
                    k += 1

                    # Spot check
                    print('elifif k: ', k)
                    print('elifif counter: ', counter)
                    print('elifif col: ', col)
                else:
                    j += 1
                    # Spot check
                    print ('row: ', row)
                    SpikeCount[row].append(counter)
                    print('elseif counter: ', counter)
                    print('SpikeCount: ', SpikeCount)
                    print('elseif j: ', j)


            else:
                SpikeCount[row].append(counter)
                counter = 0
                j += 1
                col+=1

                #Spot Check
                print('else counter: ', counter)
                print('SpikeCount: ', SpikeCount)
                print('time element: ', time[row][k])
                # print('splitInt: ', splitInterval[j], splitInterval[j + 1])
                print('else j: ', j)
                print('else col: ', col)
                print ('else k: ', k)
                print('else row: ', row)



#
    else:
        row += 1
        break




SpikeCount.append(counter)
print('Spike count: ', SpikeCount)
print (len(SpikeCount))












