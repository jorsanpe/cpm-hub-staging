FROM python:3.7

COPY ./cpm-hub-auth /cpm-hub-auth
WORKDIR /cpm-hub-auth
RUN pip install --upgrade flask

ENTRYPOINT ["python3", "cpm_hub_auth.py"]
