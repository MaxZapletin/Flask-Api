FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/main.py
COPY ./tasks.json /app/tasks.json

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["main.py" ]