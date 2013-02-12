#!/bin/sh
function check {
	TASK=$1
	EVAL=$2
	HARD=$3
	echo
	echo $TASK
	echo "$EVAL"
	eval $EVAL
	[ $? -eq 0 ] && echo DONE || echo FAIL
}

function setup {
	python -c"import lmb; lmb.run()" &
	server_pid=$!
}

function teardown {
	kill -9 $server_pid
}


setup;
check "LINTING" "./check.py" --hard
check "TESTING" "nosetests --exe lmb"
teardown;
