from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# clientIPs = ["10.116.0.12", "10.116.0.5", "10.116.0.8", "10.116.0.9", "10.116.0.7"]
clientIPs = ["10.116.0.12", "10.116.0.5", "10.116.0.8"]

RESULTS = []

start = time.time()


def display():
    end = time.time()
    timeTotal = 0
    fails = 0

    for entry in RESULTS:
        timeTotal += entry["avgTime"]
        fails += entry["fails"]

    avgTime = timeTotal / len(RESULTS)

    answers = {"time": avgTime, "drops": fails}

    timeDelta = end-start

    totalPackets = len(clientIPs) * 50 * 100

    print("\n\nTest Complete!\nAverage response time from server: {:.4f} mS".format(answers["time"]))
    print("Total requests processed: {}".format(totalPackets))
    print("{}% of requests were dropped".format((answers["drops"] / totalPackets) * 100))
    print("Total time for test: {:.4f} seconds".format(timeDelta))
    print("Request Throughput: {:.4f} requests/second\n\n".format(totalPackets / timeDelta))


@app.route('/results', methods=["POST"])
def dataPush():
    package = request.get_json()

    avgTime = package.get("avgTime")
    fails = package.get("fails")

    if avgTime is None or fails is None:
        return jsonify(userMessage="Invalid"), 400

    RESULTS.append(package)

    if len(RESULTS) == len(clientIPs):
        display()

    return jsonify(userMessage="Command Ran"), 200
