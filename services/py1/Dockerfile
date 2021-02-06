FROM python:3-buster

# WORKDIR /root
# ADD . /root

# install various things
RUN apt-get update && apt-get install -y \
  vim less

# Set OpenSSL SECLEVEL to 1
# see blog post https://medium.com/@edgar/how-to-resolve-openssl-sslv3-alert-handshake-failures-ruby-2-6-3-buster-cbc594537e7e
RUN sed -i.bak -e 's/SECLEVEL=2/SECLEVEL=1/' /usr/lib/ssl/openssl.cnf
