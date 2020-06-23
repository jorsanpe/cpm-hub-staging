FROM ubuntu:20.04

ENV TZ=Europe/Madrid
RUN mkdir /cpm-hub
RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -yq libboost-all-dev
COPY ./cpm-hub/build/cpm-hub /cpm-hub
COPY ./cpmhub.ini /cpm-hub/cpmhub.ini
WORKDIR /cpm-hub

ENTRYPOINT ["/cpm-hub/cpm-hub", "-i", "/cpm-hub/cpmhub.ini"]
