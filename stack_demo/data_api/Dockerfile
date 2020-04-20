FROM python:3.7
ADD data_api.py /
ADD models.py /
ADD requirements.txt /
ADD app.ini /
ADD run.py /
WORKDIR /
RUN pip install -r requirements.txt
CMD ["uwsgi", "app.ini"]