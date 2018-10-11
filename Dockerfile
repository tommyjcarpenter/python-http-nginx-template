FROM tiangolo/uwsgi-nginx-flask:python3.6

#setup uwsgi+nginx 
# https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
COPY ./app /app

ENV LISTENPORT 80

RUN pip install --upgrade pip
RUN pip install /app/app

#create logging dir
RUN mkdir -p /opt/logs/
