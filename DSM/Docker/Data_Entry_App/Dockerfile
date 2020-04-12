FROM python:3.7
ADD dataApp.py /
ADD models.py /
ADD requirements.txt /
ADD app.ini /
ADD run.py /
ADD m /
WORKDIR /


ENV db_name=IoT
ENV db_host=134.122.17.7
ENV db_port=3306
ENV db_user=root
ENV db_password=example

RUN pip install -r requirements.txt
RUN chmod +x m

CMD ["uwsgi", "app.ini"]
