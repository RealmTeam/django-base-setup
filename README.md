base
===

Arboressence basique d'un site django


sudo apt-get install libmysqlclient-dev
sudo apt-get install python-dev

apt-get install nginx
cp base_nginx base_nginx-ssl /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/base_nginx /etc/nginx/sites-enabled/base_nginx
ln -s /etc/nginx/sites-available/base_nginx-ssl /etc/nginx/sites-enabled/base_nginx-ssl
openssl req -new -newkey rsa:2048 -nodes -keyout base.key -out base.csr
openssl x509 -req -days 365 -in base.csr -signkey base.key -out base.crt
cp base.key base.crt base.csr /etc/nginx/ssl/
service nginx restart

pip install virtualenvwrapper
mkdir ~/.virtualenvs ~/.pip_packages

add these 4 lines to ~/.bashrc :
export WORKON_HOME=$HOME/.virtualenvs
export PIP_DOWNLOAD_CACHE=$HOME/.pip_packages
export PROJECT_HOME=$HOME/
source /usr/local/bin/virtualenvwrapper.sh

source ~/.bashrc
mkvirtualenv base
workon base
pip install -r ../requirements.txt

cp base.conf /etc/init/
ln -fs /lib/init/upstart-job /etc/init.d/base
update-rc.d base defaults
service base start