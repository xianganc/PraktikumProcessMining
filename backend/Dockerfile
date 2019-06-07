FROM ubuntu:18.04
ENV INITSYSTEM on

RUN mkdir -p \
  /deps \
  /src \
  /run/sshd \
  /root/.ssh \
  /data

COPY ./backend/deps/ /deps/
COPY ./backend/app/ /src/
COPY ./sshFile/authorized_keys /root/.ssh/authorized_keys
COPY ./sshFile/aws_ssh /root/.ssh/id_rsa
COPY ./hadoop/ /src/

RUN chmod +x /deps/deps.sh && /deps/deps.sh && chmod +x /deps/init.sh

CMD /deps/init.sh
