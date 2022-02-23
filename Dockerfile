FROM python:3-slim

WORKDIR /app

COPY . /requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "main:app"]