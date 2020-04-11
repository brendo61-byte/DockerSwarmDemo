FROM python:3.7
ADD dataApp.py /
ADD models.py /
ADD requirements.txt /
ADD app.ini /
ADD run.py /
ADD m /
WORKDIR /
RUN pip install -r requirements.txt
RUN chmod +x m

ENV db_name=IoT
ENV db_host=db
ENV db_port=3306
ENV db_user=root
ENV db_password=example

CMD ["uwsgi", "app.ini"]
