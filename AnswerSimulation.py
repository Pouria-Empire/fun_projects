# build out table based on wich explained in the shared document
patientArrival =[[1,2,3,4],[0.4,0.3,0.19,0.11],[(1,40),(41,70),(71,89),(90,100)]]

patientHealthStatus = [['B','D','A'],[20,5,3],[0.3,0.4,0.3],[(1,30),(31,70),(71,100)]]


table={
    "patient":[],             
    "randomEntranceNumber":[],
    "timeBetweenEntrance":[],
    "simulatedTime":[],
    "randomHealthNumber":[],
    ###################
    ##### بستری ####
    "BPatientID":[],
    "BStartTime":[],
    "BUseTime":[],
    "BEndTime":[],
    ##### درمانگاه ####
    "DPatientID":[],
    "DStartTime":[],
    "DUseTime":[],
    "DEndTime":[],
    #### آزمایشگاه ####
    "APatientID":[],
    "AStartTime":[],
    "AUseTime":[],   
    "AEndTime":[],
    #####################
    'WatingLineTime':[]
}

import random

def fillTable():
    index = 0
    lastDataSelect = () # what is the last type of patient whom accepted
    while(True):      

        #Generate random numbers
        randomEntrance = random.randint(1,100)
        randomHealth = random.randint(1,100)

        # just for first patient we fill the table with 0
        if(index == 0):
            table['patient'].append(1)
            table['randomEntranceNumber'].append(0)
            table['timeBetweenEntrance'].append(0)
            table['simulatedTime'].append(0)
            table['randomHealthNumber'].append(randomHealth)
        else:
            for hIndex,randArrive in enumerate(patientArrival[2]):
                if randomEntrance >= randArrive[0] and randomEntrance <= randArrive[1]:
                    # checking if greater than 12 * 60 = 720 break the loop
                    if (table['simulatedTime'][index-1]+patientArrival[0][hIndex]) > 720:
                        return

                    table['timeBetweenEntrance'].append(patientArrival[0][hIndex]) # fill entrance time
                    table['simulatedTime'].append(table['simulatedTime'][index-1]+patientArrival[0][hIndex]) # fill simulated time

                    break

            table['patient'].append(index+1)
            table['randomEntranceNumber'].append(randomEntrance)
            table['randomHealthNumber'].append(randomHealth)

        # fill the other part
        dataSelect = () # which state is selected

        for vIndex,randHealth in enumerate(patientHealthStatus[3]):
            if randomHealth>=randHealth[0] and randomHealth<=randHealth[1]:
                if(patientHealthStatus[0][vIndex] == 'B'):
                    dataSelect = ('BStartTime','BUseTime','BEndTime','BPatientID')
                elif(patientHealthStatus[0][vIndex] == 'D'):
                    dataSelect = ('DStartTime','DUseTime','DEndTime','DPatientID')
                else:
                    dataSelect = ('AStartTime','AUseTime','AEndTime','APatientID')

                if index == 0:
                    table[dataSelect[0]].append(0)
                    table[dataSelect[1]].append(patientHealthStatus[1][vIndex])
                    table[dataSelect[2]].append(patientHealthStatus[1][vIndex]) # just sum of two before
                    table['WatingLineTime'].append(0)

                else:
                    entranceSimulatedTime = table['simulatedTime'][index]
                    lastEndTask = table[lastDataSelect[2]][-1]
                    diff = lastEndTask - entranceSimulatedTime
                    if(diff <= 0): # no waiting needed
                        table[dataSelect[0]].append(entranceSimulatedTime)
                        b = patientHealthStatus[1][vIndex]
                        table[dataSelect[1]].append(b)
                        table[dataSelect[2]].append(entranceSimulatedTime+b)
                        table['WatingLineTime'].append(0)
                    else:
                        table[dataSelect[0]].append(lastEndTask)
                        b = patientHealthStatus[1][vIndex]
                        table[dataSelect[1]].append(b)
                        table[dataSelect[2]].append(lastEndTask+b)
                        table['WatingLineTime'].append(diff)
                
                break
        table[dataSelect[3]].append(index)
        lastDataSelect = dataSelect
        index += 1

