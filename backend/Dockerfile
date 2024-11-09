FROM python:3.12-alpine

RUN mkdir -p /home/app
WORKDIR /home/app
COPY . /home/app
RUN apk add --no-cache python3 postgresql-libs && \
apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
pip install -r requirements.txt && \
apk --purge del .build-deps

RUN export FLASK_APP=app.py

EXPOSE 5000

CMD ["python", "-u", "app.py"]