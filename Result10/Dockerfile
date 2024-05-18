FROM python:3.10-alpine AS base
WORKDIR /app
# EXPOSE 5000

RUN pip3 install -U Flask
RUN pip3 install -U flask-restplus

COPY ./Src /app/Src
COPY ./main.py /app/main.py


CMD ["python", "main.py"]



