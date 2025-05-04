FROM python:3.9-slim

RUN mkdir /app

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV PYTHONUNBUFFERED 1


CMD ["python", "app.py"]