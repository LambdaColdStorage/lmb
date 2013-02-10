#!/bin/sh
SWF=`find . | grep .*.sw[a-z]`
PYCF=`find . | grep *.pyc`
if [ -n "$SWF" ]; then
	echo Removing swap files. $SWF
	rm $SWF
fi;
if [ -n "$PYCF" ]; then
	echo Removing pyc files. $PYCF
	rm $PYCF
fi;
echo Done.
