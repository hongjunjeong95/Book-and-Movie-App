FROM python:3.6.7
ENV PYTHONUNBUFFERED 1
RUN apt-get -y update
RUN apt -y install vim
RUN mkdir /srv/docker-server
COPY . /srv/docker-server
WORKDIR /srv/docker-server
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]