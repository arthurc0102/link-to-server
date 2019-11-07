FROM python:3.8-alpine

WORKDIR /src

VOLUME /src/log
VOLUME /src/media
VOLUME /src/assets

EXPOSE 8000

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN apk add --update --no-cache --virtual build-deps \
        build-base linux-headers libc-dev \
        pcre-dev && \
    \
    apk add --no-cache \
        libuuid pcre mailcap logrotate \
        musl-dev libxslt-dev libffi-dev \
        jpeg-dev zlib-dev postgresql-dev && \
    \
    pip3 install --no-cache-dir pipenv uwsgi && \
    pipenv install --system --deploy --ignore-pipfile -v && \
    \
    apk del build-deps && \
    rm -rf ~/.cache

COPY ./src /src
COPY ./docker /docker

RUN mv /docker/docker-entrypoint.sh /usr/local/bin/entrypoint && \
    chmod +x /usr/local/bin/entrypoint && \
    \
    mv /docker/django.logrotate.conf /etc/logrotate.d/django && \
    mv /docker/django-logrotate.sh /etc/periodic/daily/django-logrotate && \
    chmod +x /etc/periodic/daily/django-logrotate

ENTRYPOINT [ "entrypoint" ]
CMD [ "uwsgi", "--ini", "/docker/uwsgi.ini" ]
