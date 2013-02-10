#!/bin/sh
function check {\
	TASK=$1
	EVAL=$2
	echo $TASK
	echo "$EVAL"
	eval $EVAL
	[ $? -eq 0 ] && echo OK || echo FAIL
}

check "LINTING" "./check.py --git-index"
check "TESTING" "nosetests --exe lmb"
