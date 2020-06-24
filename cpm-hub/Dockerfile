FROM ubuntu:20.04

ENV TZ=Europe/Madrid
RUN mkdir /cpm-hub-blue
RUN mkdir /cpm-hub-green
RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -yq libboost-all-dev nginx
COPY ./cpm-hub/build/cpm-hub /cpm-hub-blue
COPY ./cpm-hub/build/cpm-hub /cpm-hub-green
COPY ./cpmhub.ini /cpm-hub-blue/cpmhub.ini
COPY ./cpmhub.ini /cpm-hub-green/cpmhub.ini
RUN sed 
RUN ln -s /cpm-hub-blue /cpm-hub
WORKDIR /cpm-hub

ENTRYPOINT ["/cpm-hub/cpm-hub", "-i", "/cpm-hub/cpmhub.ini"]
