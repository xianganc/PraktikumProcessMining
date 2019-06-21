FROM ubuntu:18.04
ENV INITSYSTEM on

RUN apt-get update ;
RUN apt-get install -y \
  python3.6 \
  python3-pip \
  openssh-server \
  default-jre

RUN pip3 install pm4py flask xes