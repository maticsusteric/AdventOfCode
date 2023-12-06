from helpers import getDailyInputByFolderName
import re
inputData = getDailyInputByFolderName()

def calculatePossibleWinsMultiply(part: int):
    timesArray = re.sub(r'Time:\s*', '', inputData[0]) #inputData[0].replace("Time:", "")
    distanceArray = re.sub(r'Distance:\s*', '', inputData[1])#inputData[1].replace("Distance:", "")

    if part == 1:
        timesArray = re.sub(r'\s+', ' ', timesArray)
        distanceArray = re.sub(r'\s+', ' ', distanceArray)

        timesArray = timesArray.split(" ")
        distanceArray = distanceArray.split(" ")
    elif part == 2:
        timesArray = re.sub(r'\s+', '', timesArray)
        distanceArray = re.sub(r'\s+', '', distanceArray)

        timesArray = timesArray.split(" ")
        distanceArray = distanceArray.split(" ")

    if part == 1:
        arrayOfPossibleWins = []
        for attempt in range(len(distanceArray)):
            recordsNum = 0
            for timeHeld in range(int(timesArray[attempt]) + 1):
                # speed = velocity*time -> physics time
                remainingTime = int(timesArray[attempt]) - int(timeHeld)
                distanceMade = timeHeld * remainingTime
                print(timeHeld)
                if distanceMade > int(distanceArray[attempt]):
                    recordsNum += 1
            arrayOfPossibleWins.append(recordsNum)
    if part == 2:
        ans = 0
        for time in range(int(timesArray[0])):
            # speed = velocity*time -> physics time
            length = time * (int(timesArray[0]) - time)
            if length > int(distanceArray[0]):
                ans += 1
        return ans
    if part == 1:
        ans = arrayOfPossibleWins[0] * arrayOfPossibleWins[1] * arrayOfPossibleWins[2] * arrayOfPossibleWins[3]
    elif part == 2:
        ans = arrayOfPossibleWins[0]

    return ans

print("Part 1: " + str(calculatePossibleWinsMultiply(1)))
print("Part 2: " + str(calculatePossibleWinsMultiply(2)))