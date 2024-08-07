# maintainer info
FROM python:3.9-slim
LABEL maintainer="arung@adihara.com"

# copy requirements file
WORKDIR /app
COPY requirements.txt ./

# install python and dependences
RUN apk update
RUN apk add python3 py3-pip
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY app ./

# start command 
CMD ["sh","./prod.sh"]
EXPOSE 3000