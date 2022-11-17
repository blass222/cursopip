FROM python:3.8

WORKDIR /webserver
COPY requeriments.txt /webserver/requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /webserver/requeriments.txt

COPY . /webserver

CMD {"uvicorn", "main:webserver", "--host", "0.0.0.0", "--port", "80"}