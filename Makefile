

test: hod/.venv/bin/activate
	. ./hod/.venv/bin/activate && ./manage.py test --failfast --noinput apps

test-end:
	. .
hod/.venv/bin/activate:
	cd ./hod && bash update_venv.sh

