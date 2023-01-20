


FROM node:19-alpine3.16


RUN mkdir /client
RUN chmod a+rwx /client

COPY ./client/pnpm-lock.yaml /client/

COPY ./client/package.json /client/

EXPOSE 3000

WORKDIR /client


COPY ./compose/local/client/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./client /client


CMD npm install; npm run dev;
