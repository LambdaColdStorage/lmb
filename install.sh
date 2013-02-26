#!/bin/sh
NAME=lmb
IS_OSX=1
CWD=`dirname $0`

function setup_venv {
	mkvirtualenv --clear --no-site-packages --distribute $NAME
	pip install -r $CWD/requirements.txt
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
	install_opencv;
	install_pip_packs;
}

function download_cascade {
	CASCADE_FF=https://jviolajones.googlecode.com/files/haarcascade_frontalface_default.xml
	echo "# Downloading Haar Cascades from $CASCADE_FF"
	curl $CASCADE_FF > $CWD/lmb/cascades/haarcascade_frontalface_default.xml
}

download_cascade;
echo DONE
echo
echo '# Add this to your .bashrc, .zshrc, .profile, or .bash_profile:'
echo
echo export PATH='$PATH':"$PWD/scripts/"
echo
