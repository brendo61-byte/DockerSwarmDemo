from threading import Thread

import requests
import random
import time

URL = "http://134.122.17.7/data"
HITS = 100
THREADS = 5


class Recorder:
    def __init__(self, threads, hits):
        self.threads = threads
        self.hits = hits
        self.log = {}
        self.failedPackages = 0
        self.testRunning = True

        for i in range(threads):
            self.log.update({i: None})

    def checkThreads(self):
        testRunning = True

        while testRunning:
            if None not in self.log.values():
                testRunning = False

            else:
                time.sleep(1)

        self.findThreadAverage()

    def findThreadAverage(self):
        sumTotal = sum(self.log.values())

        self.avgTotal = (sumTotal / (self.threads * self.hits)) * (10 ** -3)

        self.testRunning = False


def spammer(recorderObj, threadNum, url, numOfHits):
    # print(f"Thread {threadNum} has started")

    totalElapsedMicroSeconds = 0

    for i in range(numOfHits):
        package = {
            "data": random.randint(0, 101),
            "timeStamp": "Now",
            "units": "c",
            "readingType": "temperature"
        }

        response = requests.post(url=url, json=package, timeout=10000)
        if response.status_code == 200:
            totalElapsedMicroSeconds += response.elapsed.microseconds
        else:
            recorderObj.failedPackages += 1

    recorderObj.log[threadNum] = totalElapsedMicroSeconds


def starter(threads, hits):
    recorder = Recorder(threads=threads, hits=hits)
    time.sleep(0.5)

    for i in range(threads):
        thread = Thread(target=spammer, args=[recorder, i, URL, hits])
        thread.start()

    recorder.checkThreads()

    return recorder


if __name__ == '__main__':
    starter(threads=THREADS, hits=HITS)
