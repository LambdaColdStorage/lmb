λ - lmb - Lambda Labs Core API
======

## Features

- Facial Detection
- Gender Classification
- Activity Monitoring

## Install

curl http://www.lambdal.com/lmb.sh | sh


### Install Process

One step:

```bash
./install.sh
```

1) Install pip packages in requirements.txt

```bash
pip install -r requirements.txt
```

2) Install OpenCV

3) Link shared objects:

After installing OpenCV, link the shared object and python wrapper into the
virtualenv.

On OSX:
```bash
ln -s /usr/local/lib/python2.7/site-packages/cv2.so ~/.virtualenvs/lmb/lib/python2.7/site-packages/cv2.so
ln -s /usr/local/lib/python2.7/site-packages/cv.py ~/.virtualenvs/lmb/lib/python2.7/site-packages/cv.py
```

## License

Released under the BSD 3-clause. See LICENSE for more details.
