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

def preemptive_priority():
    Type = input("Type of scheduling\n")  # preemetive or not
    processesNumber = int(input("Enter the number of processes\n"))  # number of rows of matrix
    number_of_columns = 4  # number of columns of matrix
    temp = []  # create the list
    for i in range(0, processesNumber):
        temp.append([])  # Create rows in list , row for each process
    for i in range(0, processesNumber):
        for j in range(0, number_of_columns):
            temp[i].append(j)
            temp[i][j] = 0
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
                Mat[i][j] = temp[i][j] = input()
            if j == 1:
                print('Arrival Time For Process', i + 1)
                Mat[i][j] = temp[i][j] = int(input())
            if j == 2:
                print('Burst Time For Process', i + 1)
                Mat[i][j] = temp[i][j] = int(input())
            if j == 3:
                print('Priority Number For Process', i + 1)
                Mat[i][j] = temp[i][j] = int(input())
    Mat.sort(key=operator.itemgetter(1, 3))
    if Type == "Preemptive":
        m_sum = 0
        for i in range(0, processesNumber):
            m_sum = m_sum + Mat[i][2]
        depsum = m_sum
        current_running = []
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

        for i in range(0, m_sum):
            for j in range(0, len(Mat)):
                if Mat[j][1] <= start:
                    waiting.append(Mat[j])
            if len(waiting) == 0:
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

    print(current_running)
    arrival = []
    bursttime = []
    departure = []
    for i in range(len(temp)):
        arrival.append(temp[i][1])
        bursttime.append(temp[i][2])
    current_running.reverse()
    for i in range(len(temp)):
        index = current_running.index(temp[i][0])
        y = depsum - index
        departure.append(y)
    tim = departure[0] - arrival[0] - bursttime[0]
    for i in range(1, processesNumber):
        tim = tim + (departure[i] - arrival[i] - bursttime[i])
    averageTime = tim / processesNumber
    print(averageTime)


############################################################### FCFS ####################################

def FCFS():
    processesNumber = int(input("Enter the number of processes\n"))  # number of rows of matrix
    number_of_columns = 3  # number of columns of matrix
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

    ProcessArrival = sorted(Mat, key=arrivaltime)
    current_running = []
    depsum = 0
    for i in range(len(ProcessArrival)):
        for j in range(0, ProcessArrival[i][2]):
            current_running.append(ProcessArrival[i][0])
        depsum = depsum + ProcessArrival[i][2]
    print(current_running)
    arrival = []
    bursttime = []
    departure = []
    for i in range(len(ProcessArrival)):
        arrival.append(ProcessArrival[i][1])
        bursttime.append(ProcessArrival[i][2])
    current_running.reverse()
    for i in range(len(ProcessArrival)):
        index = current_running.index(ProcessArrival[i][0])
        y = depsum - index
        departure.append(y)
    tim = departure[0] - arrival[0] - bursttime[0]
    for i in range(1, processesNumber):
        tim = tim + (departure[i] - arrival[i] - bursttime[i])
    averageTime = tim / processesNumber
    print(averageTime)



############################################# preemptive SJF #######################################

def preemptive_sjf():
    Type = input("Type of scheduling\n")  # preemetive or not
    processesNumber = int(input("Enter the number of processes\n"))  # number of rows of matrix
    number_of_columns = 3  # number of columns of matrix
    temp = []  # create the list
    for i in range(0, processesNumber):
        temp.append([])  # Create rows in list , row for each process
    for i in range(0, processesNumber):
        for j in range(0, number_of_columns):
            temp[i].append(j)
            temp[i][j] = 0
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

    Mat.sort(key=operator.itemgetter(1, 2))
    if Type == "Preemptive":
        m_sum = 0
        for i in range(0, processesNumber):
            m_sum = m_sum + Mat[i][2]
        current_running = []
        waiting = []
        first = Mat[0]
        for i in range(0, processesNumber):
            if Mat[i][1] == first[1]:
                if Mat[i][2] < first[2]:
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

        for i in range(0, m_sum):
            for j in range(0, len(Mat)):
                if Mat[j][1] <= start:
                    waiting.append(Mat[j])
            if len(waiting) == 0:
                first = Mat[0]
                for j in range(0, len(Mat)):
                    if Mat[j][1] == first[1]:
                        if Mat[j][2] < first[2]:
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
                    if waiting[j][2] < first[2]:
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

    print(current_running)
    arrival = []
    bursttime = []
    departure = []
    for i in range(len(temp)):
        arrival.append(temp[i][1])
        bursttime.append(temp[i][2])
    current_running.reverse()
    for i in range(len(temp)):
        index = current_running.index(temp[i])
        y = depsum - index
        departure.append(y)
    tim = departure[0] - arrival[0] - bursttime[0]
    for i in range(1, processesNumber):
        tim = tim + (departure[i] - arrival[i] - bursttime[i])
    averageTime = tim / processesNumber
    print(averageTime)

