Simple docker image for quad9 DNS-over-TLS using stubby. Based on debian:testing-slim.

Includes the following scripts:

build.sh - build image locally
start.py - start container after build or pull
# --init -> enable interrupting the container with Ctrl+C
# -p 127.0.0.1:53:53/udp -> forward container 53:udp to localhost
docker run --init -p 127.0.0.1:53:53/udp mintooraj/stubby-quad9
stop.py - kill container
Docker hub: https://hub.docker.com/r/mintooraj/stubby-quad9/
