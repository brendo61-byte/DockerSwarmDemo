FROM python:3.7
ADD dataApp.py /
ADD models.py /
ADD requirements.txt /
ADD app.ini /
ADD run.py /
ADD m /
WORKDIR /


ENV db_name=IoT
ENV db_host=db-mysql-nyc1-84974-do-user-7305389-0.a.db.ondigitalocean.com
ENV db_port=25060
ENV db_user=doadmin
ENV db_password=op3kubspwhry461c

RUN pip install -r requirements.txt
RUN chmod +x m

CMD ["uwsgi", "app.ini"]
