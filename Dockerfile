from ubuntu:latest

RUN apt-get update && \
   # add-apt-repository ppa:jonathonf/python-3.6 
  apt-get install -y software-properties-common vim && \
  add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update -y

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv && \
        apt-get install -y git

# update pip
RUN python3.6 -m pip install pip --upgrade && \
        python3.6 -m pip install wheel

WORKDIR /templates

COPY . /templates

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["test1.py"]


