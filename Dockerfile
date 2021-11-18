FROM python:3.9.9-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
    && apt-get upgrade -y
    #  \
    # && apt-get install -y \
    # bash \
    # curl \
    # gettext \
    # gifsicle \
    # imagemagick \
    # libffi \
    # libjpeg \
    # libpng \
    # libxml2 \
    # libxslt \
    # make \
    # pngquant \
    # yaml \
    # zlib \
    # && python3 -m ensurepip --upgrade \
    # && rm -r /usr/lib/python*/ensurepip

# ARG BASEDIR
# ARG INPUTDIR
# ARG OUTPUTDIR
# ARG CONFFILE
# ARG PUBLISHCONF

# ENV BASEDIR ${BASEDIR}
# ENV INPUTDIR ${INPUTDIR}
# ENV OUTPUTDIR ${OUTPUTDIR}
# ENV CONFFILE ${CONFFILE}
# ENV PUBLISHCONF ${PUBLISHCONF}

RUN mkdir /workspace
WORKDIR /workspace
COPY . /workspace
# EXPOSE 8000

RUN chmod +x /docker-entrypoint.sh
RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/workspace/docker-entrypoint.sh"]
# CMD ["make", "$1"]

# Some reference: https://github.com/apihackers/docker-pelican/blob/master/Dockerfile