.PHONY: default, dev-install, upload

default: dev-install

completion:
	sudo cp ./utils/_pueue /usr/share/zsh/site-functions/_pueue

dev-install:
	sudo python setup.py develop

clean:
	sudo rm -rf dist
	sudo rm -rf build
	sudo rm -rf pueue.egg-info

dist:
	sudo python setup.py sdist --formats=gztar,zip

upload: clean dist
	twine upload dist/*

setup:
	virtualenv -p python3 venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
