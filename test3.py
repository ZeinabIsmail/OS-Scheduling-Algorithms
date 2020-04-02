# function for calculating average waiting time
import operator


def AverageWaitingTime(no, lst):
    return Time


def priority(elem):
    return elem[3]


def arrivaltime(elem):
    return elem[1]


def BurstTime(elem):
    return elem[2]


def main():
    Algorithm = input("Enter the type of Algoritm\n")  # Enter type of algorithm
    while Algorithm == "priority schedule":
        Type = input("Type of scheduling\n")  # preemetive or not
        processesNumber = int(input("Enter the number of processes\n"))  # number of rows of matrix
        number_of_columns = 4  # number of columns of matrix
        Mat = []  # create the list
        for i in range(0, processesNumber):
            Mat.append([])  # Create rows in list , row for each process
        for i in range(0, processesNumber):
            for j in range(0, number_of_columns):
                Mat[i].append(j)
                Mat[i][j] = 0
        for i in range(0, processesNumber):
            for j in range(0, number_of_columns):
                if j == 0:
                    print('Name Of Process', i + 1)
                    Mat[i][j] = input()
                if j == 1:
                    print('Arrival Time For Process', i + 1)
                    Mat[i][j] = int(input())
                if j == 2:
                    print('Burst Time For Process', i + 1)
                    Mat[i][j] = int(input())
                if j == 3:
                    print('Priority Number For Process', i + 1)
                    Mat[i][j] = int(input())

        # Sort processes according to their ascending priority
        # ProcessPriority=sorted(Mat,key=priority)
        # print(ProcessPriority)
        # ProcessArrival=sorted(Mat,key=arrivaltime)
        # print(ProcessArrival)
        # ProcessBurst=sorted(Mat,key=BurstTime)
        # print(ProcessBurst)
        Mat.sort(key=operator.itemgetter(1,3))
        #print(Mat)
        if Type == "Non Preemptive":
            arrival = 0;  # initialize minimum arrival time
            priority = Mat[0][3]  # initialzie priority to that of first process in order
            currentProcess = Mat[0]  # initailize process to the first process
            currentRunning = []
            startingList = []
            postedlist = []
            count=0
            index=0
            # check for the same arrival time at 0
            for i in range(1, len(Mat)):
                if Mat[i][1] == 0:
                    startingList.append(Mat[i])
            if len(startingList) == 0:
                currentRunning.append(currentProcess)
                Burst = Mat[0][2]  # initialize burst time as a variable
                BurstCount = Mat[0][2]
                del Mat[0]  # Remove first process from qeueu
                while len(Mat) != 0:
                    waitingList = []
                    for i in range(0, len(Mat)):
                        if Mat[i][1] <= Burst:
                            waitingList.append(Mat[i])

                            index=i

                    if len(waitingList)==0:
                        Burst=Mat[index][1]
                        for i in range(0, len(Mat)):
                            if Mat[i][1] <= Burst:
                                waitingList.append(Mat[i])
                        first = waitingList[0]
                        for i in range(0, len(waitingList)):

                            if waitingList[i][3] < first[3]:
                                first = waitingList[i]
                            elif waitingList[i][3]== first[3] :
                                if waitingList[i][1]<first[1]:
                                    first=waitingList[i]

                        if len(waitingList) == 1:
                            first = waitingList[0]

                        currentProcess = first
                        currentRunning.append(currentProcess)
                        for i in range(0, len(Mat)):
                            if Mat[i] == first:
                                del Mat[i]
                                break
                        Burst = Burst + first[2]
                    else:
                        first = waitingList[0]
                        for i in range(0, len(waitingList)):

                            if waitingList[i][3] < first[3]:
                                first = waitingList[i]
                            elif waitingList[i][3]== first[3] :
                                if waitingList[i][1]<first[1]:
                                    first=waitingList[i]
                        if len(waitingList) == 1:
                            first = waitingList[0]
                        currentProcess = first
                        currentRunning.append(currentProcess)
                        for i in range(0, len(Mat)):
                            if Mat[i] == first:
                                del Mat[i]
                                break
                        Burst = Burst + first[2]

            else:
                startingList.append(Mat[0])
                for i in range(0, len(startingList)):
                    if Mat[i][3] < priority:
                        currentProcess = Mat[i]
                        priority = Mat[i][3]
                currentRunning.append(currentProcess)
                Burst = currentProcess[2]  # initialize burst time as a variable
                for i in range(0, len(Mat)):
                    if Mat[i] == currentProcess:
                        del Mat[i]
                        break
                # Remove first process from qeueu
                while len(Mat) != 0:
                    waitingList = []
                    for i in range(0, len(Mat)):
                        if Mat[i][1] <= Burst:
                            waitingList.append(Mat[i])
                            count=count+1
                            index=i
                    if count==0:
                        Burst=Mat[index][1]
                        for i in range(0, len(Mat)):
                            if Mat[i][1] <= Burst:
                                waitingList.append(Mat[i])
                        first = waitingList[0]
                        for i in range(0, len(waitingList)):

                            if waitingList[i][3] < first[3]:
                                first = waitingList[i]
                            elif waitingList[i][3]== first[3] :
                                if waitingList[i][1]<first[1]:
                                    first=waitingList[i]
                        if len(waitingList) == 1:
                            first = waitingList[0]


                        currentProcess = first
                        currentRunning.append(currentProcess)
                        for i in range(0, len(Mat)):
                            if Mat[i] == first:
                                del Mat[i]
                                break
                        Burst = Burst + first[2]
                    else:
                        first = waitingList[0]
                        for i in range(0, len(waitingList) ):

                            if waitingList[i][3] < first[3]:
                                first = waitingList[i]
                            elif waitingList[i][3]== first[3] :
                                if waitingList[i][1]<first[1]:
                                    first=waitingList[i]

                        if len(waitingList) == 1:
                            first = waitingList[0]


                        currentProcess = first
                        currentRunning.append(currentProcess)
                        for i in range(0, len(Mat)):
                            if Mat[i] == first:
                                del Mat[i]
                                break
                        Burst = Burst + first[2]

            GanttInformation=[]
            for i in range(0,processesNumber):
                GanttInformation.append([])  # Create rows in list , row for each process
            for i in range(0,processesNumber):
                for j in range(0,number_of_columns):
                    GanttInformation[i].append(j)
                    GanttInformation[i][j] = 0

            for i in range(0,processesNumber):
                for j in range(0,number_of_columns):
                    GanttInformation[i][0]=currentRunning[i][0]
                    GanttInformation[i][1]=currentRunning[i][2]
                    if i==0:

                        GanttInformation[i][2]=currentRunning[i][1]
                        GanttInformation[i][3]=currentRunning[i][1]+currentRunning[i][2]
                    else:
                        if currentRunning[i][1]<=GanttInformation[i-1][3]:
                            GanttInformation[i][2] = GanttInformation[i-1][3]
                            GanttInformation[i][3] = GanttInformation[i][2] + GanttInformation[i][1]
                        else:
                            GanttInformation[i][2] = currentRunning[i][1]
                            GanttInformation[i][3] = currentRunning[i][1] + currentRunning[i][2]
                sum=0
                for i in range(0, processesNumber):
                    sum=sum+(GanttInformation[i][3]-currentRunning[i][1]-GanttInformation[i][1])
                averageWaitingTime=sum/3
            print(currentRunning)
            print(GanttInformation)
            print(averageWaitingTime)
        cont = input("Do you want a new process?\n")
        if cont=="yes":
            Algorithm = input("Enter the type of Algoritm\n")  # Enter type of algorithm
            continue
        elif cont=="no":
            break




if __name__ == '__main__': main()