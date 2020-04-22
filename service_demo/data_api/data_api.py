from flask import Flask, request, jsonify
from models import DataEntry

import logging
import traceback

app = Flask(__name__)

logging.basicConfig(level="INFO", filename='program.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/data', methods=["POST"])
def dataPush():
    package = request.get_json()
    logging.debug("New data Package")

    if package.get('data') is None or package.get('timeStamp') is None or package.get('units') is None or package.get("readingType") is None:
        logging.warning("Data package is not formatted correctly.\nInput:\n{}".format(package))
        return jsonify(userMessage="Invalid package"), 400

    else:
        try:
            DataEntry.create(**package)
            return jsonify(userMessage="Package Received"), 200
        except Exception as e:
            logging.exception("Error has occurred trying to save data in the data-base.\nException: {}\nTraceBack: {}".format(e, traceback.format_exc()))
            return jsonify(userMessage="Package Failed To Reac h Data-Base"), 400