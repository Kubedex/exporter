FROM python:alpine
COPY src/ /app
WORKDIR /app
RUN apk add --no-cache gcc linux-headers make musl-dev python-dev g++
RUN pip install -r requirements.txt
EXPOSE 9484
CMD python ./kubedex.py
