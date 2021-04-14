FROM python:3.7

EXPOSE 5000 

WORKDIR /app

COPY src .
COPY templates .
COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python main.py