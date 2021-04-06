FROM python:3.7.3-slim
RUN apt update && apt-get -y install gcc
ADD . /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
EXPOSE 5050
CMD [ "python", "api.py" ]
