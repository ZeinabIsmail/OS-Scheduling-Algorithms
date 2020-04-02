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
    while Algorithm == "FCFS":

        processesNumber = int(input("Enter the number of processes\n"))  # number of rows of matrix
        number_of_columns =3 # number of columns of matrix
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


        ProcessArrival=sorted(Mat,key=arrivaltime)
        GanttInformation = []
        for i in range(0, processesNumber):
            GanttInformation.append([])  # Create rows in list , row for each process
        for i in range(0, processesNumber):
            for j in range(0,4):
                GanttInformation[i].append(j)
                GanttInformation[i][j] = 0

        for i in range(0, processesNumber):
            for j in range(0,4):
                GanttInformation[i][0] = ProcessArrival[i][0]
                GanttInformation[i][1] = ProcessArrival[i][2]
                if i == 0:

                    GanttInformation[i][2] = ProcessArrival[i][1]
                    GanttInformation[i][3] = ProcessArrival[i][1] + ProcessArrival[i][2]
                else:
                    if ProcessArrival[i][1] <= GanttInformation[i - 1][3]:
                        GanttInformation[i][2] = GanttInformation[i - 1][3]
                        GanttInformation[i][3] = GanttInformation[i][2] + GanttInformation[i][1]
                    else:
                        GanttInformation[i][2] = ProcessArrival[i][1]
                        GanttInformation[i][3] = ProcessArrival[i][1] + ProcessArrival[i][2]
            sum = 0
            for i in range(0, processesNumber):
                sum = sum + (GanttInformation[i][3] - ProcessArrival[i][1] - GanttInformation[i][1])
            averageWaitingTime = sum / 3
        print(ProcessArrival)
        print(GanttInformation)
        print(averageWaitingTime)

        cont = input("Do you want a new process?\n")
        if cont == "yes":
            Algorithm = input("Enter the type of Algoritm\n")  # Enter type of algorithm
            continue
        elif cont == "no":
            break


if __name__ == '__main__': main()