kill -SIGTERM $(cat active/cpmhub.pid)
nginx -p $(pwd) -c active/nginx -s stop

