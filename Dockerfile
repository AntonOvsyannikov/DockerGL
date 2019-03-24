FROM python:2.7

RUN apt-get update
RUN apt-get install -y python-opengl=3.1.0+dfsg-1 libosmesa6=13.0.6-1+b2

WORKDIR /home
ADD requirements.txt /home
RUN pip install -r requirements.txt

ENV PYOPENGL_PLATFORM=osmesa
