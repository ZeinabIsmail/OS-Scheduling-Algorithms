import operator
def priority(elem):
    return elem[3]
def arrivaltime(elem):
    return elem[1]
def BurstTime(elem):
    return elem[2]

################################################ Non-Preemptive SJF  #################################
class SJF:

    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))

            arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))

            burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
            temporary.extend([process_id, arrival_time, burst_time, 0])
            '''
            '0' is the state of the process. 0 means not executed and 1 means execution complete
            '''
            process_data.append(temporary)
        SJF.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        '''
        Sort processes according to the Arrival Time
        '''
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []
            '''
                 # if current time less than or equal arrival time of the process put it in the ready queue 
                                         else put it in the normal queue
            '''

            for j in range(len(process_data)):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][3] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    normal_queue.append(temp)
                    temp = []  #

            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                '''
                Sort the processes according to the Burst Time
                '''
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)

            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):  # lw process excuted change status from 0 to 1
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)

        t_time = SJF.calculateTurnaroundTime(self, process_data)
        w_time = SJF.calculateWaitingTime(self, process_data)
        SJF.printData(self, process_data, t_time, w_time)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][4] - process_data[i][1]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        average_turnaround_time = total_turnaround_time / no_of_processes
        '''
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][5] - process_data[i][2]
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        '''
        average_waiting_time = total_waiting_time / no_of_processes
        '''
        return average_waiting_time

    '''
  def printData(self, process_data, average_turnaround_time, average_waiting_time):
      process_data.sort(key=lambda x: x[4])
      Sort processes according to the Process completation time
        headers = ["Process ID", "Arrival Time", "Burest Time", "Completed", "Completation Time", "Turnaround_Time", "Waiting_Time"]
        print(tabulate(process_data, headers=headers))
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
    '''

    def printData(self, process_data, average_turnaround_time, average_waiting_time):
        process_data.sort(key=lambda x: x[0])
        '''
        Sort processes according to the Process ID
        '''
        print("Process_ID  Arrival_Time  Burst_Time      Completed  Completion_Time  Turnaround_Time  Waiting_Time")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="				")
            print()

        #print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')
################################################ preemptive priority #################################
Mat = []
global prearrival
prearrival = []
global current_running
current_running = []
temp = []
def PrioprocessCreate(processesNumber):
    number_of_columns = 4  # number of columns of matrix
    for i in range(0, processesNumber):
        temp.append([])  # Create rows in list , row for each process
    for i in range(0, processesNumber):
        for j in range(0, number_of_columns):
            temp[i].append(j)
            temp[i][j] = 0
    for i in range(0, processesNumber):
        Mat.append([])  # Create rows in list , row for each process
    for i in range(0, processesNumber):
        for j in range(0, number_of_columns):
            Mat[i].append(j)
            Mat[i][j] = 0
    print("Done number\n")
def Prioinput(ProcessID, ArrivalTime, BurstTime, Priority):
    Mat[ProcessID - 1][0] = temp[ProcessID - 1][0] = ProcessID
    Mat[ProcessID - 1][1] = temp[ProcessID - 1][1] = ArrivalTime
    Mat[ProcessID - 1][2] = temp[ProcessID - 1][2] = BurstTime
    Mat[ProcessID - 1][3] = temp[ProcessID - 1][3] = Priority

    print(Mat[ProcessID - 1])
depsum = 0
current_running = []
def preemptive_priority(processesNumber):
    Mat.sort(key=operator.itemgetter(1, 3))
    m_sum = 0
    for i in range(0, processesNumber):
        m_sum = m_sum + Mat[i][2]
        if i==processesNumber-1:
            if temp[i][1]> temp[i-1][1]+m_sum:
                m_sum = temp[i+1][1] -temp[i][1]
        else:
            if temp[i+1][1]> temp[i][1]+m_sum:
                m_sum = temp[i+1][1] -temp[i][1]
    depsum = m_sum

    waiting = []
    first = Mat[0]
    for i in range(0, processesNumber):
        if Mat[i][1] == first[1]:
            if Mat[i][3] < first[3]:
                first = Mat[i]

    current_running.append(first[0])
    for i in range(0, len(Mat)):
        if Mat[i] == first:
            Mat[i][2] = Mat[i][2] - 1
        if Mat[i][2] == 0:
            del Mat[i]
            break
    m_sum = m_sum - 1
    start = 1



    for i in range(0 ,m_sum):
        for j in range(0, len(Mat)):
            if Mat[j][1] <= start:
                waiting.append(Mat[j])
        if len(waiting) == 0:
            if Mat[j][1] != start:
                current_running.append("IDLE")

            else:
                first = Mat[0]
                for j in range(0, len(Mat)):
                    if Mat[j][1] == first[1]:
                        if Mat[j][3] < first[3]:
                            first = Mat[j]
                current_running.append(first[0])
                for q in range(0, len(Mat)):
                    if Mat[q][0] == first[0]:
                        Mat[q][2] = Mat[q][2] - 1
                    if Mat[q][2] == 0:
                        del Mat[q]
                        break
        else:
            first = waiting[0]
            for j in range(0, len(waiting)):
                if waiting[j][3] < first[3]:
                    first = waiting[j]
            waiting.clear()

            for q in range(0, len(Mat)):
                if Mat[q][0] == first[0]:
                    Mat[q][2] = Mat[q][2] - 1
                if Mat[q][2] == 0:
                    del Mat[q]
                    break
            current_running.append(first[0])

        m_sum = m_sum - 1
        start = start + 1

    current_running

def averagetime(processesNumber):
    waittime = []
    bursttime = []
    departure = []
    burst = 0
    firsttime = 0
    firstArrived = current_running[0]
    print(firstArrived)
    for i in range(0, len(temp)):
        if temp[i] == firstArrived:
            firsttime = temp[i][1]
    print(firsttime)
    for i in range(0, len(temp)):
        indexpos = 0
        indexPoslist = []
        prearrival.append(temp[i][1])
        bursttime.append(temp[i][2])
        for j in range(0, temp[i][2]):
            indexpos = current_running.index(temp[i][0], indexpos)
            indexPoslist.append(indexpos)
            indexpos += 1
        if i == 0:
            departure.append(indexPoslist[len(indexPoslist) - 1] + 1)
        else:
            departure.append(indexPoslist[len(indexPoslist) - 1] + 1 + firsttime)
        if prearrival[i] > prearrival[i-1] + bursttime[i-1]:
            waittime.append(0)
        else:
            waittime.append(departure[i] - prearrival[i] - bursttime[i])
    tim = 0
    for i in range(len(waittime)):
        tim = tim + waittime[i]
    averageTime = tim / processesNumber
    if processesNumber == 1:
        averageTime = 0
        return averageTime
    else:
        return averageTime



############################################################### FCFS ####################################
Mat = []
def FCFSprocessCreate(processesNumber):
    number_of_columns = 3  # number of columns of matrix
    for i in range(0, processesNumber):
        Mat.append([])  # Create rows in list , row for each process
    for i in range(0, processesNumber):
        for j in range(0, number_of_columns):
            Mat[i].append(j)
            Mat[i][j] = 0
    print("Done number\n")
def FCFS_input(name, ArrivalTime, BurstTime):
    Mat[name - 1][0] = name
    Mat[name - 1][1] = ArrivalTime
    Mat[name - 1][2] = BurstTime

    print(Mat[name - 1])


FCcurrent_running = []
FCrunning = []
ProcessArrival = []

def FCFSburst(processesNumber):
    ProcessArrival = sorted(Mat, key=arrivaltime)
    bursteach = []
    for i in range(len(ProcessArrival)):
        bursteach.append(ProcessArrival[i][2])
    return bursteach

def FCFS(processesNumber):
    ProcessArrival = sorted(Mat, key=arrivaltime)
    for i in range(len(ProcessArrival)):
        if ProcessArrival[i][1] > ProcessArrival[i-1][1]+ProcessArrival[i-1][2]:
            FCcurrent_running.append("IDLE")
        else:
            FCcurrent_running.append("P" + str(ProcessArrival[i][0]))
    return FCcurrent_running



def FCaverage(processesNumber):
    ProcessArrival = sorted(Mat, key=arrivaltime)
    arrival = []
    bursttime = []
    departure = []
    waittime = []
    dsum = 0

    for i in range(len(ProcessArrival)):
        arrival.append(ProcessArrival[i][1])
        bursttime.append(ProcessArrival[i][2])
        departure.append(ProcessArrival[i][2] + dsum)
        dsum = departure[i]
    tim = 0
    for i in range(processesNumber):
        tim = tim + (departure[i]-bursttime[i]-arrival[i])
    averageTime = tim / processesNumber
    if processesNumber == 1:
        averageTime = 0
        return averageTime
    else:
        return averageTime




def FCreturnLeave(processesNumber):
    ProcessArrival = sorted(Mat, key=arrivaltime)
    arrival = []
    bursttime = []
    departure = []
    dsum = 0
    for i in range(len(ProcessArrival)):
        arrival.append(ProcessArrival[i][1])
        bursttime.append(ProcessArrival[i][2])
        departure.append(ProcessArrival[i][2] + dsum)
        dsum = departure[i]

    return departure

############################################# preemptive SJF #######################################

global PreSJFtemp
PreSJFtemp = []
global SJprecurrent_running
SJprecurrent_running = []
Mat = []
global SJFprearrival
SJFprearrival = []
def processCreate(processesNumber):
    number_of_columns = 3  # number of columns of matrix
    for i in range(0, processesNumber):
        PreSJFtemp.append([])  # Create rows in list , row for each process
    for i in range(0, processesNumber):
        for j in range(0, number_of_columns):
            PreSJFtemp[i].append(j)
            PreSJFtemp[i][j] = 0
    for i in range(0, processesNumber):
        Mat.append([])  # Create rows in list , row for each process
    for i in range(0, processesNumber):
        for j in range(0, number_of_columns):
            Mat[i].append(j)
            Mat[i][j] = 0
    print("Done Number\n")

def pre_sjf_input(name, ArrivalTime, BurstTime):
    Mat[name - 1][0] = PreSJFtemp[name - 1][0] = name
    Mat[name - 1][1] = PreSJFtemp[name - 1][1] = ArrivalTime
    Mat[name - 1][2] = PreSJFtemp[name - 1][2] = BurstTime

    print(Mat[name - 1])




def preemptive_sjf(processesNumber):
    Mat.sort(key=operator.itemgetter(1, 2))
    m_sum = 0
    for i in range(0, processesNumber):
        m_sum = m_sum + Mat[i][2]
        if i==processesNumber-1:
            if PreSJFtemp[i][1] > PreSJFtemp[i-1][1]+m_sum:
                m_sum = PreSJFtemp[i+1][1] -PreSJFtemp[i][1]
        else:
            if PreSJFtemp[i+1][1] > PreSJFtemp[i][1]+m_sum:
                m_sum = PreSJFtemp[i+1][1] - PreSJFtemp[i][1]
    waiting = []
    first = Mat[0]
    for i in range(0, processesNumber):
        if Mat[i][1] == first[1]:
            if Mat[i][2] < first[2]:
                first = Mat[i]

    SJprecurrent_running.append(first[0])
    for i in range(0, len(Mat)):
        if Mat[i] == first:
            Mat[i][2] = Mat[i][2] - 1
        if Mat[i][2] == 0:
            del Mat[i]
            break
    m_sum = m_sum - 1
    start = 1

    for i in range(0, m_sum):
        for j in range(0, len(Mat)):
            if Mat[j][1] <= start:
                waiting.append(Mat[j])
        if len(waiting) == 0:
            if Mat[j][1] != start:
                SJprecurrent_running.append("IDLE")
            else:
                first = Mat[0]
                for j in range(0, len(Mat)):
                    if Mat[j][1] == first[1]:
                        if Mat[j][2] < first[2]:
                            first = Mat[j]
                SJprecurrent_running.append(first[0])
                for q in range(0, len(Mat)):
                    if Mat[q][0] == first[0]:
                        Mat[q][2] = Mat[q][2] - 1
                    if Mat[q][2] == 0:
                        del Mat[q]
                        break
        else:
            first = waiting[0]
            for j in range(0, len(waiting)):
                if waiting[j][2] < first[2]:
                    first = waiting[j]
            waiting.clear()

            for q in range(0, len(Mat)):
                if Mat[q][0] == first[0]:
                    Mat[q][2] = Mat[q][2] - 1
                if Mat[q][2] == 0:
                   del Mat[q]
                   break
            SJprecurrent_running.append(first[0])
        m_sum = m_sum - 1
        start = start + 1




def SJaveragetime(processesNumber):
    waittime = []
    bursttime = []
    departure = []
    burst = 0
    firsttime = 0
    firstArrived = SJprecurrent_running[0]
    print(firstArrived)
    for i in range(0, len(PreSJFtemp)):
        if PreSJFtemp[i] == firstArrived:
            firsttime = PreSJFtemp[i][1]
    print(firsttime)
    for i in range(0, len(PreSJFtemp)):
        indexpos = 0
        indexPoslist = []
        SJFprearrival.append(PreSJFtemp[i][1])
        bursttime.append(PreSJFtemp[i][2])
        for j in range(0, PreSJFtemp[i][2]):
            indexpos = SJprecurrent_running.index(PreSJFtemp[i][0], indexpos)
            indexPoslist.append(indexpos)
            indexpos += 1
        if i == 0:
            departure.append(indexPoslist[len(indexPoslist) - 1] + 1)
        else:
            departure.append(indexPoslist[len(indexPoslist) - 1] + 1 + firsttime)
        if SJFprearrival[i] > SJFprearrival[i - 1] + bursttime[i - 1]:
            waittime.append(0)
        else:
            waittime.append(departure[i] - SJFprearrival[i] - bursttime[i])
    tim = 0
    for i in range(len(waittime)):
        tim = tim + waittime[i]
    averageTime = tim / processesNumber
    if processesNumber == 1:
        averageTime = 0
        return averageTime
    else:
        return averageTime

#################################### non-preemptive priority ##########################################
Mat = []
waitingList = []
startingList = []
global currentRunning
currentRunning = []
global GanttInformation
GanttInformation = []
xcurrent_running = []
def NonPrioprocessCreate(processesNumber):
    number_of_columns = 4  # number of columns of matrix
    for i in range(0, processesNumber):
        Mat.append([])  # Create rows in list , row for each process
    for i in range(0, processesNumber):
        for j in range(0, number_of_columns):
            Mat[i].append(j)
            Mat[i][j] = 0

    for i in range(0, processesNumber):
        waitingList.append([])  # Create rows in list , row for each process
    for i in range(0, processesNumber):
        for j in range(0, number_of_columns):
            waitingList[i].append(j)
            waitingList[i][j] = 0
    for i in range(0, processesNumber):
        startingList.append([])  # Create rows in list , row for each process
    for i in range(0, processesNumber):
        for j in range(0, number_of_columns):
            startingList[i].append(j)
            startingList[i][j] = 0

    for i in range(0, processesNumber):
        GanttInformation.append([])  # Create rows in list , row for each process
    for i in range(0, processesNumber):
        for j in range(0, number_of_columns):
            GanttInformation[i].append(j)
            GanttInformation[i][j] = 0
    print("Done number\n")

waitingList.clear()
startingList.clear()

def NonPrioinput(name, ArrivalTime, BurstTime, Priority):
    Mat[name - 1][0] = name
    Mat[name - 1][1] = ArrivalTime
    Mat[name - 1][2] = BurstTime
    Mat[name - 1][3] = Priority

    print(Mat[name - 1])

current_running = []

def nonpreemptive_priority(processesNumber):
    Mat.sort(key=operator.itemgetter(1, 3))
    arrival = 0  # initialize minimum arrival time
    priority = Mat[0][3]  # initialzie priority to that of first process in order
    currentProcess = Mat[0]  # initailize process to the first process

    startingList = []
    postedlist = []
    count = 0
    index = 0
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

                    index = i

            if len(waitingList) == 0:
                Burst = Mat[index][1]
                for i in range(0, len(Mat)):
                    if Mat[i][1] <= Burst:
                        waitingList.append(Mat[i])
                first = waitingList[0]
                for i in range(0, len(waitingList)):

                    if waitingList[i][3] < first[3]:
                        first = waitingList[i]
                    elif waitingList[i][3] == first[3]:
                        if waitingList[i][1] < first[1]:
                            first = waitingList[i]

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
                    elif waitingList[i][3] == first[3]:
                        if waitingList[i][1] < first[1]:
                            first = waitingList[i]
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
                    count = count + 1
                    index = i
            if count == 0:
                Burst = Mat[index][1]
                for i in range(0, len(Mat)):
                    if Mat[i][1] <= Burst:
                        waitingList.append(Mat[i])
                first = waitingList[0]
                for i in range(0, len(waitingList)):

                    if waitingList[i][3] < first[3]:
                        first = waitingList[i]
                    elif waitingList[i][3] == first[3]:
                        if waitingList[i][1] < first[1]:
                            first = waitingList[i]
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
                    elif waitingList[i][3] == first[3]:
                        if waitingList[i][1] < first[1]:
                            first = waitingList[i]

                if len(waitingList) == 1:
                    first = waitingList[0]

                currentProcess = first
                currentRunning.append(currentProcess)
                for i in range(0, len(Mat)):
                    if Mat[i] == first:
                        del Mat[i]
                        break
                Burst = Burst + first[2]
    for i in range(0, processesNumber):
        for j in range(0, 4):
            GanttInformation[i][0] = currentRunning[i][0]
            GanttInformation[i][1] = currentRunning[i][2]
            if i == 0:

                GanttInformation[i][2] = currentRunning[i][1]
                GanttInformation[i][3] = currentRunning[i][1] + currentRunning[i][2]
            else:
                if currentRunning[i][1] <= GanttInformation[i - 1][3]:
                    GanttInformation[i][2] = GanttInformation[i - 1][3]
                    GanttInformation[i][3] = GanttInformation[i][2] + GanttInformation[i][1]
                else:
                    GanttInformation[i][2] = currentRunning[i][1]
                    GanttInformation[i][3] = currentRunning[i][1] + currentRunning[i][2]
    PrenonCurrent = []
    for i in range(len(currentRunning)):
        PrenonCurrent.append("P" + str(currentRunning[i][0]))

    return PrenonCurrent


def Prenonaverage(processesNumber):
    sum = 0
    for i in range(0, processesNumber):
        sum = sum + (GanttInformation[i][3] - currentRunning[i][1] - GanttInformation[i][1])
    averageWaitingTime = sum / processesNumber
    return averageWaitingTime


def Prenondepart(processesNumber):
    departure = []
    for i in range(processesNumber):
        departure.append(GanttInformation[i][3])
    return departure

def PrenonBurst(processesNumber):
    bursttime = []
    for i in range(processesNumber):
        bursttime.append(GanttInformation[i][1])
    return bursttime
######################################### ROUND ROBIN ############################################

global GChart
GChart = []
global RRAvgWaitingTime
RRAvgWaitingTime = 0
global RRAvgTurnAroundTime
RRAvgTurnAroundTime = 0
global RRdepart
RRdepart = []
PList = []

def RR_create(processesNumber):
    for i in range(0, processesNumber):
        PList.append([])  # Create rows in list , row for each process
    for i in range(0, processesNumber):
        for j in range(0, 3):
            PList[i].append(j)
            PList[i][j] = 0


    print("Done Number\n")


def RR_input(name, ArrivalTime, BurstTime):
    PList[name - 1][0] = name
    PList[name - 1][1] = ArrivalTime
    PList[name - 1][2] = BurstTime
    print(PList)


def shiftCL(alist):  # circular shift left fn: to rearrange queue
    temp = alist[0]
    for i in range(len(alist)-1):
        alist[i] = alist[i+1]
    alist[len(alist)-1] = temp
    return alist


def RR(TQ, n):  # time quantum, processes list, number of processes

    q = TQ  # time quantum
    TotalBT = 0
    time = 0  # current time
    AP = 0  # arrived processes
    RP = 0  # ready processes
    DP = 0  # done processes
    TotalCT = 0
    start = 0
    TotalAT = 0
    # lists of AT and BT
      # waiting queue
    CTList = []  # complition time

    ATList = []  # arrival time

    BTList = []  # burst time
    queue = []
    a = 0

    while a < n:
        ATList.append(PList[a][1])
        BTList.append(PList[a][2])
        a += 1

    while(DP < n):
        for i in range (AP, n):
            if (time>= PList[i][1]):
                queue.append(PList[i])
                AP+=1
                RP+=1

# if no process come or alla processes finished
        if (RP < 1):
            GChart.append(0)
            time += 1
            continue
        # shift
        if (start):  # if first quantum time is done
            queue = shiftCL(queue)

        if (queue[0][2] > 0):
            if (queue[0][2] > q):
                for g in range(time, time+q):
                    GChart.append(queue[0][0])
                time += q
                queue[0][2] -= q

            else:  # if process burst <= quantum
                for g in range(time, time+queue[0][2]):
                    GChart.append(queue[0][0])
                time += queue[0][2]
                CTList.append(time)  # add to complition time list
                queue[0][2] = 0
                DP += 1
                RP -= 1
            start = 1

    o = 0
    while o<n:
        TotalCT += CTList[o]
        TotalAT += ATList[o]
        TotalBT += BTList[o]

        o += 1

    for i in range(len(GChart)):
        if GChart[i] == 0:
            GChart[i] = "IDLE"
        else:
            GChart[i] = "P" + str(GChart[i])

        # edit
    sum = 0
    i = 1
    while (i <= (len(GChart))):
        sum = i
        RRdepart.append(sum)
        i += 1
    # edit

    RRAvgWaitingTime = (TotalCT - TotalAT - TotalBT) / n
    RRAvgTurnAroundTime = (TotalCT - TotalAT) / n
    print(RRdepart)
    return RRAvgWaitingTime

    # print(BTList)
    # print(CTList)


def main():
    while 1 :
        Algorithm = input("Enter the type of Algoritm\n")  # Enter type of algorithm
        if Algorithm == "Preemptive priority schedule":
            preemptive_priority()
        elif Algorithm == "FCFS":
            FCFS()
        elif Algorithm == "Preemptive SJF schedule":
            preemptive_sjf()
        elif Algorithm == "Non-preemptive priority schedule":
            nonpreemptive_priority()
        elif Algorithm == "Non-preemptive SJF schedule":
            no_of_processes = int(input("Enter number of processes: "))
            sjf = SJF()
            sjf.processData(no_of_processes)
        elif Algorithm == "Round robin schedule":
            time_quantum = int(input("Enter the time Quantum\n"))
            processes_number = int(input("Enter number of processes\n"))
            plist = []
            for i in range(0, processes_number):
                pid = int(input("Enter Process ID \n"))
                arrival = int(input("Enter Process arrival time \n"))
                burst = int(input("Enter Process burst \n"))
                # pid,arrival,burst
                plist.append(process(pid, arrival, burst))
            RR(time_quantum, plist, len(plist))
            print(GChart)
            print(RRAvgWaitingTime)
        else:
            print("Enter a valid type\n")

        new = print("Do you want a new process?\n")
        if new == "yes":
            break;
        else:
            continue



if __name__ == '__main__': main()