#Download base image ubuntu 16.04
FROM ubuntu:16.04

RUN echo "$LOG_TAG update and install basic packages" && \
    apt-get -y update && \
    apt-get install -y locales && \
    locale-gen en_US en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    apt-get install -y software-properties-common && \
    apt -y autoclean && \
    apt -y dist-upgrade && \
    apt-get install -y build-essential


RUN echo "$LOG_TAG Install python 3.6" && \
    add-apt-repository ppa:deadsnakes/ppa



RUN echo "$LOG_TAG Install python related packages" && \
    apt-get install -y python3-pip && \
    apt-get install libssl-dev && \
    apt-get install -y python-dev python-pip && \
    # virtualenv 
    apt-get install -y python3-venv
    # update pip
    pip3 install --upgrade pip && \
    # enable virtualenv
    python3 -m vevn env && source env/bin/activate && \
    # style guides pip dependency
    pip3 install pylint pep8 && \
    # numerical processing pip dependency
    pip3 install numpy && \
    
RUN echo "$LOG_TAG Cleanup" && \
    apt-get autoclean && \
    apt-get clean
