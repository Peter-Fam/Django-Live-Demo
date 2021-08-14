# pull official base image
FROM python:3.9.6-slim

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# create the app user --system as not create home directory for the user
RUN addgroup --system app && adduser --system --group app

# create directory for the app user
RUN mkdir -p /home/app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Copy requirements to make use of docker cache
COPY ./Pipfile $APP_HOME
COPY ./Pipfile.lock $APP_HOME
# install pip and pipenv
RUN pip install --upgrade pip
RUN pip install pipenv
# install dependencies
RUN pipenv install --system --deploy

# copy project
COPY . $APP_HOME
# chown all the files to the app user
RUN chown -R app:app $HOME
RUN chown -R app:app $APP_HOME
# change to the app user
USER app
ENTRYPOINT ["./entry-point.sh"]
