import math
from datetime import datetime
file = open("./Tests.md", "a")

def expoTest(iterations, number):
    counter = 0
    per = 1
    startTime = datetime.now()
    lastTime = datetime.now()
    cycles = []
    for i in range(iterations):
        val = math.exp(number)
        if counter == int(iterations/100):
            nowTime = datetime.now()
            diff = nowTime - lastTime;
            cycles.append(diff.total_seconds()) 
            print(f"Running: {per}% {diff.total_seconds()} Sec")
            counter = 0
            per+=1
            lastTime = nowTime
        counter+=1
    endTime = datetime.now()
    timeTaken = endTime - startTime
    avgCycleTime = sum(cycles) / len(cycles)
    print(f"\nCompleted: {per}% \nAvrage 1M cycle: {avgCycleTime} Sec \nTotal cycles: {iterations/1000000} \nTotal Time: {timeTaken.total_seconds()} Sec \nExponential: {val}")
    file.write(f"\n# Started on: {datetime.now()} \n* Completed: {per}% \n* Avrage 1M cycle: {avgCycleTime} Sec \n* Total cycles: {iterations/1000000} \n* Total Time: {timeTaken.total_seconds()} Sec \n* Exponential: {val}\n")
    file.close()

it = 10# int(input("Set Cycles (each is 1M): "))
num = 50# int(input("Exponantial of: "))
expoTest(it*1000000, num)
