import peewee
import os

db_name = os.environ.get("db_name", "IoT")
db_host = os.environ.get("db_host", "134.122.17.7")
db_port = int(os.environ.get("db_port", "3306"))
db_user = os.environ.get("db_user", "root")
db_password = os.environ.get("db_password", "example")

db = peewee.MySQLDatabase(db_name, host=db_host, port=db_port, user=db_user, passwd=db_password)


class BaseModel(peewee.Model):
    class Meta:
        database = db


class DataEntry(BaseModel):
    value = peewee.FloatField()
    timeStamp = peewee.FloatField()
    units = peewee.CharField(max_length=10)
    readingType = peewee.CharField(max_length=25)
