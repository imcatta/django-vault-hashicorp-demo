FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
COPY requirements.txt /code/
RUN \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps