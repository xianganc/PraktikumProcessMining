FROM processmining:latest
ENV INITSYSTEM on


RUN mkdir -p \
  /deps \
  /src \
  /run/sshd \
  /root/.ssh \
  /var/www \
  /data

COPY ./frontend/deps/ /deps/
COPY ./frontend/webapp/ /var/www/
COPY ./sshFile/authorized_keys /root/.ssh/authorized_keys


RUN chmod +x /deps/*.sh

CMD /deps/init.sh