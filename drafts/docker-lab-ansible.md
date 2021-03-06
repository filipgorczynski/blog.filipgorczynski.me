Title: Docker Lab + Ansible
Date: 2018-04-16 14:30
Author: filipgorczynski
Category: Tech
Slug: docker-lab-ansible
Status: draft

https://docs.docker.com/engine/examples/running\_ssh\_service/

https://vsupalov.com/build-docker-image-clone-private-repo-ssh-key/

https://docs.ansible.com/ansible/2.4/ping\_module.html

http://docs.ansible.com/ansible/devel/user\_guide/intro\_getting\_started.html

https://docs.docker.com/docker-cloud/cloud-swarm/ssh-key-setup/\#about-ssh

https://medium.com/\@ali\_oguzhan/how-to-use-scrapy-with-django-application-c16fabd0e62e

Dockerfile

<div>

<div>

FROM ubuntu:16.04

</div>

<div>

RUN apt-get update && apt-get install -y openssh-server

</div>

<div>

RUN mkdir /var/run/sshd

</div>

<div>

RUN echo 'root:screencast' \| chpasswd

</div>

<div>

RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd\_config

</div>

<div>

\# SSH login fix. Otherwise user is kicked off after login

</div>

<div>

RUN sed 's\@session\\s\*required\\s\*pam\_loginuid.so\@session optional pam\_loginuid.so\@g' -i /etc/pam.d/sshd

</div>

<div>

ENV NOTVISIBLE "in users profile"

</div>

<div>

RUN echo "export VISIBLE=now" \>\> /etc/profile

</div>

<div>

EXPOSE 22

</div>

<div>

CMD \["/usr/sbin/sshd", "-D"\]

</div>

<div>

</div>

</div>

 

/etc/ansible/hosts

\# Local example of dockers  
\[dockerlab\]  
docker1.lab  
docker2.lab  
docker3.lab

 

/etc/hosts

\# Docker labs  
172.17.0.1 docker1.lab  
172.17.0.2 docker2.lab  
172.17.0.3 docker3.lab

 
