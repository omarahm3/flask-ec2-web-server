from python:3.8

WORKDIR /server

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "server.py"]
