#!/bin/bash
ACTIVE=$(basename $(readlink -f active))
NEXT_ACTIVE=$(test $ACTIVE == "green" && echo "blue" || echo "green")

rm active
ln -s $NEXT_ACTIVE active

nohup ./active/cpm-hub -i active/cpmhub.ini &
echo $! > active/cpmhub.pid
nginx -p . -c active/nginx.conf -s reload
kill -SIGTERM $(cat $ACTIVE/cpmhub.pid)
