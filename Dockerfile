FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python2.7 python-pip

RUN apt-get install -y python-opengl=3.1.0+dfsg-1 libosmesa6=19.0.8-0ubuntu0~18.04.2

# try this if no version available
# RUN apt-get install -y python-opengl libosmesa6

WORKDIR /home
ADD requirements.txt /home
RUN pip install -r requirements.txt

ENV PYOPENGL_PLATFORM=osmesa
