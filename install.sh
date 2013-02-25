#!/bin/sh
NAME=lmb
IS_OSX=1

function setup_venv {
	mkvirtualenv --clear --no-site-packages --distribute $NAME
}
# https://github.com/LearnBoost/node-canvas/wiki/Installation---OSX

function install_pycairo {
	brew install py2cairo
}

function install_pixman {
	curl http://www.cairographics.org/releases/pixman-0.20.0.tar.gz -o pixman.tar.gz
	tar -zxf pixman.tar.gz && cd pixman-0.20.0/
	./configure --prefix=/usr/local --disable-dependency-tracking
	make install
}

function install_cairo {
	brew install libpng
	curl http://cairographics.org/releases/cairo-1.10.0.tar.gz -o cairo.tar.gz
	tar -zxf cairo.tar.gz && cd cairo-1.10.0
	./configure --prefix=/usr/local --disable-dependency-tracking
	make install
}

function install_opencv {
	echo "# Install OpenCV"
	echo "# Link OpenCV"
	if [[ $IS_OSX ]]; then
		ln -s /usr/local/lib/python2.7/site-packages/cv2.so ~/.virtualenvs/lmb/lib/python2.7/site-packages/cv2.so
		ln -s /usr/local/lib/python2.7/site-packages/cv.py ~/.virtualenvs/lmb/lib/python2.7/site-packages/cv.py
	fi;
}

function install_pip_packs {
	echo "# Installing PIP Packages:"
	cat requirements.txt
	pip install -r requirements.txt
}

function install_lmb {
	setup_venv;
	install_cairo;
	install_opencv;
	install_pip_packs;
}
