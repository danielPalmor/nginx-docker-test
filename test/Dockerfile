FROM python:3.12-alpine

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

COPY test.py test.py

CMD ["python3", "test.py"]