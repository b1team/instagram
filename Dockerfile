FROM python:3.6-buster
RUN useradd -u 1612 deploy && \
    mkdir /app && \
    chown -R deploy:deploy /app 
WORKDIR /app
COPY . .

RUN pip install -e .
USER deploy
ENV PYTHONPATH=/app
