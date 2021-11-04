FROM python:latest

LABEL BUILDING REFRESHER

COPY ./requirements.txt ./app/requirements.txt

# Add wait-for-it
COPY wait-for-it/wait-for-it.sh wait-for-it.sh 
RUN chmod +x wait-for-it.sh

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update -y 

COPY . /app


#ENTRYPOINT [ "/bin/bash", "-c" ]
#CMD ["./wait-for-it.sh" , "--host=http://web-chrome", "--port=4444" , "--strict" , "--timeout=2000" , "--" , "python main.py"]
CMD [ "python", "main.py"]