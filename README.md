λ - lmb - Lambda Labs Core API
======

## Features

- Facial Detection
- Gender Classification
- Activity Monitoring

## Install

For now:

git clone git@github.com:lambdal/lmb.git

Soon:

curl http://www.lambdal.com/install.sh | sh

### Install Process

One step:

```bash
./install.sh
```


## Command Line Tools

**```lmb```** can also be accessed via a suite of well-designed command line tools.

- ```lmb draw```: draw boxes around images
- ```lmb detect```: detect features in an image, pipe this to ```lmb draw``` to draw each feature!
- ```lmb gallery```: create an HTML image gallery

Examples:

Draw a box on file.jpg at origin (0, 0) with a width and height of 30 px:
```
lmb draw file.jpg box 0 0 30 30
```

Find the faces in an image online:
```
lmb detect http://www.lambdal.com/test.jpg
```

Find the face and view it in an image gallery in your browser:
```
lmb detect http://www.lambdal.com/test.jpg | grep face | lmb draw | lmb gallery > index.html && open index.html
```

Find the faces in all your photos:
```
ls ~/Pictures/*.jpg | lmb detect
```

Find faces in all of your pictures, draw boxes around them, and put them into an image gallery!
```
ls ~/Pictures/*.{jpg,png} | lmb detect | grep face | lmb draw | xargs lmb gallery > index.html && open index.html
```



## License

Released under the BSD 3-clause. See LICENSE for more details.
