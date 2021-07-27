FROM python:3.8.7-slim

WORKDIR /var/app

EXPOSE 8000

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN pip3 install --no-cache-dir pipenv \
  && pipenv install --system --deploy --ignore-pipfile -v

COPY ./src .
COPY ./docker /docker

RUN mv /docker/run-* /usr/local/bin \
  && chmod +x /usr/local/bin/run-* \
  && rm -rvf /docker

CMD [ "run-server" ]
