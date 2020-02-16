FROM pypy:3.6-slim

LABEL maintainer="LionTao <taojiachun31@foxmail.com>"

EXPOSE 8000

WORKDIR /opt/auth

ADD ./auth ./auth

ADD ./requirements.txt ./

RUN apt-get update && apt-get install gcc -y

RUN pip install -r requirements.txt

RUN apt-get purge gcc -y && apt-get autoremove -y && apt-get clean -y

ENTRYPOINT  ["gunicorn", "--workers=4", "--worker-class=gevent","--bind=0.0.0.0:8000","auth:app"]