Title: Set locale for Docker image
Date: 2021-07-14 10:45
Modified: 2021-07-14 10:45
Category: Tech
Tags: #docker, #locale
Slug: set-locale-for-docker-image
Author: filipgorczynski
Status: draft
Summary: 

```Dockerfile
FROM centos:7

RUN yum update -y \
    && yum upgrade -y \
    && yum install python3 pip3 -y;

# does this create venv?
RUN pip3 install flask flask-mysql

RUN mkdir -p /opt/src

WORKDIR /opt/src

COPY . /opt/src

# command that will be run when image will be run as container
ENTRYPOINT FLASKAPP=/opt/src/app.py flask run
```

```bash
:lambda: docker run fgorczynski/flask-app-demo:latest
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 11, in <module>
    sys.exit(main())
  File "/usr/local/lib64/python3.6/site-packages/flask/cli.py", line 990, in main
    cli.main(args=sys.argv[1:])
  File "/usr/local/lib64/python3.6/site-packages/flask/cli.py", line 596, in main
    return super().main(*args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/click/core.py", line 1043, in main
    _verify_python_env()
  File "/usr/local/lib/python3.6/site-packages/click/_unicodefun.py", line 100, in _verify_python_env
    raise RuntimeError("\n\n".join(extra))
RuntimeError: Click will abort further execution because Python was configured to use ASCII as encoding for the environment. Consult https://click.palletsprojects.com/unicode-support/ for mitigation steps.

This system lists some UTF-8 supporting locales that you can pick from. The following suitable locales were discovered: en_US.utf8
```

```Dockerfile
FROM centos:7

RUN yum update -y \
    && yum upgrade -y \
    && yum install python3 pip3 -y;

ENV LC_ALL=en_US.utf-8
ENV LANG=en_US.utf-8

# does this create venv?
RUN pip3 install flask flask-mysql

RUN mkdir -p /opt/src

WORKDIR /opt/src

COPY . /opt/src

# command that will be run when image will be run as container
ENTRYPOINT FLASKAPP=/opt/src/app.py flask run
```