def fillTable2():

    index = 0
    lastDataSelect = () # what is the last type of patient whom accepted
    while(True):      
        randomEntrance = random.randint(1,100)
        randomHealth = random.randint(1,100)

        # just for first patient we fill the table with 0
        if(index == 0):
            table['patient'].append(1)
            table['randomEntranceNumber'].append(0)
            table['timeBetweenEntrance'].append(0)
            table['simulatedTime'].append(0)
            table['randomHealthNumber'].append(randomHealth)
        else:
            for hIndex,randArrive in enumerate(patientArrival[2]):
                if randomEntrance >= randArrive[0] and randomEntrance <= randArrive[1]:
                    # checking if greater than 12 * 60 = 720 break the loop
                    if (table['simulatedTime'][index-1]+patientArrival[0][hIndex]) > 720:
                        return

                    table['timeBetweenEntrance'].append(patientArrival[0][hIndex]) # fill entrance time
                    table['simulatedTime'].append(table['simulatedTime'][index-1]+patientArrival[0][hIndex]) # fill simulated time

                    break

            table['patient'].append(index+1)
            table['randomEntranceNumber'].append(randomEntrance)
            table['randomHealthNumber'].append(randomHealth)


        dataSelect = () # which state is selected

        for vIndex,randHealth in enumerate(patientHealthStatus[3]):
            if randomHealth>=randHealth[0] and randomHealth<=randHealth[1]:
                if(patientHealthStatus[0][vIndex] == 'B'):
                    dataSelect = ('BStartTime','BUseTime','BEndTime','BPatientID')
                elif(patientHealthStatus[0][vIndex] == 'D'):
                    dataSelect = ('DStartTime','DUseTime','DEndTime','DPatientID')
                else:
                    dataSelect = ('AStartTime','AUseTime','AEndTime','APatientID')

                if index == 0:
                    table[dataSelect[0]].append(0)
                    table[dataSelect[1]].append(patientHealthStatus[1][vIndex])
                    table[dataSelect[2]].append(patientHealthStatus[1][vIndex]) # just sum of two before
                    table['WatingLineTime'].append(0)

                else:
                    entranceSimulatedTime = table['simulatedTime'][index]
                    if len(table[dataSelect[2]]):
                        lastEndTask = table[dataSelect[2]][-1]
                    else:
                        lastEndTask = 0
                    diff = lastEndTask - entranceSimulatedTime
                    if(diff <= 0): # no waiting needed
                        table[dataSelect[0]].append(entranceSimulatedTime)
                        b = patientHealthStatus[1][vIndex]
                        table[dataSelect[1]].append(b)
                        table[dataSelect[2]].append(entranceSimulatedTime+b)
                        table['WatingLineTime'].append(0)
                    else:
                        table[dataSelect[0]].append(lastEndTask)
                        b = patientHealthStatus[1][vIndex]
                        table[dataSelect[1]].append(b)
                        table[dataSelect[2]].append(lastEndTask+b)
                        table['WatingLineTime'].append(diff)
                
                break
        table[dataSelect[3]].append(index)
        lastDataSelect = dataSelect
        index += 1



