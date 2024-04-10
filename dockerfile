FROM python:3.10
MAINTAINER Kozlov Aleksey 'alekov.msk@yandex.ru'

RUN adduser --disabled-password ssdqadmin

WORKDIR /app
COPY requirements.txt /app/requirements.txt
# COPY pip_packages /app/pip_packages

RUN python3 -m venv venv
# RUN venv/bin/pip install --no-index --find-links /app/pip_packages -r /app/requirements.txt
RUN venv/bin/pip install -r /app/requirements.txt

COPY dqflask /app/dqflask
# COPY config /app/dqflask

COPY ssdq-start.sh /app/ssdq-start.sh
RUN chmod +x /app/ssdq-start.sh

RUN chown -R ssdqadmin:ssdqadmin ./
USER ssdqadmin

EXPOSE 5000
ENTRYPOINT ["bash", "/app/ssdq-start.sh"]
