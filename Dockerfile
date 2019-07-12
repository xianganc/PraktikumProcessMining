FROM ubuntu:19.04
ENV INITSYSTEM on

RUN apt-get update ;
RUN apt-get install -y \
  python3.6 \
  python3-pip \
  openssh-server \
  default-jre \
  curl \
  graphviz

RUN pip3 install pm4py flask opyenxes
