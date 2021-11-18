FROM python:3.9.5-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y \
    bash \
    curl \
    gettext \
    gifsicle \
    imagemagick \
    libffi \
    libjpeg \
    libpng \
    libxml2 \
    libxslt \
    make \
    pngquant \
    python3 \
    yaml \
    zlib \
    && python3 -m ensurepip --upgrade \
    && rm -r /usr/lib/python*/ensurepip

ARG BASEDIR
ARG INPUTDIR=$(BASEDIR)/content
ARG OUTPUTDIR=$(BASEDIR)/output
ARG CONFFILE=$(BASEDIR)/pelicanconf.py
ARG PUBLISHCONF=$(BASEDIR)/publishconf.py

ENV BASEDIR ${BASEDIR}
ENV INPUTDIR ${INPUTDIR}
ENV OUTPUTDIR ${BASEDIR}
ENV CONFFILE ${BASEDIR}
ENV PUBLISHCONF ${BASEDIR}

RUN mkdir /workspace
WORKDIR /workspace
COPY ./drafts /workspace
COPY ./theme /workspace
EXPOSE 8000

# RUN chmod +x /docker-entrypoint.sh
RUN pip install -U pip
RUN pip install -r requirements.txt

# ENTRYPOINT ["/api/docker-entrypoint.sh"]
CMD ["make", "$1"]

# Some reference: https://github.com/apihackers/docker-pelican/blob/master/Dockerfile