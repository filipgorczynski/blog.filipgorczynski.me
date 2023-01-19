Title: Provide more commands to Docker image
Date: 2023-01-14 10:01:38
Modified: 2023-01-14 10:01:38
Category: Notes
Tags: #notes, #docker, #docker-compose, #commands
Slug: provide-more-commands-to-docker-image
Author: filipgorczynski
Status: draft
Cover: https://blog.filipgorczynski.me/images/feature/ian-taylor-jOqJbvo1P9g.jpg
meta_url: https://blog.filipgorczynski.me/2023/01/provide-more-commands-to-docker-image
Summary: 

![Photo by Ian Taylor](https://blog.filipgorczynski.me/images/feature/ian-taylor-jOqJbvo1P9g.jpg)

```Dockerfile
FROM python:3.11.1-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y

RUN mkdir /app
WORKDIR /app
COPY . /app/
EXPOSE 8000

RUN chmod +x /app/docker-entrypoint.sh
RUN pip install -U pip
RUN pip install -r requirements-dev.txt

ENTRYPOINT ["/api/docker-entrypoint.sh"]

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app", "--reload"]

```

```bash
#!/usr/bin/env bash

set -e

-DEFAULT_CMD=shell

function log_info() {
  echo "[INFO]: $*"
}

function log_warn() {
  echo "[WARNING]: $*"
}

DEFAULT_CMD=shell

if [[ $1 == "" ]]; then
  CMD=$DEFAULT_CMD
else
  CMD=$1
  shift
fi

function log_warn() {
  C_YELLOW '\u001b[33m '
  C_RESET='\u001b[0m '
  echo -e "${C_YELLOW}[WARNING]: $* ${C_RESET}"
 }

until cd /app/
do
    echo "Waiting for server volume..."
done

pwd
ls -al

cd /api/

-case $CMD in
-  help)
-    _print_help
-  ;;
-
-  rundebugserver)
-    log_info "Start debug server"
-  ;;
-
-  shell)
-    log_info "Start Django shell"
-    python manage.py shell
-  ;;
-
-  test)
-    log_info "Start Django tests"
-    python manage.py test $--keepdb
-  ;;
-
-  coverage)
-    log_info "Generate tests coverage report"
-    coverage run --source='.' manage.py test . && coverage html -d ../htmlcov
-  ;;
-
-  *)
-    log_warn "Unknown command '$CMD'"
-  ;;
-esac

until ./manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

# python manage.py migrate
# python manage.py collectstatic --no-input

# gunicorn server.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
exec "$@"

```

```yml
version: '3.8'

services:

  # mongodb:
  #   container_name: rathma-mongodb
  #   image: mongo:5.0.8
  #   restart: always
  #   environment:
  #     - MONGO_INITDB_ROOT_USERNAME=admin
  #     - MONGO_INITDB_ROOT_PASSWORD=S3cret
  #   volumes:
  #     - mongodbdata:/data/db
  #   ports:
  #     - 27017:27017

  rathma-api:
    container_name: rathma-api
    restart: always
    build:
      context: ../api
      dockerfile: Dockerfile
      # target: prod
      # args:
      #   - SSH_PRV_KEY
    # environment:
    #   - MONGODB_URI=${MONGODB_URI}
    # networks:
    #   - rathma-net
    volumes:
      - ../api:/app/api
      # - api_node_modules:/node_modules/
    ports:
      # 0.0.0.0:${API_RUN_PORT:-8080}
      - 0.0.0.0:8080:8000
    depends_on:
      - pg_db
      # - mongo-express
```

[GitHub \#181717](https://github.com/filipgorczynski/gorczynski-docker-entrypoints)

<small class="unsplash-reference">
    Photo by <a href="https://unsplash.com/@carrier_lost?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ian Taylor</a> on <a href="https://unsplash.com/photos/jOqJbvo1P9g?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</small>
