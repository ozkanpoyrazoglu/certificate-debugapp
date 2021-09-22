FROM python:3.6.1-alpine

WORKDIR /flask-project

ADD . /flask-project

RUN pip install -r requirements.txt

RUN apk upgrade --update-cache --available && \
    apk add openssl && \
    rm -rf /var/cache/apk/*

EXPOSE 5000

CMD ["python", "hello.py"]