FROM python:2

ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD requirements.txt /app/
ADD . /app
RUN pip install -r requirements.txt

CMD [ "python", "./server.py" ]

EXPOSE 8000