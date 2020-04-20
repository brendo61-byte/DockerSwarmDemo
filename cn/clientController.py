from flask import Flask, request, jsonify
from dummyClient import starter
import logging
import time
import requests

from threading import Thread

MASTER_CONTROLLER_IP = "10.116.0.4"

PORT = 5001

RETURN_URL = ""

app = Flask(__name__)

logging.basicConfig(level="INFO", filename='program.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def runClient(threads, hits):
    recorderObj = starter(threads=threads, hits=hits)

    testStatus = recorderObj.testRunning


    data = {
        "avgTime": recorderObj.avgTotal,
        "fails": recorderObj.failedPackages
    }

    print(data)

    url = "http://" + MASTER_CONTROLLER_IP + ":5000/results"
    requests.post(url=url, json=data)


@app.route('/start', methods=["POST"])
def dataPush():
    print("starting clients")
    package = request.get_json()
    logging.debug("New data Package")

    threads = package.get("threads")
    hits = package.get("hits")

    if hits is None or threads is None:
        return jsonify(userMessage="Invalid command"), 400

    thread = Thread(target=runClient, args=[threads, hits])
    thread.start()

    return jsonify(userMessage="Command Ran"), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=PORT)
