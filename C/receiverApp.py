from flask import Flask, request, jsonify
import time

app = Flask(__name__)

clientIPs = ["0.0.0.0"]

RESULTS = []


def display():
    timeTotal = 0
    fails = 0

    for entry in RESULTS:
        timeTotal += entry["avgTime"]
        fails += entry["fails"]

    avgTime = timeTotal / len(RESULTS)

    answers = {"time": avgTime, "drops": fails}

    print("\n\nTest Complete!\nAverage response time from server: {:.4f} mS".format(answers["time"]))
    print("{}% of requests were dropped\n\n".format((answers["drops"] / len(clientIPs) * 50 * 100) * 100))


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
