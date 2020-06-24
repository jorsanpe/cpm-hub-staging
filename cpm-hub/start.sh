nohup ./active/cpm-hub -i active/cpmhub.ini &
echo $! > active/cpmhub.pid
nginx -p $(pwd) -c active/nginx.conf
