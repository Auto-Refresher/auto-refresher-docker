FROM python:latest

LABEL BUILDING REFRESHER

COPY ./requirements.txt ./app/requirements.txt

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update -y 

COPY . /app

CMD [ "python", "main.py"]