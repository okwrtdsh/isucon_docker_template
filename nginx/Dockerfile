FROM nginx:latest
ARG ALP_ZIP_URL=https://github.com/tkuchiki/alp/releases/download/v1.0.21/alp_freebsd_amd64.zip
WORKDIR /tmp

RUN apt-get update -qq \
 && apt-get upgrade -y \
 && apt-get install --no-install-recommends -y \
    wget \
    jq \
    unzip \
    vim \
    neovim \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && wget "$ALP_ZIP_URL" -O alp.zip \
 && unzip alp.zip \
 && mv alp /usr/local/bin/

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
