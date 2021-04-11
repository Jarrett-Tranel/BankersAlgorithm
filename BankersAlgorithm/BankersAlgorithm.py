#The number of units of each resource is represented as a one-dimensional array R[m], 
#where m is the number of resources and each entry R[j] records the number of units of resource Rⱼ .
numOfResource = [6, 4, 2, 4, 2] #numOfResource = [numOfResources]

#The maximum claims are represented as a two-dimensional array P[n][m] where each entry P[i][j] contains an integer
#that records the maximum number of units of resource Rⱼ that process pᵢ will ever request.
processes = [[[4, 2, 0], [3, 1, 0]], [[2, 2, 0], [4, 1, 0], [1, 4, 0]]] #maxClaims[processId, ResourceNumber, resourcesAllocated]
#I decided to make this a 3d array instead of a 2D array to be able to better track what's going on given that this is a simulation

allocationEdges = [0, 0, 0, 0, 0]
requestsEdges = [0, 0, 0, 0, 0]

#be able to request(i, j, k) or release(i, j, k), given i = processID, j = resourceNumber, and k = numOfUnitsBeingTransferred

def findProcessRequestMax(pid, rid): #Helper Function
    for i in range (len(processes[pid])):
        if (processes[pid][i][0] == rid):
            return (processes[pid][i][1])
    print("Process ", str(pid), " has no requests for request ", str(rid))
    return(0)

def getHeldResources(pid, rid): #Helper Function
    for i in range (len(processes[pid])):
        if (processes[pid][i][0] == rid):
            return (processes[pid][i][2])
    print("Process ", str(pid), " has no requests for request ", str(rid))
    return(0)

def addHeldResources(pid, rid, num): #Helper Function
    for i in range (len(processes[pid])):
        if (processes[pid][i][0] == rid):
            processes[pid][i][2] += num
            return
    print("Process ", str(pid), " has no requests for request ", str(rid))
    return(0)

def subtractHeldResources(pid, rid, num): #Helper Function
    for i in range (len(processes[pid])):
        if (processes[pid][i][0] == rid):
            processes[pid][i][2] -= num
            return
    print("Process ", str(pid), " has no requests for request ", str(rid))
    return(0)

def request(processID, resourcesNum, numOfUnits):
    for i in range (len(processes[processID])):
        max = findProcessRequestMax(processID, resourcesNum)
        held = getHeldResources(processID, resourcesNum)
        if ((numOfResource[resourcesNum] - allocationEdges[resourcesNum]) - (max-held) >= 1): 
            requestsEdges[resourcesNum] += numOfUnits
        else:
            print("Request denied")
            for j in range (len(requestsEdges)):
                requestsEdges[j] = 0
            return
    print ("Request Granted")   
    for j in range (len(requestsEdges)):
         requestsEdges[j] = 0
    allocationEdges[resourcesNum] += numOfUnits
    addHeldResources(processID, resourcesNum, numOfUnits)


def checkResourceStatus(rid):
    return(numOfResource[rid] - allocationEdges[rid])

def release(processID, resourcesNum, numOfUnits):
    subtractHeldResources(processID, resourcesNum, numOfUnits)
    allocationEdges[resourcesNum] -= numOfUnits
    print("Released ", str(numOfUnits), " units of resource ", str(resourcesNum), " from process ", str(processID))
    return()


def showEverything(resourcesLeft, ProcessStatus):
    for i in range (len(ProcessStatus)):
        for k in range (len(ProcessStatus[i])):
            print ("Process ", str(i), " has ", str(ProcessStatus[i][k][2]), " units of resource ", str(ProcessStatus[i][k][0]), 
               " taken. Process ", str(i), " needs ", str(ProcessStatus[i][k][1] -ProcessStatus[i][k][2]), " more units of resource ", 
               str(ProcessStatus[i][k][0])) 
    for j in range (len(resourcesLeft)):
        print ("Resource ", str(j), " has ", str(checkResourceStatus(j)), "units remaining.\n")

#print (str(processes[0][0][1]))
showEverything(numOfResource, processes)
request(0, 3, 1)
showEverything(numOfResource, processes)
release(0, 3, 1)
showEverything(numOfResource, processes)

while(1):
    showEverything(numOfResource, processes)
    print ("What would you like to do? \n 1.Request a Resource \n 2.Release a Resource")
    choice = input()
    print ("What process ID would you like to target?")
    pid = int(input())
    print ("What resource ID would you like to target?")
    rid = int(input())
    print ("How many units of resources ", rid, " would you like to transfer?")
    num = int(input())
    if (choice == "1"):
        request(pid, rid, num)
    elif (choice == "2"):
        release(pid, rid, num)


