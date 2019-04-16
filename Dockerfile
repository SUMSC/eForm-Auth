FROM pypy:3.6-slim

EXPOSE 8000

WORKDIR /opt/auth

ADD ./auth ./auth

ADD ./requirements.txt ./

ADD ./docker-entrypoint.sh ./

RUN chmod a+x docker-entrypoint.sh

RUN apt-get update && apt-get install gcc -y

RUN pip install -r requirements.txt

ENTRYPOINT  ["gunicorn", "--workers=4", "--worker-class=gevent","--bind=0.0.0.0:8000","auth:app"]

