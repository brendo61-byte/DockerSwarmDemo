from flask import Flask, request, jsonify
from models import DataEntry, db

import logging
import traceback

app = Flask(__name__)

logging.basicConfig(level="INFO", filename='program.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def makeTables():
    models = [DataEntry]
    db.create_tables(models, safe=True)


def cleanTables():
    DataEntry.delete()


@app.route('/controller', methods=["GET"])
def dataPush():
    logging.info("Cleaning DataBase")

    try:
        makeTables()
        cleanTables()
        return jsonify(userMessage="DB Seeded"), 200
    except Exception as e:
        logging.exception("Failed to clean data-base tables.\nException: {}\nTraceBack:\n{}".format(e, traceback.format_exc()))
        return jsonify(userMessage="Package Failed To Seed data-base"), 400
