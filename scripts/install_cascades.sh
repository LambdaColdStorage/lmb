#!/bin/sh
outdir=$1
cascades="haarcascade_frontalface_default.xml"
echo "Putting cascades ($cascades) in $outdir"
for f in $cascades; do
	curl http://jviolajones.googlecode.com/files/$f > $outdir/$f
done;

