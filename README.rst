=================
Django base setup
=================


This is the basic setup for a new django project.

-------------------------------------------------------------------------------------------------------

****************
Where to start ?
****************



Installing the development environment :
========================================

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


Running the server :
====================
::

    source .venv/bin/activate
    python manage.py runserver

Running celery :
================
::

    celery --app=base.celery:app worker --loglevel=INFO


-------------------------------------------------------------------------------------------------------

*************************************
Setting up the production environment
*************************************

Before anything else :
======================

::

    sudo apt-get install libmysqlclient-dev python-dev python-mysqldb

In the following commands, replace `{{base}}` by the name you want for your site.
Open all files you're asked to `cp` to change the name of the site as well.

You can also run `python manage.py configuredeployment` which will configure  
all the files for you and change these commands accordingly.

Installing the server :
=======================

::

    sudo apt-get install nginx
    sudo cp public/base_nginx /etc/nginx/sites-available/{{base}}.conf
    sudo cp public/base_nginx-ssl /etc/nginx/sites-available/{{base}}-ssl.conf
    sudo ln -s /etc/nginx/sites-available/{{base}}.conf /etc/nginx/sites-enabled/{{base}}
    sudo ln -s /etc/nginx/sites-available/{{base}}-ssl.conf /etc/nginx/sites-enabled/{{base}}-ssl
    openssl req -new -newkey rsa:2048 -nodes -keyout {{base}}.key -out {{base}}.csr
    openssl x509 -req -days 365 -in {{base}}.csr -signkey {{base}}.key -out {{base}}.crt
    sudo mkdir /etc/nginx/ssl
    sudo mv {{base}}.key {{base}}.crt {{base}}.csr /etc/nginx/ssl/
    sudo service nginx restart

Installing the virtualenv :
===========================

::

    sudo pip install virtualenvwrapper
    mkdir ~/.virtualenvs ~/.pip_packages
    echo -e "export WORKON_HOME=$HOME/.virtualenvs\nexport PIP_DOWNLOAD_CACHE=$HOME/.pip_packages\nexport PROJECT_HOME=$HOME/\nsource /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
    source ~/.bashrc
    mkvirtualenv {{base}}
    workon {{base}}
    pip install -r requirements.txt


If you don't have virtualenv or pip :
::

    sudo apt-get install python-setuptools
    sudo easy_install pip
    sudo pip install virtualenv


Setting upstart script :
========================

::

    sudo cp public/base.conf /etc/init/{{base}}.conf
    sudo ln -fs /lib/init/upstart-job /etc/init.d/{{base}}
    sudo update-rc.d {{base}} defaults
    sudo service {{base}} start

Installing celery :
===================

::

    sudo apt-get install redis-server supervisor
    sudo cp public/celery_worker.conf /etc/supervisor/conf.d/{{base}}_celery_worker.conf
    sudo supervisorctl reread
    sudo supervisorctl update

-------------------------------------------------------------------------------------------------------

************
Using docker
************

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

Building our app :
==================

::

    docker build -t {{base}}-image .

Running dependencies :
======================

::

    docker run --name {{base}}-nginx -v public/nginx_docker:/etc/nginx/sites-enabled/{{base}}.conf:ro -d nginx
    docker run --name {{base}}-db -e MYSQL_ROOT_PASSWORD=rootpassword -e MYSQL_DATABASE=db_name -e MYSQL_USER=user -e MYSQL_PASSWORD=password -d mysql


Running our container :
=======================

::

    docker run --name {{base}} --link {{base}}-db:mysql -p {{port}}:8000 -d {{base}}-image

Get shell access to the container :
===================================

::

    docker exec -it {{base}} bash
