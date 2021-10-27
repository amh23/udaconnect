FROM python:3.8

WORKDIR .

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5005

CMD ["python", "app/person_grpc_server.py"]