# Let's start with a python 3.12 slim image
FROM python:3.12.2-slim

# Set the working directory in the container
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential wget

RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
    tar -xzf ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib/ && \
    ./configure --prefix=/usr --build=aarch64-unknown-linux-gnu && \
    make && \
    make install && \
    cd .. && \
    rm -rf ta-lib*

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

CMD ["python3", "src/training.py"]


