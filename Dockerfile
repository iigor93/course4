FROM python:3.8.10

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD flask run -p 80
