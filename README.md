Django base setup
=================

This is the basic setup for a new django project.

---------------------------------------------------------------

**Before anything else** :

    sudo apt-get install libmysqlclient-dev python-dev python-mysqldb
    
In the following commands, replace base by the name you want for your site.
Open all files you're asked to `cp` to change the name of the site as well.

**Installing the server** :

    sudo apt-get install nginx
    cp base_nginx base_nginx-ssl /etc/nginx/sites-available/base.conf
    ln -s /etc/nginx/sites-available/base.conf /etc/nginx/sites-enabled/base
    ln -s /etc/nginx/sites-available/base-ssl.conf /etc/nginx/sites-enabled/base-ssl
    openssl req -new -newkey rsa:2048 -nodes -keyout base.key -out base.csr
    openssl x509 -req -days 365 -in base.csr -signkey base.key -out base.crt
    sudo cp base.key base.crt base.csr /etc/nginx/ssl/
    service nginx restart

**Installing the virtualenv** :

    pip install virtualenvwrapper mkdir ~/.virtualenvs ~/.pip_packages
    echo -e "export WORKON_HOME=$HOME/.virtualenvs\nexport PIP_DOWNLOAD_CACHE=$HOME/.pip_packages\nexport PROJECT_HOME=$HOME/\nsource /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
    source ~/.bashrc
    mkvirtualenv base
    workon base
    pip install -r ../requirements.txt

**Setting upstart script** :

    cp base.conf /etc/init/
    ln -fs /lib/init/upstart-job /etc/init.d/base
    update-rc.d base defaults
    service base start

