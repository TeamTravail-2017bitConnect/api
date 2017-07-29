#! /bin/sh
HOME=/home/ec2-user
GUNICORN=$HOME/.pyenv/shims/gunicorn
PID=$HOME/PID
cmd=`cat $PID`
errorlog=/var/log/gunicorn/error-log

rm app.zip
zip -r app.zip app/*
scp -i travail.pem app.zip ec2-user@52.192.108.213:$HOME/app.zip
ssh -i travail.pem ec2-user@52.192.108.213 "rm -rf travail"
ssh -i travail.pem ec2-user@52.192.108.213 sh stop.sh
ssh -i travail.pem ec2-user@52.192.108.213 unzip -o app.zip -d travail
#ssh -i travail.pem ec2-user@52.192.108.213 sh load.sh


