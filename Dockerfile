# Build an image that can serve mlflow models.
FROM ubuntu:latest

RUN apt-get -y update

RUN apt-get install -y python3 && apt-get install -y python3-pip python3-dev && cd /usr/local/bin && ln -s /usr/bin/python3 python && pip3 install flask

RUN pip install pyyaml

COPY webapp .

RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

EXPOSE 5555

CMD ["python","app.py"]
