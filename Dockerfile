FROM python:3.9
WORKDIR /apps

RUN apt update && apt install -y python3-pip python3-devel gcc
ADD ./main.py /main.py
CMD python3 main.py