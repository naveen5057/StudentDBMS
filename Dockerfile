FROM python:3.6-alpine

WORKDIR /app/
EXPOSE 8000

COPY StudentDatabaseMgmt/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./StudentDatabaseMgmt /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app
RUN ls
RUN pip3 install -r requirements.txt
EXPOSE 8000

CMD [ "python", "manage.py",  "runserver",  "0.0.0.0:8000"]