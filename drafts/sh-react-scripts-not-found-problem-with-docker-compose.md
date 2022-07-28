Title: sh: react-scripts: not found problem with docker-compose
Date: 2021-11-22 19:13
Modified: 2021-11-22 19:13
Category: Tech
Tags: #docker, #volumes, #docker-compose
Slug: sh-react-scripts-not-found-problem-with-docker-compose
Author: filipgorczynski
Status: draft
meta_og_title: sh: react-scripts: not found problem with docker-compose
meta_og_description:
meta_og_url: https://blog.filipgorczynski.me/
meta_og_image:
Summary: Dockerfile CMD failes with sh: react-scripts: not found, but works fine when called manually

Reference: https://stackoverflow.com/questions/68322528/docker-missing-script-dev-but-its-there
Hello there,
I'm out of ideas right now.
I have a simple Dockerfile:

```Dockerfile
FROM node:lts-alpine
WORKDIR /app
COPY ./package.json .
RUN npm i
COPY ./ ./
EXPOSE 3000
CMD ["npm", "run", "start"]

```

and docker-compose.yml

```yml
version: '3.7'

services:
  client:
    build:
      context: ./app
      dockerfile: Dockerfile
    environment:
      CHOKIDAR_USEPOLLING: 'true'
    volumes:
      - ./app:/app
    ports:
      - '3000:3000'

volumes:
  app:
```

IMO, both files are quite self-explanatory.

I've decided to add some bash script to make everything faster, so it looks like:

```bash
#!/usr/bin/env bash

docker container prune -f;
docker image prune -a -f;
docker volume prune -f;
docker system prune -a -f;
docker-compose up --build --remove-orphans --force-recreate;
```

I've tried:

- to change directory name (previously it had period in it)
- to play with docker-compose.[dev|develop|prod].yml and Dockerfile[.dev|.prod] file names
- renamed the application directory from `client` to `app` to have identical structure with the clean project - where it works correctly (package.json files are identical, "name" key in that file was changed accordingly to reflect directory name changes `"name": "app"`
- to install `react-scripts` globally as independent Dockerfile instruction
- to add `$(npm bin)/react-scripts start` for package.json scripts
- compared the same package versions between non-working and working project
- to mount node_modules as a separate volume
- to change `CMD ["npm", "start"]` and `CMD ["npm", "run", "start"]`

The funny thing is that I wanted to reproduce the problem on a clean project - and it worked perfectly.
