FROM python:3.9.1

RUN pip install psycopg2

WORKDIR /app

COPY main.py main.py

EXPOSE 5432

ENTRYPOINT [ "python", "main.py" ]