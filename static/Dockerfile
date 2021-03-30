FROM node:14-alpine

WORKDIR /usr/src/app
COPY package*.json .
RUN npm clean-install

COPY . .

CMD ["npm", "start"]
