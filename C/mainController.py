import requests
import time
import os
from receiverApp import app, clientIPs, RESULTS
from threading import Thread

dockerIP = "10.116.0.10"
PORT = 5000


def clean():
    url = "http://" + dockerIP + ":5002/command"
    data = {"data": "local-docker"}

    return requests.post(url=url, json=data)


def clients():
    for client in clientIPs:
        url = "http://" + client + ":5001/start"

        data = {
            "threads": 50,
            "hits": 100
        }

        requests.post(url=url, json=data)


def dockerCompose():
    print("Starting the network...")

    print("Cleaning testing environment")

    x = clean()

    if x.status_code == 200:
        print("... environment ready")

    else:
        print("WARNING: environment could not be cleaned!")
        exit()

    print("Spawning clients")
    print("... using default client settings")
    print("... {} clients generated".format(len(clientIPs * 50)))
    print("Waiting for test to complete")

    results = clients()


def starter():
    time.sleep(1)
    os.system("clear")
    val = input("\nEnter a test number to run.\nOptions are:\n1)docker-compose\n")

    if val is not "1":
        print("Bad test option. Program now exiting")

    if val == "1":
        print("Running docker-compose test...")
        dockerCompose()


if __name__ == '__main__':
    thread1 = Thread(target=starter)
    thread1.start()

    app.run(host="0.0.0.0", debug=False, port=PORT)
