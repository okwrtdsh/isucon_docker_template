FROM python:latest
RUN mkdir /app
WORKDIR /app

RUN apt-get update -qq \
 && apt-get upgrade -y \
 && apt-get install --no-install-recommends -y \
    graphviz
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
 && pip install --no-cache-dir \
    flask \
    uwsgi \
    snakeviz \
    gprof2dot

COPY src/ /app

CMD uwsgi -M --ini /app/uwsgi.ini
