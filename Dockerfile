FROM python:3-slim

WORKDIR /app

COPY . /requirments.txt /app/

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "app.main:app","python"]