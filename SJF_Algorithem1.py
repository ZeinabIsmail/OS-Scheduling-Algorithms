import SJFnon

process_data = []
w_time = 0
process_id = []
process_time = []
process_burst = []


class SJF:


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

            for j in range(len(process_data)):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][3] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    normal_queue.append(temp)
                    temp = []

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
                last_s_time = len(start_time) - 1
                process_data[k].append(start_time[last_s_time])
                process_data[k].append(e_time)

            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                last_s_time = len(start_time) - 1
                process_data[k].append(start_time[last_s_time])
                process_data[k].append(e_time)

        t_time = SJF.calculateTurnaroundTime(self, process_data)
        w_time1 = SJF.calculateWaitingTime(self, process_data)
        global w_time
        w_time = w_time1
        global process_id
        global process_time
        global process_burst
        process_data.sort(key=lambda x: x[4])
        for i in range(len(process_data)):

            if i == 0 and process_data[i][4] !=0 :
                process_id.append('idle')
                process_time.append(process_data[i][4])
                process_burst.append(process_data[i][4])
                process_id.append('P'+str(process_data[i][0]))
                process_time.append(process_data[i][5])
                process_burst.append(process_data[i][2])

            elif process_data[i][4] == process_data[i-1][5] or process_data[i][4] == 0 :
                process_id.append('P' + str(process_data[i][0]))
                process_time.append(process_data[i][5])
                process_burst.append(process_data[i][2])

            elif process_data[i][4] > process_data[i-1][5]:
                process_id.append('idle')
                process_time.append(process_data[i][4])
                process_burst.append(process_data[i][4])
                process_id.append('P' + str(process_data[i][0]))
                process_time.append(process_data[i][5])
                process_burst.append(process_data[i][2])




    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
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
            waiting_time = process_data[i][6] - process_data[i][2]
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



#if __name__ == "__main__":
   # no_of_processes = int(input("Enter number of processes: "))
    #sjf = SJF()
    #sjf.processData(no_of_processes)

def noProcess (SJFnon_noOfprocess) :
    processNo = SJFnon_noOfprocess
    print("Number entered")


def ProcessInfo (ID , Arrival ,Burst) :
    temp = [ID, Arrival, Burst, 0]
    process_data.append(temp)
    print("info entered")
    return process_data

