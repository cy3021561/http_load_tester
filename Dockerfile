FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN pip install .

ENTRYPOINT ["http_load_tester"]
