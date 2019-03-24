FROM python:2.7

RUN apt-get update
RUN apt-get install -y python-opengl libosmesa6

WORKDIR /home
ADD requirements.txt /home
RUN pip install -r requirements.txt

ENV PYOPENGL_PLATFORM=osmesa
