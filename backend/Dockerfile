FROM ubuntu:18.04
ENV INITSYSTEM on

RUN mkdir -p \
  /deps \
  /src/bin \
  /run/sshd \
  /root/.ssh \
  /data

COPY ./backend/deps/ /deps/
COPY ./backend/app/ /src/
COPY ./hadoop/bin/ /src/bin/
COPY ./sshFile/authorized_keys /root/.ssh/authorized_keys

RUN chmod +x /deps/deps.sh && /deps/deps.sh && chmod +x /deps/init.sh

CMD /deps/init.sh
