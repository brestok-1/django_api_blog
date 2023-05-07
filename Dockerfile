FROM python:3.10

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /api_service_blog2

ADD . /api_service_blog2

RUN pip install -r requirements.txt

COPY . .

