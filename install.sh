#!/bin/sh
NAME=lmb
IS_OSX=1

mkvirtualenv --clear --no-site-packages --distribute $NAME

function install_cairo {
	brew install cairo
}

function install_opencv{
	echo "# Install OpenCV"
	echo "# Link OpenCV"
	if [[ $IS_OSX ]]; then
		ln -s /usr/local/lib/python2.7/site-packages/cv2.so ~/.virtualenvs/lmb/lib/python2.7/site-packages/cv2.so
		ln -s /usr/local/lib/python2.7/site-packages/cv.py ~/.virtualenvs/lmb/lib/python2.7/site-packages/cv.py
	fi;
}

function install_pip_packs {
	echo "# Installing PIP Packages:
	cat requirements.txt
	pip install -r requirements.txt
}

# graphics lib
install_cairo;
install_opencv;
install_pip_packs;
