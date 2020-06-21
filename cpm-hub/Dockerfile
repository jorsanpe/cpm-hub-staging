FROM python:3.7

COPY ./ /app
COPY ./public /app/public
COPY ./payment_checks /app/payment_checks
WORKDIR /app
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
