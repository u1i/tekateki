FROM alpine
MAINTAINER uli.hitzel@gmail.com

EXPOSE 8080

RUN apk update
RUN apk add python3
RUN apk add py3-pip
RUN mkdir /app
RUN pip3 install cherrypy bottle
COPY app /app

CMD ["python","/app/server.py"]
