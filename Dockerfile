FROM python:3.8.4-alpine3.11

# Get source
#RUN mkdir /tmp
WORKDIR /tmp

#RUN apt-get install -y \
#        swig \
#        python-dev \
#        libssl-dev \
# && rm -rf /var/lib/apt/lists/*

COPY . /tmp

RUN export PYTHONPATH=/usr/bin/python \
 && pip install -r requirements.txt

# Run server
EXPOSE 5000

# CMD ["flask", "run", "-h", "localhost", "-p", "5000"]

CMD ["python", "app.py"]
