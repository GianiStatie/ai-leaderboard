FROM python:3.11-slim-buster

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 4001

CMD ["python", "./app/manage.py", "runserver", "0.0.0.0:4001"]