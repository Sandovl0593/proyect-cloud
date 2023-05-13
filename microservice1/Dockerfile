FROM python:3-slim

WORKDIR /api-usuarios/app

RUN pip3 install flask
RUN pip3 install flask-Cors
RUN pip3 install flask-mysql
RUN pip3 install Flask-RESTful

ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

COPY . .

CMD ["flask", "run"]