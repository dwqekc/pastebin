FROM python:3.10.12
WORKDIR /backend

RUN apt-get update && \
    apt-get install -y \
    wkhtmltopdf \
    xvfb \
    libfontconfig \
    libjpeg62-turbo \
    libxrender1

RUN mkdir "tmp"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1