FROM python:3.12-bookworm

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 4001

CMD ["python", "./app/manage.py", "runserver", "0.0.0.0:4001"]