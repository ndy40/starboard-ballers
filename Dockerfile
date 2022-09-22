FROM node:18-alpine AS nodebase
WORKDIR /code
COPY client/package*.json /code/
RUN npm upgrade npm;  \
    npm install -g vite@latest; \
    npm install --save-dev;


FROM nodebase AS nodedev
ENV NODE_ENV=dev
WORKDIR /code/
COPY --from=nodebase /code/node_modules /code/node_modules
COPY ./client /code/
RUN npm install --save-dev

CMD npm run watch-build


FROM python:3.10-alpine AS pythondev
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
