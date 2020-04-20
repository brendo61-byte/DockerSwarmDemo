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
CMD ["uwsgi", "app.ini"]