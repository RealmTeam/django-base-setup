#!/bin/sh -e

now () {
    date "+[%d/%m/%Y - %R:%S]"
}

echo $(now) "cd into" $(dirname "$0")
cd $(dirname "$0")


projectname=$(basename $(pwd))
echo $(now) activating virtualenv $projectname
. ~/.virtualenvs/$projectname/bin/activate
 
unset GIT_DIR

echo $(now) pulling changes
git pull

echo $(now) installing requirements
pip install -r requirements.txt 

echo $(now) collecting static files
./manage.py collectstatic --noinput