#################################### non-preemptive priority ##########################################

def nonpreemptive_priority():
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
    Mat.sort(key=operator.itemgetter(1, 3))
    if Type == "Non Preemptive":
        arrival = 0;  # initialize minimum arrival time
        priority = Mat[0][3]  # initialzie priority to that of first process in order
        currentProcess = Mat[0]  # initailize process to the first process
        currentRunning = []
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

        GanttInformation = []
        for i in range(0, processesNumber):
            GanttInformation.append([])  # Create rows in list , row for each process
        for i in range(0, processesNumber):
            for j in range(0, number_of_columns):
                GanttInformation[i].append(j)
                GanttInformation[i][j] = 0

        for i in range(0, processesNumber):
            for j in range(0, number_of_columns):
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
            sum = 0
            for i in range(0, processesNumber):
                sum = sum + (GanttInformation[i][3] - currentRunning[i][1] - GanttInformation[i][1])
            averageWaitingTime = sum / 3
        current_running = []
        for i in range(len(currentRunning)):
            for j in range(0, Mat[i][2]):
                current_running.append(currentRunning[i][0])
        print(current_running)
        print(averageWaitingTime)

######################################### ROUND ROBIN ############################################
GChart = []  # Gaint Chart
RRAvgWaitingTime = 0
RRAvgTurnAroundTime = 0


class process:
    def __init__(self, PId, AT, BT):
        self.PId = PId  # process id
        self.arrival = AT  # arrival time
        self.burst = BT  # burst time


def shiftCL(alist):  # circular shift left fn: to rearrange queue
    temp = alist[0]
    for i in range(len(alist)-1):
        alist[i] = alist[i+1]
    alist[len(alist)-1] = temp
    return alist


def RR(TQ, PList, n):  # time quantum, processes list, number of processes
    global GChart
    global RRAvgWaitingTime
    global RRAvgTurnAroundTime
    queue = []  # waiting queue
    CTList = []  # complition time
    TotalCT = 0
    ATList = []  # arrival time
    TotalAT = 0
    BTList = []  # burst time
    TotalBT = 0
    time = 0  # current time
    AP = 0  # arrived processes
    RP = 0  # ready processes
    DP = 0  # done processes
    q = TQ  # time quantum
    start = 0

    # lists of AT and BT
    a = 0
    while a < n:
        ATList.append(PList[a].arrival)
        BTList.append(PList[a].burst)

        a += 1

    while(DP < n):
        for i in range (AP, n):
            if (time>= PList[i].arrival):
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

        if (queue[0].burst > 0):
            if (queue[0].burst > q):
                for g in range(time, time+q):
                    GChart.append(queue[0].PId)
                time += q
                queue[0].burst -= q
            else:  # if process burst <= quantum
                for g in range(time, time+queue[0].burst):
                    GChart.append(queue[0].PId)
                time += queue[0].burst
                CTList.append(time)  # add to complition time list
                queue[0].burst = 0
                DP += 1
                RP -= 1
            start = 1

    o = 0
    while o<n:
        TotalCT += CTList[o]
        TotalAT += ATList[o]
        TotalBT += BTList[o]

        o += 1

    RRAvgWaitingTime = (TotalCT - TotalAT - TotalBT) / n
    RRAvgTurnAroundTime = (TotalCT - TotalAT) / n
    # print(ATList)
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
