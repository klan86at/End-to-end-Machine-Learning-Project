FROM python:3.12-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . .

RUN pip install -r reqiurements.txt

CMD ["python3", "app.py"]