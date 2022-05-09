FROM node:18-alpine

WORKDIR /usr/src/app
COPY package*.json .

RUN npm --global install --no-audit --no-fund npm && \
    npm --no-audit --no-fund clean-install
