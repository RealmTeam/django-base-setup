==========================
Django + React boilerplate
==========================


This is the basic setup for a new django project.

-------------------------------------------------------------------------------------------------------

****************
Where to start ?
****************



Installing the development environment :
========================================

Server :
--------

Before anything else :
::

    sudo apt-get install libmysqlclient-dev python-dev python-mysqldb

Install the cache handler :
::

    sudo apt-get install memcached

Setup the virtualenv :
::

    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

If you don't have virtualenv or pip :
::

    sudo apt-get install python-setuptools
    sudo easy_install pip
    sudo pip install virtualenv

If you want to use celery :
::

    sudo apt-get install redis-server

Front :
-------

Before anything else :
::

    sudo apt-get install nodejs npm
    sudo npm install -g yarn

Installing front dependencies :
::

    cd front && yarn install && cd ..


Running the server :
====================
::

    source .venv/bin/activate
    python manage.py runserver

Running celery :
================
::

    source .venv/bin/activate
    celery --app=main.celery:app worker --loglevel=INFO -B

Running the front :
===================
::

    source .venv/bin/activate
    python manage.py runfront

-------------------------------------------------------------------------------------------------------

*************************************
Setting up the production environment
*************************************

Before anything else :
======================

In the following commands, replace `{{name}}` by the name you want for your site.

You can also run `python manage.py configuredeployment` which will configure  
all the files for you and change these commands accordingly.

Generating certificate for https :
==================================

::

    openssl req -new -newkey rsa:2048 -nodes -keyout nginx/ssl/{{name}}.key -out nginx/ssl/{{name}}.csr
    openssl x509 -req -days 365 -in nginx/ssl/{{name}}.csr -signkey nginx/ssl/{{name}}.key -out nginx/ssl/{{name}}.crt

Installing docker :
===================

::

    sudo sh -c "wget -qO- https://get.docker.io/gpg | apt-key add -"
    sudo sh -c "echo deb http://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list"
    sudo aptitude update
    sudo aptitude install lxc-docker
    sudo gpasswd -a ${USER} docker
    sudo service docker restart
    newgrp docker

Creating and running our stack :
================================

::

    docker-compose up -d
    # Alternatively, you can use the DEBUG environment variable to launch in prod or in dev
    DEBUG=True docker-compose up -d

Checking if the stack is running :
==================================

::

    docker-compose ps

Get shell access to a container :
=================================

::

    docker-compose exec api bash

Display the logs from the stack :
=================================

::

    docker-compose logs -f

Stopping and Destroying the stack :
===================================

::

    docker-compose down

Stopping the stack :
====================

::

    docker-compose stop

Starting the stack :
====================

::

    docker-compose start


