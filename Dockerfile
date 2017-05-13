FROM debian:8.7
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python offlineimap
COPY ./data/ /opt/
COPY ./data/mailtotelegram/.offlineimaprc ./root
RUN mkdir /root/mail
COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
