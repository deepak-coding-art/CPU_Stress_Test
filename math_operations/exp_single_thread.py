import math
from datetime import datetime as tim

# Gratings
print("CPU Stress Test")

# Calculting Exponential function
def calcExpo(iterations, number):
    for _ in range(iterations):
        math.exp(number)

# Wite the results to file
def writeTest(totalTime, averageTime, score, cycles):
    file = open("./Tests.md", "a")
    file.write(f"\n# Started on: {tim.now()}\n* Cycles {cycles}\n* All cycles compeleted in {totalTime}(S)\n* Average time: {averageTime}(S)\n* Score: {score}")
    file.close()

# Exponential test function
def expoTest(cycles):
    cycleSize = 1000000
    expos = list(range(0, 600))
    cycleDivs = cycleSize//len(expos)
    cycleTimes = []
    for cycle in range(cycles):
        cycleStartTime = tim.now()
        for expo in expos:
            calcExpo(cycleDivs, expo)
        cycleEndTime = tim.now()
        cycleTimes.append((cycleEndTime - cycleStartTime).total_seconds())
        print(f"{cycle} cycles compeleted {round(cycleTimes[cycle], 6)}(S)")
    totalTime = sum(cycleTimes)
    averageTime = sum(cycleTimes)/len(cycleTimes)
    score = (1 / averageTime)*100
    print(f"\nAll cycles compeleted in {totalTime}(S) \nAverag time: {averageTime}(S) \nScore: {score}")
    writeTest(totalTime, averageTime, score, cycles)

# Main loop
while(True):
    cycles = int(input("\nCycles(1M each): "))
    print("Cycle started.\n")
    expoTest(cycles)
    again = input("\nPress N for exit, Press Enter for run gain: ")
    if(again == 'N' or again == "n"):
        break