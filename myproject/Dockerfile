FROM python:3.9

ENV PYTHONBUFFERED 1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 6969

CMD ["python", "manage.py", "runserver", "0.0.0.0:6969"]
