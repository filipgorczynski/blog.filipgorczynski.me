Title: Dockerized MERN stack
Date: 2022-02-05 07:31
Modified: 2022-02-05 07:31
Category: Tech
Tags: #docker, #mern, #mongo, #expressjs, #reactjs, #nodejs
Slug: dockerized-mern-stack
Author: filipgorczynski
Status: draft
Cover: https://blog.filipgorczynski.me/images/post/2022/01/photo-1556075798-4825dfaaf498.jpg
meta_url: https://blog.filipgorczynski.me/2022/01/deploy-blog-changes-to-ftp-server-on-git-push
Summary: I was a Python (Django + DRF) and JavaScript (mostly Vue) developer few years now. Time changes and new tools showing up. It's impossible to know them all but it's nice to learn at least some of them. MERN stack sounds like a good choice.

I was a Python (Django + DRF) and JavaScript (mostly Vue) developer few years now. Time changes and new tools showing up. It's impossible to know them all but it's nice to learn at least some of them. MERN stack sounds like a good choice.

However, MERN is not a single technology. It's a group of technologies that can be used together to build a full stack applications.

It's stands from MongoDB, ExpressJS, ReactJS and NodeJS. And it's because they're work pretty well together and allows to build full-stack applications with JavaScript language only.

Installing them one-by-one is pretty easy, but using them in dockerized environment may be a bit confusing. The problem I've found was with Docker volumes and node_modules directory. Why? Let's 