def answerQ1_5(table):
    # print average patient in waiting line:
    import numpy as np
    #calculate avergae waiting time in all data
    waitingLine = np.array(table['WatingLineTime'])
    averageWatingLine = np.sum(waitingLine)/np.count_nonzero(waitingLine)
    print("Average patient waiting time: (hour)"+ str(averageWatingLine/60))
    ##################################
    #calculate avergae waiting time based on health status
    AStatusPatiens = [table['WatingLineTime'][x] for x in table['APatientID'] ]
    BStatusPatiens = [table['WatingLineTime'][x] for x in table['BPatientID'] ]
    DStatusPatiens = [table['WatingLineTime'][x] for x in table['DPatientID'] ]
    averageWatingLineA = np.sum(AStatusPatiens)/np.count_nonzero(AStatusPatiens)
    averageWatingLineB = np.sum(BStatusPatiens)/np.count_nonzero(BStatusPatiens)
    averageWatingLineD = np.sum(DStatusPatiens)/np.count_nonzero(DStatusPatiens)
    
    print("Average patient waiting time in Laboratory: (hour)"+str(averageWatingLineA/60))
    print("Average patient waiting time in clinic: (hour)"+str(averageWatingLineD/60))
    print("Average patient waiting time in Hospitalization: (hour)"+str(averageWatingLineB/60))

    ##################################
    #calculate avergae length of waiting line
    #(Persons who still on line after 12 hours passed) - (persons who accepted)

    personsOnLine = [x for x in table['patient'] if table['WatingLineTime'][x-1] > 720]
    print("Average patient waiting on line: "+str(len(personsOnLine)))
    ##################################
    # draw cdf of waiting line cdf:
    import matplotlib.pyplot as plt
    from matplotlib import mlab
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    count, bins_count = np.histogram(table['WatingLineTime'], bins=100)
    pdf = count / sum(count)
    cdf = np.cumsum(pdf)
    plt.title("CDF of waiting line")
    plt.plot(bins_count[1:], cdf, label="CDF")
    plt.legend()
    plt.show()
    ##################################
    # draw cdf of waiting line cdf based on health status.
    my_bins = 20
    count, bins_count = np.histogram(AStatusPatiens, bins=my_bins)
    pdf = count / sum(count)
    cdf = np.cumsum(pdf)
    plt.title("CDF of waiting line in Laboratory")
    plt.plot(bins_count[1:], cdf, label="CDF")
    plt.legend()
    plt.show()
    count, bins_count = np.histogram(BStatusPatiens, bins=my_bins)
    pdf = count / sum(count)
    cdf = np.cumsum(pdf)
    plt.title("CDF of waiting line in Hospitalization")
    plt.plot(bins_count[1:], cdf, label="CDF")
    plt.legend()
    plt.show()
    count, bins_count = np.histogram(DStatusPatiens, bins=my_bins)
    pdf = count / sum(count)
    cdf = np.cumsum(pdf)
    plt.title("CDF of waiting line in clinic")
    plt.plot(bins_count[1:], cdf, label="CDF")
    plt.legend()
    plt.show()
    ##################################
    # Avarage free time:
    # (Sum of passed time ) - (sum of used time in answering patients)
    # Better to say : for all 0 in waiting line we can say : sum (simulated time - last finished job) = (table['simulatedTime'][i] - table[lastDataSelect[2]][i-1] )
    zeroLine = [x-1 for x in table['patient'] if table['WatingLineTime'][x-1] == 0]
    resulatArray =[0]
    for id in zeroLine:
        if id>0:
            lastJob = 0
            if id in table['APatientID']:
                if(table['APatientID'].index(id) == 0):
                    lastJob = 0
                else:
                    lastJob = table["AEndTime"][table['APatientID'].index(id)-1]
            elif id in table['BPatientID']:
                if(table['BPatientID'].index(id) == 0):
                    lastJob = 0
                else:
                    lastJob = table["BEndTime"][table['BPatientID'].index(id)-1]
            elif id in table['DPatientID']:
                if(table['DPatientID'].index(id) == 0):
                    lastJob = 0
                else:
                    lastJob = table["DEndTime"][table['DPatientID'].index(id)-1]
            resulatArray.append(table['simulatedTime'][id] - lastJob)
    print("Free time of Employee: (hour)"+str(sum(resulatArray)/60))

if __name__ == '__main__':
    fillTable()

    print('...............Table1 made..............')

    answerQ1_5(table)

    # reset table
    table=  {
    "patient":[],             
    "randomEntranceNumber":[],
    "timeBetweenEntrance":[],
    "simulatedTime":[],
    "randomHealthNumber":[],
    ###################
    ##### بستری ####
    "BPatientID":[],
    "BStartTime":[],
    "BUseTime":[],
    "BEndTime":[],
    ##### درمانگاه ####
    "DPatientID":[],
    "DStartTime":[],
    "DUseTime":[],
    "DEndTime":[],
    #### آزمایشگاه ####
    "APatientID":[],
    "AStartTime":[],
    "AUseTime":[],   
    "AEndTime":[],
    #####################
    'WatingLineTime':[]
    }

    fillTable2()

    print('...............Table2 made..............')

    answerQ1_5(table)