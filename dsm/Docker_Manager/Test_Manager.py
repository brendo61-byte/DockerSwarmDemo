from flask import Flask, request, jsonify
import logging
import requests

PORT = 5002

PATH = "/Users/brendo/repos/CSU/DockerSwarmDemo/DSM/Docker"

app = Flask(__name__)

logging.basicConfig(level="INFO", filename='program.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def startAndSeedDockerCompose():
    URL = "http://0.0.0.0/controller"

    requests.get(url=URL)


@app.route('/command', methods=["POST"])
def dataPush():
    print("cleaning")
    package = request.get_json()
    logging.debug("New data Package")

    command = package.get('data')

    if command == "local-docker":
        startAndSeedDockerCompose()
        return jsonify(userMessage="Command Ran"), 200

    return jsonify(userMessage="Invalid command"), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=PORT)
