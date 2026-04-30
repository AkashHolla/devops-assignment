# Service A Dockerfile
FROM python:3.11

WORKDIR /app
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -r requirements.txt

ENV SECRET_KEY=supersecret123
ENV DB_PASSWORD=admin1234

EXPOSE 5000

USER root

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
