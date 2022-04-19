FROM python:3.8.10

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .

CMD flask run -h 0.0.0.0 -p 8080
