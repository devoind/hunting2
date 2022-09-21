FROM python:3.10-slim

WORKDIR /opt/hunting

RUN groupadd --system service && useradd --system -g service api

RUN apt-get update -y && apt-get install -y --no-install-recommends curl \
    && apt-get autoclean && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . .

USER api

ENTRYPOINT ["bash", "entrypoint.sh"]
